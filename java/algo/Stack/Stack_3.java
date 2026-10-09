package Stack;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;


public class Stack_3 {
    private Stack<Integer> stack1;
    private Stack<Integer> stack2;
    private Stack<Integer> stack3;
    private Stack<Integer> stack4;

    @BeforeEach
    public void setUp() {
        stack1 = new Stack<Integer>(); //empty
        stack2 = new Stack<Integer>();
        stack2.push(2);
        stack3 = new Stack<Integer>();
        for (int i = 0; i < 5; i++) {
            stack3.push(10);
        }
        stack4 = new Stack<Integer>();
        for (int i = 0; i < 10; i++) {
            stack4.push(i * 2);
        }
    }

    // Курс "Практика в программировании на АСД. Задание 1.
    // Подберите в вашем языке программирования подходящую динамическую структуру данных для хранения стека. Реализуйте методы size(), pop(), push() и peek().
    @Test
    public void testSize1() {
        assertEquals(0, stack1.size());
    }

    @Test
    public void testSize2() {
        assertEquals(1, stack2.size());
    }

    @Test
    public void testSize3() {
        assertEquals(5, stack3.size());
    }

    @Test
    public void testSize4() {
        assertEquals(10, stack4.size());
    }

    @Test
    public void testPop1() {
        assertNull(stack1.peek());
        assertEquals(0, stack1.size());
        assertNull(stack1.pop());
        assertEquals(0, stack1.size());
    }

    @Test
    public void testPop2() {
        assertEquals(2, stack2.peek());
        assertEquals(1, stack2.size());
        assertEquals(2, stack2.pop());
        assertEquals(0, stack2.size());
    }

    @Test
    public void testPop3() {
        assertEquals(10, stack3.peek());
        assertEquals(5, stack3.size());
        assertEquals(10, stack3.pop());
        assertEquals(4, stack3.size());
    }

    @Test
    public void testPop4() {
        assertEquals(18, stack4.peek());
        assertEquals(10, stack4.size());
        assertEquals(18, stack4.pop());
        assertEquals(16, stack4.peek());
        assertEquals(9, stack4.size());
    }

    @Test
    public void testPush1() {
        assertNull(stack1.peek());
        assertEquals(0, stack1.size());
        stack1.push(1);
        assertEquals(1, stack1.peek());
        assertEquals(1, stack1.size());
    }

    @Test
    public void testPush2() {
        assertEquals(2, stack2.peek());
        assertEquals(1, stack2.size());
        stack2.push(1);
        assertEquals(1, stack2.peek());
        assertEquals(2, stack2.size());
    }

    @Test
    public void testPush3() {
        assertEquals(10, stack3.peek());
        assertEquals(5, stack3.size());
        stack3.push(1);
        assertEquals(1, stack3.peek());
        assertEquals(6, stack3.size());
    }

    @Test
    public void testPush4() {
        assertEquals(18, stack4.peek());
        assertEquals(10, stack4.size());
        stack4.push(1);
        assertEquals(1, stack4.peek());
        assertEquals(11, stack4.size());
    }

    @Test
    public void testPeek1() {
        assertNull(stack1.peek());
    }

    @Test
    public void testPeek2() {
        assertEquals(2, stack2.peek());
    }

    @Test
    public void testPeek3() {
        assertEquals(10, stack3.peek());
    }

    @Test
    public void testPeek4() {
        assertEquals(18, stack4.peek());
    }

    // Задача 4. Напишите функцию, которая получает на вход строку, состоящую из открывающих и закрывающих скобок и, используя только
    // стек и оператор цикла, определите, сбалансированы ли скобки в этой строке.
    // Сложность по времени: O(n) - всегда надо пробежать весь стек.
    // Сложность по памяти: O(n) - для анализа строки длиной n создаётся стек длиной n.
    @Test
    public void testBalanced1() {
        String test = "(()((())()))";
        assertTrue(StackUtilities.balanced(test));
    }

    @Test
    public void testBalanced2() {
        String test =  "(()()(()";
        assertFalse(StackUtilities.balanced(test));
    }

    @Test
    public void testBalanced3() {
        String test = "(((((((((";
        assertFalse(StackUtilities.balanced(test));
    }

