class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        tc: O(n)
        sc: O(1)
        at first i used a code logic where i had to rely on an additional data structure to copy the elements that not matched with the val. but it had higher space complexity and not much efficient althought the time complexity is still O(n). 

        My second thought was to use the pop method the nums array while also looping on the nums array simultaneously. While this approach may seems intuitively correct but on deeper look it kinda works like an item/entity being operated by 2 diffferent operations and failling to clean locking ---in our case the for looping on the nums array while also popping on the same nums array resulted in missing on some of genuinely good elements of nums that did not matched the val , completely messing up our final resultant array. 

        thrid approch , after having a thorough brainsotrming with gemini i understood that we can just replace the values with each index entry that is our current approach and final solution without rely in on the Neetcode.io solution from textbook. >> in this tc and sc are best of what could squeez with the given limitations.
        """
        idx = 0
        for value in nums:
            if val != value:
                print("executing the value: ", value)
                nums[idx] = value
                idx += 1 
        print("nums array : ", nums)
        return idx
                





# Alternate solutions : 

""" 

>> Effecient time complexity of O(n), 
>> bad space complexity of O(n) -> since we are using an additional new array data structure [resArr] to hold to unremoved elements. 

numsSize = len(nums)
        resArr = []
        counter = 0
        if val > 50: 
            return 0
        for idx, value in enumerate(nums):
            if value != val:
                print("value matched with : ", value)
                resArr.append(value)
            else: 
                counter += 1
        nums.clear()
        nums.extend(resArr)
        return len(nums)

"""