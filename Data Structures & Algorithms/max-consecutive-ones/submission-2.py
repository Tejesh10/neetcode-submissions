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


# INITIAL THOUGHTS: 
"""at first i thought we could just use a map to store the key and value pairs to count the occurences of each element of the array, but the idea fails cuz the map would all the entries realted to one 1's throughout the array regardless of the position , meaning the code would count the 1's occurence although they are not consecutively present. 

this approach clearly not the one we seek . 


Secondly, i thought of the current code without looking at the predefined solutions provided in NeetCode.io here

Overall Nice work, as I didn't rely on the textbook solutions and had to think thorugh the solution by myself.



Finally, I need to understand other alternative solutions provided here in the Neetcode.io textbook."""

# FINAL NOTES: 

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
                


        