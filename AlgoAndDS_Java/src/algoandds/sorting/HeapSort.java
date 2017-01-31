package algoandds.sorting;

public class HeapSort implements Sortable{
	
	int heapSize = 0;
	
	private void maxHeapify(int[] array, int index) {
		int leftChildIndex = index * 2;
		int rightChildIndex = index * 2 + 1;
		int largestValueNodeIndex = index;
		if(leftChildIndex < heapSize && array[leftChildIndex] > array[index]) {
			largestValueNodeIndex = leftChildIndex;
		}
		if(rightChildIndex < heapSize && array[rightChildIndex] > array[largestValueNodeIndex]) {
			largestValueNodeIndex = rightChildIndex;
		}
		if(largestValueNodeIndex != index) {
			swap(array, index, largestValueNodeIndex);
			maxHeapify(array, largestValueNodeIndex);
		}
	}
	
	private void buildMaxHeap(int[] array) {
		this.heapSize = array.length;
		for(int cntr = array.length/2; cntr >= 0; cntr--) {
			maxHeapify(array, cntr);
		}
	}

	private void swap(int[] array, int index, int largestValueNodeIndex) {
		int temp = array[index];
		array[index] = array[largestValueNodeIndex];
		array[largestValueNodeIndex] = temp;
	}

	 /*public static void main(String[] args) {
	    int[] array = {3,1,7,9,6,5,4,8,2};
	    new HeapSort().sortArray(array);
	    for (int n : array) {
	        System.out.println(n);
	    }
	}*/

	public void sortArray(int[] array) {
		buildMaxHeap(array);
		for(int cntr = array.length-1; cntr > 0; cntr--) {
			swap(array, 0, cntr); 
			heapSize -= 1;
			maxHeapify(array, 0);
		}
	}
}
