Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.




### Solution 1
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:


        # to check if there are duplicates we just need to confirm if the lengths of the list and the set version is the same
        return len(nums) != len(set(nums))




#### SOLUTION 2

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))


        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False



#### SOLUTION 3 using standard list

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))


        seen = []

        for n in nums:
            if n in seen:
                return True
            seen.append(n)
        return False
