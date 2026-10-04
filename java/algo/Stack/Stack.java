package Stack;

import java.util.*; // я решил, что эта строка - это подсказка: я буду использовать ArrayList для внутреннего хранилища

public class Stack<T> {
    ArrayList storage;

    public Stack() {
        this.storage = new ArrayList();
    }

    public int size() {
        // размер текущего стека
        return this.storage.size();
    }

    public T pop() {
        if (!this.storage.isEmpty())
            return (T) this.storage.removeLast();
        return null;  // если стек пустой
    }

    public void push(T val) {
        // ваш код
        this.storage.add(val);
    }

    public T peek() {
        // ваш код
        if (!this.storage.isEmpty())
            return (T) this.storage.getLast();
        return null; // если стек пустой
    }
}