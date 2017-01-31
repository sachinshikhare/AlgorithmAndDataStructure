package algoandds.datastructures.linkedlist.generic;

public class DoubleLinkedList<T> implements MyLinkedList<T> {

	private NodeForDLL<T> head;
	private int listSize;
	
	DoubleLinkedList() {
		head = new NodeForDLL<T>(null);
		listSize = 0;
	}
	public void addAtStart(T data) {

		NodeForDLL<T> node = new NodeForDLL<T>(data);
		if(listSize == 0) {
			head.setNext(node);
			node.setPrev(head);
		} else {
			node.setNext(head.getNext());
			head.getNext().setPrev(node);
			head.setNext(node);
			node.setPrev(head);
		}
		listSize++;
	}

	public void addAtEnd(T data) {

		if(listSize == 0) {
			addAtStart(data);
		} else {
			NodeForDLL<T> node = new NodeForDLL<T>(data);
			NodeForDLL<T> current = head;
			while(current.getNext() != null){
				current = current.getNext();
			}
			current.setNext(node);
			node.setPrev(current);
			listSize++;
		}
	}

	public void addAtIndex(T data, int index) {

		if(listSize == 0 || index == 0) {
			addAtStart(data);
		} else if(index == listSize + 1) {
			addAtEnd(data);
		} else {
			NodeForDLL<T> node = new NodeForDLL<T>(data);
			NodeForDLL<T> current = head;
			int counter = 0;
			while(counter++ != index) {
				current = current.getNext();
			}
			node.setPrev(current.getPrev());
			current.getPrev().setNext(node);
			current.setPrev(node);
			node.setNext(current);
			listSize++;
		}
	}

	public T removeFirst() {
		
		T returnValue = null;
		if(listSize == 0) {
			System.out.println("Not possible");
		} else if(listSize == 1) {
			returnValue = head.getNext().getData();
			head.setNext(null);
			listSize--;
		} else {
			head.setNext(head.getNext().getNext());
			head.getNext().setPrev(head);
			listSize--;
		}
		return returnValue;
	}

	public T removeLast() {
		T returnValue = null;
		if(listSize == 0) {
			System.out.println("Not possible");
		} else {
			NodeForDLL<T> current = head;
			while(current.getNext() != null) {
				current = current.getNext();
			}
			returnValue = current.getData();
			current.getPrev().setNext(null);
			listSize--;
		}
		return returnValue;
	}

	public T removeAtIndex(int index) {

		T returnValue = null;
		if(listSize == 0 || index > listSize) {
			System.out.println("Not possible");
			return null;
		} else if(index == 0) {
			returnValue = removeFirst();
		} else if(index == listSize) {
			returnValue = removeLast();
		} else {
			int counter = 0;
			NodeForDLL<T> current = head;
			while(counter++ != index) {
				current = current.getNext();
			}
			current.getPrev().setNext(current.getNext());
			current.getNext().setPrev(current.getPrev());
			listSize--;
			returnValue = current.getData();
		}
		return returnValue;
	}

	public T getFirst() {

		if(listSize == 0) {
			System.out.println("Not possible");
			return null;
		} else {
			return head.getNext().getData();
		}
	}

	public T getLast() {

		if(listSize == 0) {
			System.out.println("Not possible");
			return null;
		} else {
			NodeForDLL<T> current = head;
			while(current.getNext() != null) {
				current = current.getNext();
			}
			return current.getData();
		}
	}

	public T getAtIndex(int index) {

		if(listSize == 0 || index > listSize) {
			System.out.println("Not possible");
			return null;
		} else if(index == 1) {
			return head.getNext().getData();
		} else {
			NodeForDLL<T> current = head;
			int counter = 0;
			while(counter++ != index) {
				current = current.getNext();
			}
			return current.getData();
		}
	}

	@Override
	public String toString() {
		
		String listData = null;
		NodeForDLL<T> current = head.getNext();
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
		NodeForDLL<T> current = head.getNext();
		boolean dataFound = false;
		T currNodeData = null;
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
