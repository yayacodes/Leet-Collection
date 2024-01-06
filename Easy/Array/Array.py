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
    


    
if __name__ == '__main__':
    ar = Array()
    nums = [0,0,1,1,1,2,2,3,3,4]
    ar.removeDuplicates(nums)