package algoandds.datastructures.linkedlist.generic;

public interface MyLinkedList<T> /*extends Iterable<T>*/{

	public void addAtStart(T data);
	public void addAtEnd(T data);
	public void addAtIndex(T data, int index);
	public T removeFirst();
	public T removeLast();
	public T removeAtIndex(int index);
	public T getFirst();
	public T getLast();
	public T getAtIndex(int index);
	public boolean search(T data);
	
//	public int size();
//	public boolean isEmpty();
//	public T getNextData();
}
