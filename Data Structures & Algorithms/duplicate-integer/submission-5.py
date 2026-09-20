class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # This one has slightly higher space complexity as we are using a additonal data structure -- set here which add space. 
        # space: O(n) // Time: O(n)
        UniqueSet = set()
        for number in nums :
            if number in UniqueSet :
                return True # duplicate found 
            UniqueSet.add(number)
        return False
                
