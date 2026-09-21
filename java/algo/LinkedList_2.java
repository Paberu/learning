class LinkedListUtils {
    public static LinkedList sumUp(LinkedList firstList, LinkedList secondList) {
        if (firstList.count() != secondList.count()) {
            return new LinkedList();
        }
        LinkedList sumList = new LinkedList();
        Node node1 = firstList.head;
        Node node2 = secondList.head;
        while (node1 != null) {
            sumList.addInTail(new Node(node1.value+node2.value));
            node1 = node1.next;
            node2 = node2.next;
        }
        return sumList;
    }
}