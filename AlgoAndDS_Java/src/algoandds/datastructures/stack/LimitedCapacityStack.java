package algoandds.datastructures.stack;

public class LimitedCapacityStack {

	private static int capacity;
	private int[] stackArray;
	private static int top = -1;
	
	public LimitedCapacityStack(int capacity) {
		this.capacity = capacity;
		stackArray = new int[this.capacity];
		System.out.println("Stack Capacity... " + this.capacity);
	}
	
	public boolean isFull() {
		boolean result = false;
		if(top == capacity - 1){
			result = true;
		}
		return result;
	}
	
	public boolean isEmpty() {
		boolean result = false;
		if(top == -1) {
			result = true;
		}
		return result;
	}
	
	public boolean push(int value) {
		boolean result = true;
		if(isFull()) {
			System.out.println("Stack is full");
			result = false;
		} else {
			stackArray[++top] = value;	
		}
		return result;
	}
	
	public int pop() {
		int result = -1;
		if(isEmpty()) {
			System.out.println("Stack is empty");
		} else { 
			result = stackArray[top--];	
		}
		return result;
	}
	
	public int getTop() {
		int result = -1;
		if(isEmpty()) {
			System.out.println("Stack is empty");
		}
		result = stackArray[top];
		return result;
	}
	
	public void printStack() {
		for (int value : stackArray) {
			System.out.print(value + ", ");
		}
	}
}

class StackTester {
	public static void main(String[] args) {
		LimitedCapacityStack stack = new LimitedCapacityStack(5);
		
		System.out.println("Is Empty: " + stack.isEmpty());
		System.out.println("Is Full: " + stack.isFull());
		
		System.out.println("Element added: " + stack.push(10));
		System.out.println("Element added: " + stack.push(20));
		System.out.println("Element added: " + stack.push(30));
		System.out.println("Is Empty: " + stack.isEmpty());
		System.out.println("Is Full: " + stack.isFull());
		stack.printStack();
		System.out.println(stack.pop());		
		System.out.println("Element added: " + stack.push(300));
		System.out.println("Element added: " + stack.push(400));
		System.out.println("Element added: " + stack.push(500));
		stack.printStack();
		System.out.println("Is Empty: " + stack.isEmpty());
		System.out.println("Is Full: " + stack.isFull());
		System.out.println("Element added: " + stack.push(6000));
		System.out.println(stack.pop());		
		System.out.println(stack.pop());		
		System.out.println(stack.pop());		
		System.out.println(stack.pop());		
		System.out.println(stack.pop());		
		System.out.println(stack.pop());		
		System.out.println(stack.pop());		
		System.out.println("Is Empty: " + stack.isEmpty());
		System.out.println("Is Full: " + stack.isFull());
	}
}