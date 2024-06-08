#LEET CODE: Least Number of Unique Integers after K Removals

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:

        freq_counter = {}
        
        for num in arr:
            if num in freq_counter:
                freq_counter[num] +=1
            else:
                freq_counter[num] =1

        freq_values = list(freq_counter.values())  
        sorted_freq = sorted(freq_values)

        unique_count = len(sorted_freq)

        for freq in sorted_freq:
            if k>= freq:
                k -= freq
                unique_count -=1
            else:
                break
        return unique_count
