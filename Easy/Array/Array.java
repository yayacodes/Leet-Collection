package Easy.Array;

public class Array {

    public Array() {

    }

    public static void main(String[] args) {
        Array a = new Array();
        a.removeDuplicates(new int[] { 0, 0, 1, 1, 1, 2, 2, 3, 3, 4 });
    }

    // Remove Duplicates From Sorted Array
    public int removeDuplicates(int[] nums) {
        if (nums.length == 0)
            return 0;

        int insertIndex = 1;

        for (int i = 1; i < nums.length; i++) {
            if (nums[i] != nums[i - 1]) {
                nums[insertIndex] = nums[i];
                insertIndex++;
            }

        }

        return insertIndex;
    }

    // Best Time to Buy and Sell
    public int maxProfit(int[] prices) {

        int i = 0;
        int j = 1;
        int profit = 0;

        while (j < prices.length) {
            if (prices[j] > prices[i]) {
                profit += (prices[j] - prices[i]);
            }
            j++;
            i++;
        }
        return profit;
    }

    // Rotate Array
    public void rotate(int[] nums, int k) {
        int n = nums.length - 1;
        k %= nums.length;

        reverse(nums, 0, n);
        reverse(nums, 0, k - 1);
        reverse(nums, k, n);
    }

    public void reverse(int[] nums, int start, int end) {
        while (start < end) {
            int temp = nums[start];
            nums[start] = nums[end];
            nums[end] = temp;
            start++;
            end--;
        }
    }

}