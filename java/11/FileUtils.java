import java.io.File;
import java.util.ArrayList;
import java.util.Arrays;

public class FileUtils {

    public static void viewAllSubdirs(){
        // На курсе по АТД было два варианта прохождения по дереву: в глубину и в ширину. Здесь как будто бы
        // представлен вариант обхода в ширину.
        File root = new File(".");  // создаёт объект File, которому соответствует текущий каталог
        ArrayList<File> expand = new ArrayList<File>(); // создаёт список для хранения всех вложенных каталогов одного (текущего) уровня
        expand.add(root); // добавляет корневой каталог (т.е. текущий в список всех каталогов)

        for(int depth = 0; depth < 10; depth++) {  // цикл работает на глубину вложения до 10 подкаталогов
            File[] expandCopy = expand.toArray(new File[expand.size()]); // на текущем уровне создаётся массив с копией списка файлов, которые требуется обойти и проверить
            expand.clear(); // исходный список очищается, чтобы в него поместить файлы и папки следующего уровня вложенности
            for (File file : expandCopy) {  // в результате каждый файл, который попал в этот список
                System.out.println(depth + " " + file); // выводится на экран с указанием того уровня вложенности, на котором он находится.
                if (file.isDirectory()) {
                    expand.addAll(Arrays.asList(file.listFiles()));  // а если текущий файл - это каталог, то список всех файлов, которые находятся в нём
                    // добавляется в очищенный в начале итерации список expand. Добавлять элементы массива в список напрямую нельзя, т.к. массив - это
                    // примитивный тип, а не класс, реализующий интерфейс Collection. Следовательно, надо либо создавать временный обезличенный объект
                    // типа List, по которому метод addAll() сам пробежится, либо использовать Collections.addAll(), который пробежится по массиву без
                    // создания лишних объектов, либо писать вложенный for. Как говорится, можно, а зачем? )))
                }
            }
        }
    }

    public static ArrayList<ArrayList<String>> searchThroughDirectory(String path, String extension, boolean through) {
        File root = new File(path);
        ArrayList<String> files = new ArrayList<>();
        ArrayList<String> dirs = new ArrayList<>();
        ArrayList<File> inner_dirs = new ArrayList<>();

        File[] children = root.listFiles();
        if (children != null) {
            for (File file : children) {

                if (file.isDirectory()) {
                    dirs.add(file.getName());
                    inner_dirs.add(file);
                }

                if (file.isFile() && file.getName().endsWith(extension)) {
                    files.add(file.getName());
                }
            }
            if (through) {
                for (File dir : inner_dirs) {
                    File[] inner_children = dir.listFiles();
                    if (inner_children != null) {
                        for (File inner_file : inner_children) {
                            if (inner_file.isDirectory()) {
                                dirs.add(inner_file.getName());
                            }

                            if (inner_file.isFile() && inner_file.getName().endsWith(extension)) {
                                files.add(inner_file.getName());
                            }
                        }
                    }
                }
            }
        }
        ArrayList<ArrayList<String>> result = new ArrayList<>();
        result.add(files);
        result.add(dirs);
        return result;
    }

    public static boolean toDeleteDirectory(String path){
        File[] files = new File(path).listFiles();
        for (File file : files) {
            if (file.isDirectory()) {
                return false;
            }
        }
        for (File file : files) {
            file.delete();
        }
        return new File(path).delete();
    }

    public void main(String[] args){
        ArrayList<ArrayList<String>> result = searchThroughDirectory("C:\\Users\\paberu\\Documents\\GitHub\\TorrentGetter", "torrent", false);
        ArrayList<ArrayList<String>> result2 = searchThroughDirectory("C:\\Users\\paberu\\Documents\\GitHub\\TorrentGetter", "torrent", true);
        System.out.println(result);
        System.out.println(result2);
        System.out.println(toDeleteDirectory("to_delete"));
        viewAllSubdirs();
    }
}