package algoandds.sorting;

public class QuickSort implements Sortable{

	public void sortArray(int[] array) {

		quickSort(array, 0, array.length-1);
	}

	private void quickSort(int[] array, int low, int high) {

		if(low < high) {
			int q = partition(array, low, high);
			quickSort(array, low, q-1);
			quickSort(array, q+1, high);
		}
	}

	private int partition(int[] array, int low, int high) {
		
		int pivot = array[high];
		int i = low-1;
		for(int j = low; j <= high-1; j++) {
			if(pivot > array[j]) {
				i++;
				swap(array, i, j);
			}
		}
		swap(array, i+1, high);
		return i+1;
	}

	private void swap(int[] array, int i, int j) {

		int temp = array[i];
		array[i] = array[j];
		array[j] = temp;
	}

	 /*public static void main(String[] args) {
	    int[] array = {3,1,7,9,6,5,4,8,2};
	    new QuickSort().sortArray(array);
	    for (int n : array) {
	        System.out.println(n);
	    }
	}*/
}
