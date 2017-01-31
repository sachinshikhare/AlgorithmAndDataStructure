package algoandds.sorting;

import java.util.Calendar;
import java.util.Random;

/**
 * Created by Sachin Shikhare on 13-11-2016.
 */
public class TestData {
    private static final int MAX_SIZE = 1000;

    private static final int MAX_RANDOM_LIMIT = 1000000;

    private static final boolean ENABLE_DATA_DISPLAY = false;

    public static void main(String[] args) {

        System.out.println("==========================================COMPARISON==================================================");
        System.out.println("Please wait...");
        System.out.println("Total Time Insertion Sort -----------------------> " + testInsertionSort() + " ms");
        System.out.println("Total Time Merge Sort -----------------------> " + testMergeSort() + " ms");
        System.out.println("Total Time Heap Sort -----------------------> " + testHeapSort() + " ms");
        System.out.println("Total Time Quick Sort -----------------------> " + testQuickSort() + " ms");
        System.out.println("======================================================================================================");
    }

    private static long testQuickSort() {
        Sortable sortable = new QuickSort(); // QUICK SORT
        int[] array = createTestData();
        long sortStartedAt = Calendar.getInstance().getTimeInMillis();
        sortable.sortArray(array);
        long totalTimeQuickSort = Calendar.getInstance().getTimeInMillis() - sortStartedAt;
        afterSorting(array, totalTimeQuickSort);
        return totalTimeQuickSort;
	}

	private static long testInsertionSort() {
        Sortable sortable = new InsertionSort(); // INSERTION SORT
        int[] array = createTestData();
        long sortStartedAt = Calendar.getInstance().getTimeInMillis();
        sortable.sortArray(array);
        long totalTimeInsertSort = Calendar.getInstance().getTimeInMillis() - sortStartedAt;
        afterSorting(array, totalTimeInsertSort);
        return totalTimeInsertSort;
    }

    private static long testMergeSort() {
        Sortable sortable = new MergeSort(); // MERGE SORT
        int[] array = createTestData();
        long sortStartedAt = Calendar.getInstance().getTimeInMillis();
        sortable.sortArray(array);
        long totalTimeMergeSort = Calendar.getInstance().getTimeInMillis() - sortStartedAt;
        afterSorting(array, totalTimeMergeSort);
        return totalTimeMergeSort;
    }
    private static long testHeapSort() {
        Sortable sortable = new HeapSort(); // HEAP SORT
        int[] array = createTestData();
        long sortStartedAt = Calendar.getInstance().getTimeInMillis();
        sortable.sortArray(array);
        long totalTimeHeapSort = Calendar.getInstance().getTimeInMillis() - sortStartedAt;
        afterSorting(array, totalTimeHeapSort);
        return totalTimeHeapSort;
    }

    public static void afterSorting(int[] array, long totalTime) {
        if(isSorted(array)) {
            System.out.println("Sorting is successful");
            System.out.println("Total time to sort: " + totalTime + "ms");
            System.out.println("Sorted array: ");
            if(ENABLE_DATA_DISPLAY) {
                displayArray(array);
                System.out.println();
                System.out.println("============================================================================================");
            }
        } else {
            System.out.println("Sorting is unsuccessful");
        }

    }

    private static int[] createTestData() {
        int[] array = new int[MAX_SIZE];
        Random random = new Random();
        for (int counter = 0; counter < MAX_SIZE; counter++) {
            array[counter] = random.nextInt(MAX_RANDOM_LIMIT);
        }
        if(ENABLE_DATA_DISPLAY) {
            System.out.println("============================================================================================");
            System.out.println("Test data (Before Sorting): ");
            displayArray(array);
            System.out.println();
            System.out.println("============================================================================================");
        }
        return array;
    }

    private static void displayArray(int[] array) {
        for (int number: array) {
            System.out.print(number + " ");
        }
    }

    private static boolean isSorted(int[] array) {

        for (int counter = 0; counter < MAX_SIZE-1; counter++) {
            if(array[counter] > array[counter+1]){
                System.out.println("problem at " + counter + " position");
                return false;
            }
        }
        return true;
    }
}
