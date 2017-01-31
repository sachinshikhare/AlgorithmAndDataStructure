package algoandds.datastructures.linkedlist.generic;

public class SingleLinkedList<T> implements MyLinkedList<T> {

	private Node<T> head;
	private int listSize;
	
	SingleLinkedList() {
		head = new Node<T>(null);
		listSize = 0;
	}
	
	public void addAtStart(T data) {
		Node<T> node = new Node<T>(data);
		node.setNext(head.getNext());
		head.setNext(node);
		listSize++;
	}
	
	public void addAtIndex(T data, int index) {
		if(index > listSize + 1) {
			System.out.println("Not possible");
		} else {
			Node<T> node = new Node<T>(data);
			Node<T> current = head;
			int cntr = 0;
			while(current.getNext() != null && cntr++ != index-1){
				current = current.getNext();
			}
			node.setNext(current.getNext());
			current.setNext(node);
			listSize++;
		}
	}
	
	public void addAtEnd(T data) {
		Node<T> node = new Node<T>(data);
		Node<T> current = head;
		while(current.getNext() != null) {
			current = current.getNext();
		}
		current.setNext(node);
		listSize++;
	}
	
	public T removeFirst() {
		if(head.getNext() == null){
			return null;
		}
		Node<T> firstNode = head.getNext();
		head.setNext(firstNode.getNext());
		listSize--;
		return firstNode.getData();
	}
	
	public T removeLast() {
		if(head.getNext() == null){
			return null;
		}
		Node<T> current = head.getNext();
		Node<T> lastNode = null;
		while(current.getNext().getNext() != null) {
			current = current.getNext();
		}
		lastNode = current.getNext();
		current.setNext(null);
		listSize--;
		return lastNode.getData();
	}
	
	public T removeAtIndex(int index) {
		
		if(index > listSize) {
			System.out.println("Not possible");
			return null;
		}
		Node<T> current = head;
		int counter = 0;
		while(current.getNext() != null && counter++ != index-1){
			current = current.getNext();
		}
		Node<T> removedNode = current.getNext();
		current.setNext(removedNode.getNext());
		listSize--;
		return removedNode.getData();
	}
	
	public T getFirst() {
		return head.getNext() != null ? head.getNext().getData() : null;
	}
	
	public T getLast() {
		Node<T> current = head;
		T returnObj = null;
		if(current.getNext() != null) {
			while(current.getNext() != null) {
				current = current.getNext();
			}
			returnObj = current.getData();
		}
		return returnObj;
	}
	
	public T getAtIndex(int index) {
		if(listSize < index) {
			System.out.println("Not possible");
			return null;
		}
		Node<T> current = head;
		int counter = 0;
		while(counter++ != index){
			current = current.getNext();
		}
		return current.getData();
	}
	
	@Override
	public String toString() {
		
		String listData = null;
		Node<T> current = head.getNext();
		if(current != null) {
			listData = current.toString(); 
			while(current.getNext() != null) {
				current = current.getNext();
				listData += current.toString();
			}
		}
		return listData;
	}

	public boolean search(T data) {
		Node<T> current = head.getNext();
		boolean dataFound = false;
		if(current != null) {
			while(current.getNext() != null) {
				dataFound = data.equals(current.getData());
				if(dataFound) {
					break;
				}
				current = current.getNext();
			}
		}
		return dataFound;
	}
}
