#LEET CODE: Minimum number of swaps to make the string balanced

class Solution:
    def minSwaps(self, s: str) -> int:
        # Initialize counters for unbalanced closing brackets
        close_count = 0
        max_close_count = 0
        
        # Iterate through the string
        for char in s:
            if char == '[':
                if close_count > 0:
                    # We have an unmatched closing bracket, so pair it with this opening bracket
                    close_count -= 1
                else:
                    # No unmatched closing bracket, nothing to pair
                    pass
            else:  # char == ']'
                close_count += 1
                max_close_count = max(max_close_count, close_count)
        
        # The minimum number of swaps needed is half the max_close_count
        return (max_close_count + 1) // 2



