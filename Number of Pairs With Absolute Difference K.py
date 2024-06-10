#### SOLUTION



#### APPROACH
# 1) Initialize an empty dictionary to store the frequency of each number.
# 2) create dicitonary
# 3) iterate through each unique number in th efrequecny dictionary and check if the number minu k exists in the dictionary
# 4) if it does calculate the number of valid pairs formed by the current number and its counterpark (number minus 'k')




class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        # Initialize an empty frequency dictionary
        frequency_dict = {}

        # Populate the frequency dictionary with counts of each number in nums
        for num in nums:
            if num in frequency_dict:
                frequency_dict[num] += 1
            else:
                frequency_dict[num] = 1

        # Calculate the number of valid pairs
        count = 0
        for num in frequency_dict:
            if num - k in frequency_dict:
                count += frequency_dict[num] * frequency_dict[num - k]

        return count
