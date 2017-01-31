package algoandds.sorting;

public class InsertionSort implements Sortable{

    public void sortArray(int[] array) {
        for(int cntr1 = 1; cntr1 < array.length; cntr1++) {
            int key = array[cntr1];
            int cntr2 = cntr1;
            while(cntr2 > 0 && key < array[cntr2-1]) {
                array[cntr2] = array[cntr2-1];
                cntr2--;
            }
            array[cntr2] = key;
        }
    }

    /*public static void main(String[] args) {
        int[] array = {3,1,7,9,6,5,4,8,2};
        new InsertionSort().sortArray(array);
        for (int n : array) {
            System.out.println(n);
        }
    }*/

}