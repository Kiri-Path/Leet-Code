# typically if we just wanted to reverse a list we would just need to splice the list and reverse the order. for example...

def reverseString(s):
    s = s[::-1]
    return s

# Example output
s = ['h', 'e', 'l', 'l', 'o']
s = reverseString(s)
print(s)  # Output: ['o', 'l', 'l', 'e', 'h']


# However in this particular questions it says to do this by modifying the input array in place with O(1) extra memeroy
# this means the solution should not use extra space that grows with the input size, other than a fixed amount of space (like a few variables). 
#Using slicing to create a new reversed list would require O(n) additional space, where n is the number of elements in the list.
#therefore, we do not want to create  a new list, instead we want to re-arrange the existing list

def reverseString(s):
    # first set right and left with indexes 0 and len(s)-1 respectively (so they both start from opposite ends)
    left, right = 0, len(s) - 1
    
    while left < right: # now we are setting the while condition that the index on the left should always be less than the index on the right, the moment this stops we break out of the loop.
        # Swap the elements at the left and right pointers
        s[left], s[right] = s[right], s[left]
        # After swapping we then want to increment the index of the left side  and decrement the index on the right side so we move the pointers towards the center
        left += 1
        right -= 1

    # as we continue to grow the index of the left and decrease the index on the right eventually they will either equal each other (if we have odd set of numbers) or the left index will be greater than the right index. at which point the loop breaks.


