package algoandds.datastructures.linkedlist;

class NodeForDLL {
	private String data;
	private NodeForDLL next;
	private NodeForDLL prev;
	NodeForDLL(String data) {
		this.data = data;
	}
	public String getData() {
		return data;
	}
	public void setData(String data) {
		this.data = data;
	}
	public NodeForDLL getNext() {
		return next;
	}
	public void setNext(NodeForDLL next) {
		this.next = next;
	}
	public NodeForDLL getPrev() {
		return prev;
	}
	public void setPrev(NodeForDLL prev) {
		this.prev = prev;
	}
}
