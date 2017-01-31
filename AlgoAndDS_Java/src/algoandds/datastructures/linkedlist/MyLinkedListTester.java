package algoandds.datastructures.linkedlist;

public class MyLinkedListTester {

	public static void main(String[] args) {
		
		MyLinkedList linkedList = null;
		
//		System.out.println("Testing Single Linked List...");
//		linkedList = new SingleLinkedList();
		
		System.out.println("Testing Double Linked List...");
		linkedList = new DoubleLinkedList();

		System.out.println("Adding at start... ");
		linkedList.addAtStart("A");
		System.out.println(linkedList);
		System.out.println("Adding at start... ");
		linkedList.addAtStart("B");
		System.out.println(linkedList);
		System.out.println("Adding at start... ");
		linkedList.addAtStart("C");
		System.out.println(linkedList);
		System.out.println("Adding at start... ");
		linkedList.addAtStart("D");
		System.out.println(linkedList);
		System.out.println("Adding at start... ");
		linkedList.addAtStart("E");
		System.out.println(linkedList);
		System.out.println("Adding at start... ");
		linkedList.addAtStart("F");
		System.out.println(linkedList);
		System.out.println("Add at End...");
		linkedList.addAtEnd("AA");
		System.out.println(linkedList);
		System.out.println("Add at End...");
		linkedList.addAtEnd("BB");
		System.out.println(linkedList);
		System.out.println("Add at End...");
		linkedList.addAtEnd("CC");
		System.out.println(linkedList);
		System.out.println("Add at End...");
		linkedList.addAtEnd("DD");
		System.out.println(linkedList);
		System.out.println("Add at Index...");
		linkedList.addAtIndex("AAA", 3);
		System.out.println(linkedList);
		System.out.println("Add at Index...");
		linkedList.addAtIndex("BBB", 5);
		System.out.println(linkedList);
		System.out.println("Add at Index...");
		linkedList.addAtIndex("CCC", 2);
		System.out.println(linkedList);
		System.out.println("Add at Index...");
		linkedList.addAtIndex("DDD", 7);
		System.out.println(linkedList);
		System.out.println("Add at Index...");
		linkedList.addAtIndex("EEE", 5);
		System.out.println(linkedList);
		System.out.println("Get First: " + linkedList.getFirst());
		System.out.println("Get Last: " + linkedList.getLast());
		System.out.println("Get At Index: " + linkedList.getAtIndex(5));
		System.out.println("Get At Index: " + linkedList.getAtIndex(2));
		System.out.println("Get At Index: " + linkedList.getAtIndex(55));
		System.out.println("Removing First element: " + linkedList.removeFirst());
		System.out.println("Removing First element: " + linkedList.removeFirst());
		System.out.println("Removing First element: " + linkedList.removeFirst());
		System.out.println(linkedList);
		System.out.println("Removing Last element: " + linkedList.removeLast());
		System.out.println("Removing Last element: " + linkedList.removeLast());
		System.out.println("Removing Last element: " + linkedList.removeLast());
		System.out.println(linkedList);
		System.out.println("Removing element at index: " + linkedList.removeAtIndex(4));
		System.out.println("Removing element at index: " + linkedList.removeAtIndex(8));
		System.out.println("Removing element at index: " + linkedList.removeAtIndex(44));
		System.out.println(linkedList);
	}

}
