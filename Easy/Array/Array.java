package Easy.Array;

import java.util.Arrays;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;

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

    // Contains Duplicate
    public boolean containsDuplicate(int[] nums) {
        Set<Integer> set = new HashSet<>();

        for (int n : nums) {
            if (set.contains(n))
                return true;
            else
                set.add(n);
        }
        return false;
    }

    // Single Number
    public int singleNumber(int[] nums) {
        Map<Integer, Integer> map = new HashMap<Integer, Integer>();

        for (int n : nums) {
            map.put(n, map.getOrDefault(n, 0) + 1);
        }

        for (Map.Entry<Integer, Integer> entry : map.entrySet()) {
            if (entry.getValue() == 1)
                return entry.getKey();
        }
        return -1;
    }

    // Intersection of Two Arrays II
    public int[] intersect(int[] nums1, int[] nums2) {
        if (nums1.length > nums2.length)
            return intersect(nums2, nums1);

        HashMap<Integer, Integer> m = new HashMap<Integer, Integer>();

        for (int x : nums1) {
            m.put(x, m.getOrDefault(x, 0) + 1);
        }

        int k = 0;

        for (int y : nums2) {
            int count = m.getOrDefault(y, 0);
            if (count > 0) {
                nums1[k++] = y;
                m.put(y, count - 1);
            }
        }
        return Arrays.copyOfRange(nums1, 0, k);
    }

}