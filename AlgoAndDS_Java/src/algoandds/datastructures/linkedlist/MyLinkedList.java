package algoandds.datastructures.linkedlist;

public interface MyLinkedList {

	public void addAtStart(String data);
	public void addAtEnd(String data);
	public void addAtIndex(String data, int index);
	public String removeFirst();
	public String removeLast();
	public String removeAtIndex(int index);
	public String getFirst();
	public String getLast();
	public String getAtIndex(int index);
	public boolean search(String data);
}