    @Test
    public void testBalanced4() {
        String test = ")))))))))";
        assertFalse(StackUtilities.balanced(test));
    }

    // Задача 5. Расширьте фукнцию из предыдущего примера, если скобки могут быть трех типов: (), {}, [].
    // Сложность по времени: O(n) - всегда надо пробежать весь стек.
    // Сложность по памяти: O(n) - для анализа строки длиной n создаётся стек длиной n.
    @Test
    public void testBalancedExtended1() {
        String test = "(({{}})((([[[]]]))()))";
        assertTrue(StackUtilities.balancedExtended(test));
    }

    @Test
    public void testBalancedExtended2() {
        String test =  "(()())[[(())";
        assertFalse(StackUtilities.balancedExtended(test));
    }

    @Test
    public void testBalancedExtended3() {
        String test = "({{{[[[(((((";
        assertFalse(StackUtilities.balancedExtended(test));
    }

    @Test
    public void testBalancedExtended4() {
        String test = ")))))))))";
        assertFalse(StackUtilities.balancedExtended(test));
    }

    // Задача 6. Добавьте в стек функцию, возвращающую текущий минимальный элемент в нём за O(1) (подсказка: используйте второй стек).
    // Сложность по времени: O(1) - берётся верхняя из стека минимумов.
    // Сложность по памяти: O(n) - создаётся дополнительный стек, равный по размеру предыдущему.
    @Test
    public void testMin1() {
        Stack_2<Integer> stack = new Stack_2<Integer>();
        assertThrows(ArithmeticException.class, () -> stack.min());
    }

    @Test
    public void testMin2() {
        Stack_2<Integer> stack = new Stack_2<Integer>();
        stack.push(2);
        assertEquals(2, stack.min());
    }

    @Test
    public void testMin3() {
        Stack_2<Integer>stack = new Stack_2<Integer>();
        for (int i = 0; i < 5; i++) {
            stack.push(10);
        }
        assertEquals(10, stack.min());
    }

    @Test
    public void testMin4() {
        Stack_2<Integer> stack = new Stack_2<Integer>();
        for (int i = 0; i < 10; i++) {
            stack.push(i * 2);
        }
        assertEquals(0, stack.min());
    }

    // Задача 7. Добавьте в стек функцию, которая возвращает среднее значение всех элементов в стеке. Она должна выполняться за O(1).
    // Сложность по времени: O(1) - переменная double делится на переменную int.
    // Сложность по памяти: O(1) - поддерживается две лишних переменных.
    @Test
    public void testAverage1() {
        Stack_2<Integer> stack = new Stack_2<Integer>();
        assertThrows(ArithmeticException.class, () -> stack.average());
    }

    @Test
    public void testAverage2() {
        Stack_2<Integer> stack = new Stack_2<Integer>();
        stack.push(2);
        assertEquals(2.0, stack.average());
    }

    @Test
    public void testAverage3() {
        Stack_2<Integer>stack = new Stack_2<Integer>();
        for (int i = 0; i < 5; i++) {
            stack.push(10);
        }
        assertEquals(10.0, stack.average());
    }

    @Test
    public void testAverage4() {
        Stack_2<Integer> stack = new Stack_2<Integer>();
        for (int i = 0; i < 10; i++) {
            stack.push(i * 2);
        }
        assertEquals(9.0, stack.average());
    }

    //Задача 8. Постфиксная запись выражения -- это запись, в которой порядок вычислений определяется не скобками и приоритетами, а только позицией элемента в выражении.
    // Рассчитайте с её помощью например такое выражение:
    @Test
    public void testFortranLike1() {
        String test = "8 2 + 5 * 9 + =";
        assertEquals(59, StackUtilities.fortranLike(test));
    }

    @Test
    public void testFortranLike2() {
        String test = "Молилась ли ты на ночь, Дездемона!?";
        assertThrows(IllegalArgumentException.class, () -> StackUtilities.fortranLike(test));
    }

    @Test
    public void testFortranLike3() {
        String test = "   5 5 + 5 * 50 + ";
        assertEquals(100, StackUtilities.fortranLike(test));
    }
}
