"""
Given a sorted array consisting of only integers 
where every element appears twice except for one element 
which appears once. Find this single element that appears only once.

Example 1:
Input: [1,1,2,3,3,4,4,8,8]
Output: 2
Example 2:
Input: [3,3,7,7,10,11,11]
Output: 10
"""
#nums= [3,3,7,10,10,11,11,12,12] # even index 10  same as pos-1  => left
#array = [3,3,7,7,10,11,11]   # odd index 3   same as pos-1  => right
#array = [3,3,7,7,11,11,19,12,12] # even index 10  different from pos-1 => right
#array = [3,3,6,7,7,11,11]   # odd index 3   different from pos-1 => left
nums = [1,1,2]


class Solution(object):
    def singleNonDuplicate(self, nums):
        if nums.__len__() == 0:
            return None
        if nums.__len__() == 1:
            return nums[0]         
        pos = nums.__len__() >> 1
        up_pos = nums.__len__()
        low_pos = 0
        while nums[pos] == nums[pos-1] or nums[pos] == nums[pos+1]:
            direction = (nums[pos] == nums[pos-1]) ^ (pos % 2)
            if direction==0: # True is right        
                low_pos = pos
                pos = (pos + up_pos) >> 1
            else: # False is left
                up_pos = pos
                pos = (pos + low_pos) >> 1
            if pos == 0 or pos == nums.__len__()-1:
                return nums[pos]
        return nums[pos]