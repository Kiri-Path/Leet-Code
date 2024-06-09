# Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

# Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.



### SOLUTION

### APPROACH

#the key difference between this question and 2 sum, is that our array is sorted!
# so we can a 2 pointer algorithm, i.e we can have a right and left pointer starting from either end of the array
# if the sum of the 2 end points is less than or greater than the target then we just need to move the left pointer up or right pointer down respectively. 
# this is time complexity O(n) and space compelxity of O(1) constant since we are not storing anything 



class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        


        #2 pointer algorithm
        l = 0
        n = len(numbers)
        r = n-1


        while l<r:
            summ = numbers[l] + numbers[r]
            if summ ==target:
                return [l+1, r+1] # question asks to add one
            elif summ < target:
                l += 1 # if our sum is less than the target then we can increase the summ moving moving the left counter to the next index as its a sorted array therefore guaranteeing it will be bigger
            else:
                r -=1 # if our sum is bigger than the target then we can decrease the summ by moving the right counter down to the index before thus guaranteeing the summ will be smaller.

