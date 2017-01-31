package algoandds.sorting;

/**
 * Created by Sachin Shikhare on 16-11-2016.
 */
public class BubbleSort implements Sortable {

//    @Override
//    public void sortArray(int[] array) {
//
////        TODO: Not implemented
//        for (int cntr1 = 0; cntr1 < array.length; cntr1++) {
//            for (int cntr2 = array.length; cntr2 < cntr1 + 1; cntr2--) {
//                if(array[cntr2] < array[cntr2-1]) {
//                    int temp = array[cntr2];
//                    array[cntr2-1] = array[cntr2];
//                    array[cntr2] = temp;
//                }
//            }
//        }
//    }

    public static void main(String[] args) {
        int[] array = {3,1,7,9,6,5,4,8,2};
        new BubbleSort().sortArray(array);
        for (int n : array) {
            System.out.println(n);
        }
    }

	public void sortArray(int[] array) {
		// TODO Auto-generated method stub
		
	}

}
