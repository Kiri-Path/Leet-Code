class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        n = len(nums)

        k %= n  # Ensure k is within the range of the array length

        # Reverse the entire array by splicing the list and then -1 will reverse the order
        #note: a single colon is to set a range, a double colon is to set the step change if you want to pick every other number etc.
        nums[:] = nums[::-1]

        # Reverse the first k elements
        # splicing :k, this select from the beginning to k'th index. then we apply the ::-1 to reverse the order
        nums[:k] = nums[:k][::-1]

        # Reverse the remaining elements
        # now we do the same thing with the values after k'th index to the end. 
        nums[k:] = nums[k:][::-1]
