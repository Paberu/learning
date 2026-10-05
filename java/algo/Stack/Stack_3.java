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

}
