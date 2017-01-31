package algoandds.datastructures.queue;

public class CircularArrayQueue implements Queue{
	
	private int capacity;
	private int[] queueArray;
	private int front;
	private int rear; 
	private int elementsInQueue;
	public CircularArrayQueue(int capacity) {

		this.capacity = capacity;
		queueArray = new int[capacity];
		elementsInQueue = 0; 
		front = 0;
		rear = 0;
	}

	public boolean isFull() {
		
//		int diff = rear - front;
//		if(diff == -1 || diff == (this.capacity))
//			return true;
//		return false;
		return elementsInQueue == queueArray.length-1;
	}

	public boolean isEmpty() {

		return elementsInQueue == 0;
	}

	public int size() {
		return elementsInQueue;
//		if(rear > front) {
//			return rear - front;
//		} else {
//			return this.capacity - front + rear;
//		}
	}

	public void enqueue(int value) {

		if(this.isFull()){
			System.out.println("Queue is already full, ");
		} else {
			queueArray[rear] = value;
			rear = (rear + 1) % capacity;
			elementsInQueue++;
		}
	}

	public int dequeue() {
		int removedValue = -1;
		if(isEmpty()) {
			System.out.println("Queue is empty, ");
		} else {
			removedValue = queueArray[front];
			front = (front + 1) % capacity;
			elementsInQueue--;
		}
		return removedValue;
	}
	
	public int peek() {
		return queueArray[front];
	}

}

class QueueTester {
	
	public static void main(String[] args) {
		Queue queue = new CircularArrayQueue(5);
		System.out.println("Size: " + queue.size());
		System.out.println("Is Empty: " + queue.isEmpty());
		System.out.println("Is Full: " + queue.isFull());
		System.out.println("Adding element");
		queue.enqueue(1);
		System.out.println("Adding element");
		queue.enqueue(2);
		System.out.println("Adding element");
		queue.enqueue(3);
		System.out.println("Adding element");
		System.out.println("Peek:" + queue.peek());
		queue.enqueue(4);
		System.out.println("Size: " + queue.size());
		System.out.println("Is Empty: " + queue.isEmpty());
		System.out.println("Is Full: " + queue.isFull());
		System.out.println("Removed element: " + queue.dequeue());
		System.out.println("Size: " + queue.size());
		System.out.println("Peek:" + queue.peek());
		System.out.println("Adding element");
		queue.enqueue(10);
		System.out.println("Adding element");
		queue.enqueue(20);
		System.out.println("Adding element");
		queue.enqueue(30);
		System.out.println("Size: " + queue.size());
		System.out.println("Is Empty: " + queue.isEmpty());
		System.out.println("Is Full: " + queue.isFull());
		System.out.println("Removed element: " + queue.dequeue());
		System.out.println("Removed element: " + queue.dequeue());
		System.out.println("Removed element: " + queue.dequeue());
		System.out.println("Removed element: " + queue.dequeue());
		System.out.println("Removed element: " + queue.dequeue());
		System.out.println("Size: " + queue.size());
		System.out.println("Is Empty: " + queue.isEmpty());
		System.out.println("Is Full: " + queue.isFull());
		System.out.println("Adding element");
		queue.enqueue(100);
		System.out.println("Adding element");
		queue.enqueue(200);
		System.out.println("Adding element");
		queue.enqueue(300);
		System.out.println("Size: " + queue.size());
		System.out.println("Is Empty: " + queue.isEmpty());
		System.out.println("Is Full: " + queue.isFull());
		System.out.println("Peek:" + queue.peek());
	}
}