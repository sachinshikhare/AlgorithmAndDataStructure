package algoandds.datastructures.queue;

public interface Queue {

	public boolean isFull();
	public boolean isEmpty();
	public int size();
	public void enqueue(int value);
	public int dequeue();
	public int peek();
}

