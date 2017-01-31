package algoandds.datastructures.linkedlist;

public class SingleLinkedList implements MyLinkedList {

	private Node head;
	private int listSize;
	
	SingleLinkedList() {
		head = new Node(null);
		listSize = 0;
	}
	
	public void addAtStart(String data) {
		Node node = new Node(data);
		node.setNext(head.getNext());
		head.setNext(node);
		listSize++;
	}
	
	public void addAtIndex(String data, int index) {
		if(index > listSize + 1) {
			System.out.println("Not possible");
		} else {
			Node node = new Node(data);
			Node current = head;
			int cntr = 0;
			while(current.getNext() != null && cntr++ != index-1){
				current = current.getNext();
			}
			node.setNext(current.getNext());
			current.setNext(node);
			listSize++;
		}
	}
	
	public void addAtEnd(String data) {
		Node node = new Node(data);
		Node current = head;
		while(current.getNext() != null) {
			current = current.getNext();
		}
		current.setNext(node);
		listSize++;
	}
	
	public String removeFirst() {
		if(head.getNext() == null){
			return null;
		}
		Node firstNode = head.getNext();
		head.setNext(firstNode.getNext());
		listSize--;
		return firstNode.getData();
	}
	
	public String removeLast() {
		if(head.getNext() == null){
			return null;
		}
		Node current = head.getNext();
		Node lastNode = null;
		while(current.getNext().getNext() != null) {
			current = current.getNext();
		}
		lastNode = current.getNext();
		current.setNext(null);
		listSize--;
		return lastNode.getData();
	}
	
	public String removeAtIndex(int index) {
		
		if(index > listSize) {
			System.out.println("Not possible");
			return null;
		}
		Node current = head;
		int counter = 0;
		while(current.getNext() != null && counter++ != index-1){
			current = current.getNext();
		}
		Node removedNode = current.getNext();
		current.setNext(removedNode.getNext());
		listSize--;
		return removedNode.getData();
	}
	
	public String getFirst() {
		return head.getNext() != null ? head.getNext().getData() : null;
	}
	
	public String getLast() {
		Node current = head;
		String returnString = null;
		if(current.getNext() != null) {
			while(current.getNext() != null) {
				current = current.getNext();
			}
			returnString = current.getData();
		}
		return returnString;
	}
	
	public String getAtIndex(int index) {
		if(listSize < index) {
			System.out.println("Not possible");
			return null;
		}
		Node current = head;
		int counter = 0;
		while(counter++ != index){
			current = current.getNext();
		}
		return current.getData();
	}
	
	@Override
	public String toString() {
		
		String listData = "";
		Node current = head.getNext();
		if(current != null) {
			listData = current.getData(); 
			while(current.getNext() != null) {
				current = current.getNext();
				listData += ", " + current.getData();
			}
		}
		return listData;
	}

	public boolean search(String data) {
		Node current = head.getNext();
		boolean dataFound = false;
		String currNodeData = null;
		if(current != null) {
			while(current.getNext() != null) {
				currNodeData = current.getData();
				dataFound = current.getData() == currNodeData;
				if(dataFound) {
					break;
				}
				current = current.getNext();
				
			}
		}
		return dataFound;
	}
}
