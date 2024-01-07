from ast import List
import collections


class Array(object):
        
    #Remove Duplicates From Sorted Array
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        i = 0
        
        if len(nums) == 0:
            return 0
        
        for num in nums[1:]:
            if nums[i] != num:
                i += 1
                nums[i] = num
        
        return i + 1

    #Best Time To Buy and Sell
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        i = 0
        j = 1
        profit = 0
        
        while (j < len(prices)):
            if prices[j] > prices[i]:
                profit += (prices[j] - prices[i])
            i+=1
            j+=1
        
        return profit
    
    #Rotate Array 
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums) - 1
        k %= len(nums)

        self.reverse(nums, 0, n)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, n)

    def reverse(self, nums, start, end):

        while start < end:
            temp = nums[start]
            nums[start] = nums[end]
            nums[end] = temp
            start += 1
            end -= 1

    #Contains Duplicate
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        unique = set()
        
        for i in nums:
            if i in unique:
                return True
            else:
                unique.add(i)
        return False
    
    #Single Number
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        map = {}
        
        for n in nums:
            if n not in map:
                map[n] = 1
            else:
                map[n] += 1
                
        for key in map:
            if map[key] == 1:
                return key

    #Intersection of Two Arrays II
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if not nums1 or not nums2:
            return []

        map1 = collections.Counter(nums1)

        result = []

        for num in nums2:
            if num in map1 and map1[num]:
                result.append(num)
                map1[num] -= 1
    
        return result
    
    # Move Zeroes
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        j = 0
        
        for n in nums:
            if n != 0:
                nums[j] = n
                j+=1
                
        while j < len(nums):
            nums[j] = 0
            j+=1
    
    # Plus One 
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        n = len(digits) - 1
        
        while digits[n] == 9:
            digits[n] = 0
            n = n - 1
        if n < 0:
            digits = [1] + digits
        else:
            digits[n] = digits[n] + 1
        return digits
            
    
if __name__ == '__main__':
    ar = Array()
    nums = [0,0,1,1,1,2,2,3,3,4]
    ar.removeDuplicates(nums)