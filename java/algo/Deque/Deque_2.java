package Deque;

public class Deque_2 {
    public static boolean isPalindrom(String checkForPalindrom) {
        Deque<Character> deq = new Deque<Character>();
        for (char symbol : checkForPalindrom.toCharArray()) {
            deq.addTail(symbol);
        }
        while(deq.size() >= 1) {
            if ( !deq.removeFront().equals(deq.removeTail()) ) {
                return false;
            }
        }
        return true;
    }
}
