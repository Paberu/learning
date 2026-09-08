import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.file.StandardCopyOption;
import java.util.Enumeration;
import java.util.zip.ZipEntry;
import java.util.zip.ZipFile;
import java.util.zip.ZipOutputStream;

public class ZipUtils {

    // лучше было бы использовать Zip4j, но тогда задача решается одной строкой, а это уже не учёба, а читинг )))
    public static void addFilesToZip(String zipFilename, String[] filenames) {
        Path tempZipFile; // создаётся файл для временного хранения архивных данных
        try {
            Path currentDir = Paths.get("").toAbsolutePath(); // или Paths.get(".")
            tempZipFile = Files.createTempFile(currentDir, "zip_update", ".zip");
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
        try (ZipOutputStream zipOutputStream = new ZipOutputStream(new FileOutputStream(tempZipFile.toFile())); ZipFile oldZip = new ZipFile(zipFilename)){
            // никак не могу перестать кайфовать от try с параметрами; просто объявляю необходимые мне файлы/потоки до начала try, и они закроются автоматически,
            // будет ли это вылет по Exception'у, или же отработает штатно.

            Enumeration<? extends ZipEntry> files = oldZip.entries(); // получил список файлов в виде странного перечисления; в описании сказано, что такая сигнатура нужна для сохранения совместимости в том случае, если я начну создавать авторские классы, дочерние по отношению к ZipEntry.
            while (files.hasMoreElements()) {   // пробежка по файлам в цикле
                ZipEntry file = files.nextElement();  // беру текущий файл...

                ZipEntry newOldFile = new ZipEntry(file.getName()); // создаю копию текущего файла, чтобы сберечь все метаданные
                newOldFile.setExtra(file.getExtra());
                newOldFile.setComment(file.getComment());
                newOldFile.setMethod(file.getMethod());
                newOldFile.setTime(file.getTime());

                if (file.getMethod() == ZipEntry.STORED) {  // если файлы сжаты этим методом, а я не перенесу следующие метаданные, то архив будет безнадежно испорчен
                    newOldFile.setCrc(file.getCrc());
                    newOldFile.setSize(file.getSize());
                    newOldFile.setCompressedSize(file.getCompressedSize());
                }

                zipOutputStream.putNextEntry(newOldFile); // теперь помещаю запись о нём в новый архивный файл, а заодно перенаправляю поток записи в этот файл
                if (!file.isDirectory()) {   // если текущая запись - не каталог, начать копирование описанным в курсе способом
                    try (InputStream fileStream = oldZip.getInputStream(file)){  // сначала создаётся поток для чтения файла из архива
                        byte[] buffer = new byte[1024];  // инициализация необходимых переменных
                        int length;
                        while ((length = fileStream.read(buffer)) > 0) {  // красивый, я считаю, ход: данные из потока считываются в буфер, и, пока есть, что считывать, длина считанной последовательности записывается в length
                            zipOutputStream.write(buffer, 0, length);  // а в новый файл записывается содержимое буфера
                        }  // как только в буфер перестали поступать данные...
                    }
                }
                zipOutputStream.closeEntry(); // закрывается поток записи, который шёл в newOldFile
            }

            // теперь важно не забыть дописать новые файлы
            for(String filename : filenames){  // для каждого файла в списке файлов на добавление в архив
                ZipEntry newFile = new ZipEntry(filename);  // создать запись с указанным именем файла
                zipOutputStream.putNextEntry(newFile);  // и добавить её в архив с привязкой потока к новому файлу
                Files.copy(Path.of(filename), zipOutputStream); // не до конца привык к пакету java.nio, но функционал удобный; выше по файлу попробовал олдскульный вариант, который я применял на работе ещё с Java_1.6, когда распаковывал архивы drweb в ЦБ, а здесь шикарный ход в одну строку
                zipOutputStream.closeEntry(); // закрыть поток записи в новый файл.
            }
        } catch (IOException e) {
            throw new RuntimeException(e);
        }

        // После того, как создал временный файл, я могу попробовать им заменить старый.
        try {
            Files.move(tempZipFile, Path.of(zipFilename), StandardCopyOption.REPLACE_EXISTING);
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }

    static void main(String[] args) {
        ZipUtils.addFilesToZip("to_delete.zip", new String[]{"ZipUtils.java", "FileUtils.java"});
    }
}
