### SOLUTION

APPROACH:
# Initialize a counter unmatched = 0 to track unmatched opening brackets [.
# Iterate through the string:
# Increment unmatched for each [.
# Decrement unmatched for each ] if unmatched > 0 (indicating a match).
# Calculate the number of swaps needed to balance the string: (unmatched + 1) // 2.
# This approach ensures we count and balance unmatched opening brackets efficiently in O(n) time and O(1) space.


class Solution:
  def minSwaps(self, s: str) -> int:
    # Cancel out all the matched pairs, then we'll be left with ']]]..[[['.
    # The answer is ceil(# of unmatched pairs // 2).
    unmatched = 0

    for c in s:
      if c == '[':
        unmatched += 1
      elif unmatched > 0:  # c == ']' and there's a match.
        unmatched -= 1

    return (unmatched + 1) // 2

        
