import javax.imageio.ImageIO;
import java.awt.*;
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
        assert files != null;
        for (File file : files) {
            String filename = file.getName();
            if (!file.isDirectory() && filename.endsWith(inExtension)) {
                try {
                    BufferedImage image = ImageIO.read(file);
                    Graphics2D g = image.createGraphics();
                    int squareSize = Math.min(image.getHeight(), image.getWidth()) / 2;
                    g.setColor(Color.BLACK);
                    g.drawRect((image.getWidth()-squareSize)/2, (image.getHeight()-squareSize)/2, squareSize, squareSize);
                    g.setFont(new Font(Font.MONOSPACED, Font.ITALIC, squareSize/4));
                    g.drawString("Hello,", (image.getWidth()-squareSize)/2+2, (image.getHeight()-squareSize)/2+g.getFont().getSize()+2);
                    g.drawString("World!", (image.getWidth()-squareSize)/2+2, (image.getHeight()-squareSize)/2+g.getFont().getSize()*2+4);
                    g.dispose();
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
