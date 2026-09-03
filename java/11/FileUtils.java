public class FileUtils {

    public static void viewAllSubdirs(){
        File root = new File(".");  // создаёт объект File, которому соответствует текущий каталог
        ArrayList<File> expand = new ArrayList<File>(); // создаёт список для хранения всех вложенных каталогов
        expand.add(root); // добавляет корневой каталог (т.е. текущий в список всех каталогов)

        for(int depth = 0; depth < 10; depth++) {
        // цикл работает на глубину вложения до 10 подкаталогов
            File[] expandCopy = expand.toArray(new File[expand.size()]); // на каждом уровне вложенности идёт сброс имеющегося списка в массив
            expand.clear(); // а исходный список очищается
            for (File file : expandCopy) {
                System.out.println(depth + " " + file);
                if (file.isDirectory()) {
                    expand.addAll(Arrays.asList(file.listFiles()));
                }
            }
        }
    }
}