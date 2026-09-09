import javax.imageio.ImageIO;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;
import java.nio.file.Paths;

public class GraphUtils {

    public static void convert(String inExtension, String outExtension) {
        File[] files = new File[]{};
        try {
            files = Paths.get("").toAbsolutePath().toFile().listFiles();
        } catch (NullPointerException npe) {
            System.out.println("Wrong current path! 0_o");
        }
        // Path currentDir = Paths.get("").toAbsolutePath();
        // for (File file : currentDir.toFile().listFiles()) {
        assert files != null;
        for (File file : files) {
            String filename = file.getName();
            if (!file.isDirectory() && filename.endsWith(inExtension)) {
                try {
                    BufferedImage image = ImageIO.read(file);
                    int dot = filename.lastIndexOf('.');
                    String name = filename.substring(0, dot);
                    ImageIO.write(image, outExtension, new File(name + "." + outExtension));
                } catch (IOException ioe) {
                    System.out.println("Error! Can't read or write to file.");
                }
            }
        }
    }

    static void main() {
        GraphUtils.convert("jpg", "png");
    }

}
