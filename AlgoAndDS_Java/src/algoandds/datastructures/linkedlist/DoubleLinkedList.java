package algoandds.datastructures.linkedlist;

public class DoubleLinkedList implements MyLinkedList {

	private NodeForDLL head;
	private int listSize;
	
	DoubleLinkedList() {
		head = new NodeForDLL(null);
		listSize = 0;
	}
	public void addAtStart(String data) {

		NodeForDLL node = new NodeForDLL(data);
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

	public void addAtEnd(String data) {

		if(listSize == 0) {
			addAtStart(data);
		} else {
			NodeForDLL node = new NodeForDLL(data);
			NodeForDLL current = head;
			while(current.getNext() != null){
				current = current.getNext();
			}
			current.setNext(node);
			node.setPrev(current);
			listSize++;
		}
	}

	public void addAtIndex(String data, int index) {

		if(listSize == 0 || index == 0) {
			addAtStart(data);
		} else if(index == listSize + 1) {
			addAtEnd(data);
		} else {
			NodeForDLL node = new NodeForDLL(data);
			NodeForDLL current = head;
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

	public String removeFirst() {
		
		String returnValue = null;
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

	public String removeLast() {
		String returnValue = null;
		if(listSize == 0) {
			System.out.println("Not possible");
		} else {
			NodeForDLL current = head;
			while(current.getNext() != null) {
				current = current.getNext();
			}
			returnValue = current.getData();
			current.getPrev().setNext(null);
			listSize--;
		}
		return returnValue;
	}

	public String removeAtIndex(int index) {

		String returnValue = null;
		if(listSize == 0 || index > listSize) {
			System.out.println("Not possible");
			return null;
		} else if(index == 0) {
			returnValue = removeFirst();
		} else if(index == listSize) {
			returnValue = removeLast();
		} else {
			int counter = 0;
			NodeForDLL current = head;
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

	public String getFirst() {

		if(listSize == 0) {
			System.out.println("Not possible");
			return null;
		} else {
			return head.getNext().getData();
		}
	}

	public String getLast() {

		if(listSize == 0) {
			System.out.println("Not possible");
			return null;
		} else {
			NodeForDLL current = head;
			while(current.getNext() != null) {
				current = current.getNext();
			}
			return current.getData();
		}
	}

	public String getAtIndex(int index) {

		if(listSize == 0 || index > listSize) {
			System.out.println("Not possible");
			return null;
		} else if(index == 1) {
			return head.getNext().getData();
		} else {
			NodeForDLL current = head;
			int counter = 0;
			while(counter++ != index) {
				current = current.getNext();
			}
			return current.getData();
		}
	}

	@Override
	public String toString() {
		
		String listData = "";
		NodeForDLL current = head.getNext();
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
		NodeForDLL current = head.getNext();
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
