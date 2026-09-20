class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        """"
         >> information so far is that we only will ever have 1's or 0's 
         >> and the n value is limited to only 100k inputs size
         >> goal : we need to find number of consecutive 1's in the given array. 

         >> questions: 
         if no consecutive ones are not found then what should i display ? 
         if empty array then what should i display ?  
        """
        numsSize = len(nums)
        maxCount, currCount = 0, 0
        for idx, val in enumerate(nums):
            if val == 1: 
                currCount += 1
                if currCount > maxCount:
                    maxCount = currCount
            else:
                currCount = 0
        return maxCount
             
""" dry run: 
input : [1,1,0,1,1,1]
// itr1 ; 
val - 1 , currcount - 1 , maxCount - 1 

// itr2 : 
    val - 1 true, >> currCount - 2 , maxCount 2


// itr3 : 
    val - 0 false, >> currCount - 0

// itr4: 
    val - 1 true >> currCount - 1, maxCount - 2


// itr5: 
    val - 1 true >> crrCount - 2, maxCount - 2

// itr6: 
    val - 1 true >> currCount - 3, maxCount - 3
"""
                


        