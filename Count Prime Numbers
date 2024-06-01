class Solution:
    def countPrimes(self, n: int) -> int:
            def is_prime(num):
                if num <= 1:
                    return False
                for i in range(2, int(num**0.5) + 1): ## by default if a* b = c, then by default the a or b must be < sqrt(c). thats why we take the range up to the sqrt of the number +1 (the +1 is because of the indexing in python)
                    if num % i == 0:
                        return False
                return True

            count = 0
            for i in range(2, n):
                if is_prime(i):
                    count += 1
            return count
