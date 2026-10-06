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

    //Задача 6. Добавьте в стек функцию, возвращающую текущий минимальный элемент в нём за O(1) (подсказка: используйте второй стек).
    // Я помню, что задачи со звёздочкой мы выносим в файл с постфиксом _2. Но в таком случае мы получим сложно O(n) и изуродуем исходный стек.
    // Я выношу эту функцию в Stack.java. Здесь оставлю этот говнокод как пример того, как нельзя писать.
    public static int minInStack(Stack<Integer> stack) {
        if (stack.size() == 0) throw new IllegalArgumentException("Этой функции нельзя скармливать пустой стек");
        Stack<Integer> stackForCheck = new Stack<Integer>();
        stackForCheck.push(stack.pop()); // инициализация, как она есть (мне не нравится, что в процессе поиска наименьшего значения я корёжу исходный стек, это надо менять)
        int iterations = stack.size();
        for (int i = 0; i < iterations; i++) {
            int element = stack.pop();
            if (element < stackForCheck.peek()) {
                stackForCheck.push(element);
            }
        }
        return stackForCheck.peek();
    }
}
