package Stack;

public class Stack_2 {
    public static boolean balanced(String s) {
        Stack<Character> checkerStack = new Stack<Character>();
        for (int i = 0; i < s.length(); i++) {
            char symbol = s.charAt(i);
            if (symbol == '(') {
                checkerStack.push('(');
            } else if (symbol == ')') {
                if (checkerStack.size() == 0) {
                    return false;
                }
                checkerStack.pop();
            }
        }
        return (checkerStack.size() == 0);
    }

    public static boolean balancedExtended(String s) {
        Stack<Character> checkerStack = new Stack<Character>();
        for (int i = 0; i < s.length(); i++) {
            char symbol = s.charAt(i);
            switch (symbol) {
                case '(', '[', '{' -> checkerStack.push(symbol);
                case ')', ']', '}' -> {
                    if (checkerStack.size() == 0) {
                        return false;
                    }
                    char checkSymbol = checkerStack.pop();
                    if ( (checkSymbol == '(' && symbol != ')') ||
                            (checkSymbol == '[' && symbol != ']') ||
                            (checkSymbol == '{' && symbol != '}') )
                        return false;
                }
            }
        }
        return (checkerStack.size() == 0);
    }
}
