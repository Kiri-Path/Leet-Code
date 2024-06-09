#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

#You may assume that each input would have exactly one solution, and you may not use the same element twice.

#You can return the answer in any order.



### SOLUTION


###APPROACH  : 
#easiest way would be to look at all possible pairs using integers i & j in a nested for loop but that would make it an O(n^2).
# to avoid looking at all the pairs we can create a hash map where each key will be the number and value will be the index (because thats what the problem is asking).
# now we only need to loop through the array once and therefore will only be an O(n) solution. 
# so we pick a value, subtract it from the target so we know which value we are looking for and we can search for that in the array and return the index(value if it is)


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        

        #create hashmap
        h ={}

        for i in range(len(nums)): # go through all valid indicies
            h[nums[i]] = i #set the nums value at index i  as the key and then give it a value of the index 
            # note if we see duplicate numbers it will update the value with latest index.
        

        for i in range(len(nums)):
            y = target -nums[i] # we want to check if y exists in h and we want to ensure we are not using the same index! 

            if y in h and h[y] != i:
                return [i, h[y]]
