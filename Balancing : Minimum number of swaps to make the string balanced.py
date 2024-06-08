#LEET CODE: Minimum number of swaps to make the string balanced

class Solution:
    def minSwaps(self, s: str) -> int:
    # Cancel out all the matched pairs, then we'll be left with ']]]..[[['.
    # The answer is ceil(# of unmatched pairs // 2).
    # Cancel out all the matched pairs, then we'll be left with ']]]..[[['.
    # The answer is ceil(# of unmatched pairs // 2).
        imbalance = 0
        max_imbalance = 0

        for char in s:
            if char =='[':
                imbalance +=1
            else:
                imbalance -=1
            
            if imbalance <0:
                max_imbalance = max(max_imbalance, -imbalance)
        return (max_imbalance+1)//2
