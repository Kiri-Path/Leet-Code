#LEET CODE: Least Number of Unique Integers after K Removals


# approach: 
# create a dictionary of numbers and the frequency they appear in
# Then create a unique count field which will the length of the list of all the freqnecy values
# now the important bit... if the frequency value is less than the value of k then we need to reduce the the count
# because we would remove that many integers, then we need to reduce k by that many values.


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
