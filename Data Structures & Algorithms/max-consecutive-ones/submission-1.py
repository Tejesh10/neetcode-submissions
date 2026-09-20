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


""" as far as i could see , the complexity for this code is as follows: 

 >> time complexity : O(n) -> since we're are using 1 for loop to iterate over an array of size n 
 >> space complexity : O(1) -> the only additional ds we are right now using here is a variable to store count , at two instances ... this doesn't affect much of the size of the code. hence the size complexity here reamins constant regardless of the size of the input array. 
"""


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
                


        