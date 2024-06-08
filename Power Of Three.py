class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        while n % 3 == 0: ##what this function does is divde n by 3 and then reassign the result back to n
            n /= 3
        # once n stops being divisble by 3 with no remainder it breaks the loop and then in the final part it checks if n ended up equaling 1, if it did then yes it was  apower of 3 else no.
        return n == 1 
