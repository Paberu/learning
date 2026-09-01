package utils;

import java.io.IOException;
import java.util.logging.FileHandler;
import java.util.logging.Level;
import java.util.logging.Logger;
import java.util.logging.SimpleFormatter;

public class GameLogger {
    private static final Logger logger = Logger.getLogger("GameLogger");

    static {
        try {
            FileHandler fileHandler = new FileHandler("game.log", true);
            fileHandler.setLevel(Level.FINEST);
            fileHandler.setFormatter(new SimpleFormatter());
            logger.setLevel(Level.FINEST);
            logger.addHandler(fileHandler);
        } catch (IOException e) {
            System.err.println("Cannot create log-file:\n" + e.getMessage());
        }
    }

    public static void logChange(String className, String fieldName, Object oldValue, Object newValue) {
        logger.log(Level.FINEST, "[{0}] {1}: {2} -> {3}",
                new Object[]{className, fieldName, oldValue, newValue});
    }

    public static void logCreation(String className, Object object) {
        logger.log(Level.FINEST, "[{0}] Создан объект: {1}", new Object[]{className, object});
    }
}