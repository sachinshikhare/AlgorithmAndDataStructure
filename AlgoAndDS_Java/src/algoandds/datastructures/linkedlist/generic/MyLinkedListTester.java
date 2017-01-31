package algoandds.datastructures.linkedlist.generic;

import algoandds.beans.Employee;

public class MyLinkedListTester {

	public static void main(String[] args) {
		
		MyLinkedList<Employee> linkedList = null;
		
		System.out.println("Testing Single Linked List...");
		linkedList = new SingleLinkedList<Employee>();
		
//		System.out.println("Testing Double Linked List...");
//		linkedList = new DoubleLinkedList<Employee>();

		System.out.println("Adding at start... ");
		linkedList.addAtStart(getEmplyee(1, "A"));
		System.out.println(linkedList);
		System.out.println("Adding at start... ");
		linkedList.addAtStart(getEmplyee(2, "B"));
		System.out.println(linkedList);
		System.out.println("Adding at start... ");
		linkedList.addAtStart(getEmplyee(3, "C"));
		System.out.println(linkedList);
		System.out.println("Adding at start... ");
		linkedList.addAtStart(getEmplyee(4, "D"));
		System.out.println(linkedList);
		System.out.println("Adding at start... ");
		linkedList.addAtStart(getEmplyee(5, "E"));
		System.out.println(linkedList);
		System.out.println("Adding at start... ");
		linkedList.addAtStart(getEmplyee(6, "F"));
		System.out.println(linkedList);
		System.out.println("Add at End...");
		linkedList.addAtEnd(getEmplyee(7, "AA"));
		System.out.println(linkedList);
		System.out.println("Add at End...");
		linkedList.addAtEnd(getEmplyee(8, "BB"));
		System.out.println(linkedList);
		System.out.println("Add at End...");
		linkedList.addAtEnd(getEmplyee(9, "CC"));
		System.out.println(linkedList);
		System.out.println("Add at End...");
		linkedList.addAtEnd(getEmplyee(10, "DD"));
		System.out.println(linkedList);
		System.out.println("Add at Index...");
		linkedList.addAtIndex(getEmplyee(11, "AAA"), 3);
		System.out.println(linkedList);
		System.out.println("Add at Index...");
		linkedList.addAtIndex(getEmplyee(12, "BBB"), 5);
		System.out.println(linkedList);
		System.out.println("Add at Index...");
		linkedList.addAtIndex(getEmplyee(13, "CCC"), 2);
		System.out.println(linkedList);
		System.out.println("Add at Index...");
		linkedList.addAtIndex(getEmplyee(14, "DDD"), 7);
		System.out.println(linkedList);
		System.out.println("Add at Index...");
		linkedList.addAtIndex(getEmplyee(15, "EEE"), 5);
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
		System.out.println("Seach employee by id: " + linkedList.search(new Employee(1))); // TODO : check for this line... this line not working properly
		System.out.println("Seach employee by id: " + linkedList.search(new Employee(3)));
		System.out.println("Seach employee by id: " + linkedList.search(new Employee(5)));
	}

	private static Employee getEmplyee(int empId, String empDetl) {
		return new Employee(empId, empDetl,empDetl);
	}

}
