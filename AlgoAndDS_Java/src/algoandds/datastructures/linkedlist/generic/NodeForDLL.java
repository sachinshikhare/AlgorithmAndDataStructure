package algoandds.datastructures.linkedlist.generic;

class NodeForDLL<T> {
	private T data;
	private NodeForDLL<T> next;
	private NodeForDLL<T> prev;
	NodeForDLL(T data) {
		this.data = data;
	}
	public T getData() {
		return data;
	}
	public void setData(T data) {
		this.data = data;
	}
	public NodeForDLL<T> getNext() {
		return next;
	}
	public void setNext(NodeForDLL<T> next) {
		this.next = next;
	}
	public NodeForDLL<T> getPrev() {
		return prev;
	}
	public void setPrev(NodeForDLL<T> prev) {
		this.prev = prev;
	}
	@Override
	public String toString() {
		return data.toString();
	}
}
