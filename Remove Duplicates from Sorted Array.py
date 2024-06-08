### SOLUTION 2 :  O(n)  time , O(N) space since we re-create list


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:


        # set(nums) convers the list to a set. Converting to a set removes duplicates.
        # then we can use sorted function to sort the order by default asc
        # convert back to a list

        nums[:] = sorted(set(nums))
        return len(nums)



### SOLUTION 2 :  O(n)  time , O(1) space since we are doing the change  IN PLACE

here we create left and right pointer.
right pointer is going to go along list and check if the one before is the same
Left pointer is going to hold the position of the string which needs to be swapped out after the right pointer identifies the duplicate.

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:


        l = 1
        for r in range(1, len(nums)):
            if nums[r] != nums[r-1]:
                nums[l] = nums[r]
                l += 1
        return l
