package Stack;

public class Stack_2 {
    public static boolean balanced(String s) {
        Stack checkerStack = new Stack<Character>();
        char[] symbolsToCheck = s.toCharArray();
        for (int i = 0; i < symbolsToCheck.length; i++) {
            char symbol = symbolsToCheck[i];
            if (symbol == '(') {
                checkerStack.push('(');
            } else if (symbol == ')') {
                if (checkerStack.peek() == null) {
                    return false;
                }
                char checkSymbol = (char)checkerStack.pop();
                if (checkSymbol != '(') {
                    return false;
                }
            }
        }
        return (checkerStack.size() == 0);
    }
}
