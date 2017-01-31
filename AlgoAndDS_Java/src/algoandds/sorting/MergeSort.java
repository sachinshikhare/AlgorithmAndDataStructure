package algoandds.sorting;

/**
 * Created by Sachin Shikhare on 13-11-2016.
 */

/**
 * BASIC RULES: startIndex <= mid < EndIndex
 *
 */
public class MergeSort implements Sortable{

    public void sortArray(int[] array) {
        mergeSort(array, 0, array.length-1);
    }

    private static void mergeSort(int[] array, int startIndex, int endIndex) {
        int mid = 0;
        if(startIndex < endIndex) {
            mid = (startIndex+endIndex)/2;
            mergeSort(array, startIndex, mid);
            mergeSort(array, mid + 1, endIndex);
            merge(array, startIndex, mid, endIndex);
        }
    }

    private static void merge(int[] array, int startIndex, int mid, int endIndex) {

        int len1 = mid - startIndex + 1;
        int len2 = endIndex - mid;
        int[] left = new int[len1];
        int[] right = new int[len2];

        for(int cntr = 0; cntr < len1; cntr++) {
            left[cntr] = array[startIndex + cntr];
        }
        for (int cntr = 0; cntr < len2; cntr++) {
            right[cntr] = array[mid + cntr + 1];
        }

        int rightCounter = 0;
        int leftCounter = 0;
        int mainArrCounter = startIndex;

        while(leftCounter < len1 && rightCounter < len2) {
            if(left[leftCounter] < right[rightCounter]) {
                array[mainArrCounter] = left[leftCounter];
                leftCounter++;
            } else {
                array[mainArrCounter] = right[rightCounter];
                rightCounter++;
            }
            mainArrCounter++;
        }

        while(leftCounter < len1) {
            array[mainArrCounter++] = left[leftCounter++];
        }
        while(rightCounter < len2) {
            array[mainArrCounter++] = right[rightCounter++];
        }
    }

//    public static void main(String[] args) {
//        int[] array = {3,1,7,9,6,5,4,8,2};
//        new MergeSort().sortArray(array);
//        for (int n : array) {
//            System.out.println(n);
//        }
//    }
}
