### write program to print "hello world"

def say_hello(first_name):
    print("Hello,", first_name + "!")

# Example usage:
user_name = input("Enter your first name: ")
say_hello(user_name)



### write program to check if a SINGLE number is even or odd

def check_even_odd(number):
    if number % 2 == 0:
        print(number, "is even.")
    else:
        print(number, "is odd.")

#### Example usage:
num = int(input("Enter a number: "))
check_even_odd(num)


### write a program to check if a list of numbers is even or odd, return as 2 lists

def separate_even_odd(numbers):
    even_numbers = []
    odd_numbers = []
    for num in numbers:
        if num % 2 == 0:
            even_numbers.append(num)
        else:
            odd_numbers.append(num)
    return even_numbers, odd_numbers

#### Example usage:
num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_nums, odd_nums = separate_even_odd(num_list)
print("Even numbers:", even_nums)
print("Odd numbers:", odd_nums)


### . Write a program to find the sum of all numbers in a list. 

def sum_of_list(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

#### Example usage:
num_list = [1, 2, 3, 4, 5]
print("Sum of numbers in the list:", sum_of_list(num_list))


###4. Write a program to find the largest number in a list. 

def find_largest_number(numbers):
    if not numbers:  # Check if the list is empty
        return None  # If the list is empty, return None
    
    max_num = numbers[0]  # Assume the first number is the largest initially
    for num in numbers:
        if num > max_num:
            max_num = num  # Update max_num if a larger number is found
    return max_num

#### Example usage:
num_list = [10, 5, 20, 8, 15]
largest_num = find_largest_number(num_list)
print("Largest number in the list:", largest_num)



### wirte a program to reverse a string

def reverse_string(s):
    return s[::-1]

#### Example usage:
input_string = "hello"
reversed_string = reverse_string(input_string)
print("Reversed string:", reversed_string)


### write a program to find th efactorial of a number

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

#### Example usage:
num = 5
print("Factorial of", num, "is", factorial(num))


### write a program to find if a number is a prime

approach 1: the obvious way to do this would be to check if any number small than 'n' can divide into 'n' without any remainder (except for 1) , if so then it is not prime else it is

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

# Example usage:
num = 17
print("Is", num, "a prime number?", is_prime(num))

the problem with this solution, it has to iterate through every number between 2 and n. this is not optimum! so we can do via second solution which only checks a handful of dvisions

approach 2 :

check if the number is less than 2 so we ignore 1. now we know if 2 numbers mutliply to give a new number, either one of those numbers must be less than the sqrt of the number.
for example a* b = c then therefore either a<=sqrt(c) or b <= sqrt(c). so all we need to do is iterate from 2 through the numbers up to the sqrt of n


def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True



approach 3:
first check if the number is <1 if so then it is not prime
check if iis then <=3 if so then it is prime
then check if the number is perfectly divisble by 2 or perfectly divisnble by 3, if so then it is not prime

now the rest of the checks is based on the fact a prime number takes the form 6n+(or)-1

we now intdouce i = 5 
now we know if 2 numbers mutliply to give a new number, either one of those numbers must be less than the sqrt of the number.
for example a* b = c then therefore either a<=sqrt(c) or b <= sqrt(c)

so we check WHILE  i*i < n (while this statement is true)
if n can be divided by i and give no remainder or n divided by i+2 gives no remainder then it is not prime 
then we now incrmeent += 6 onto i. (this follows the 6n+(or)-1 
otherwise it is prime

def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# Example usage:
num = 17
print("Is", num, "a prime number?", is_prime(num))

this is a better solution since it only iterates through a number of divisions as opposed ot the first solutions which tries to divide every number.



### write a function to convert Celcius to Fahrenheit

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# Example usage:
celsius_value = 20
fahrenheit_value = celsius_to_fahrenheit(celsius_value)
print(f"{celsius_value} degrees Celsius is equal to {fahrenheit_value} degrees Fahrenheit.")


### write a program to find the largest element in a list

def find_largest(numbers):
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest

# Test the function
nums = [10, 5, 8, 20, 3]
largest_num = find_largest(nums)
print(f"The largest number is {largest_num}")


write a python program to count the frequency of each element in a list

def count_frequency(numbers):
    frequency = {}
    for num in numbers:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1
    return frequency

# Test the function
nums = [1, 2, 3, 2, 1, 3, 2, 4, 5, 4]
frequency_count = count_frequency(nums)
print(frequency_count)



#### write a program to find the common elements between 2 lists

def find_common_elements(list1, list2):
    common_elements = []
    for item in list1:
        if item in list2:
            common_elements.append(item)
    return common_elements

# Test the function
list_a = [1, 2, 3, 4, 5]
list_b = [4, 5, 6, 7, 8]
common = find_common_elements(list_a, list_b)
print(common)



#### write a program to find the unique numbers in a list

def remove_duplicates(numbers):
    unique_numbers = []
    for num in numbers:
        if num not in unique_numbers:
            unique_numbers.append(num)
    return unique_numbers

# Test the function
nums = [1, 2, 3, 2, 1, 3, 2, 4, 5, 4]
unique_nums = remove_duplicates(nums)
print(unique_nums)




### From 2 lists, check how many items in one list smaller or equal to each value in the other list.

for eg 
say i have 2 lists 
A = [ 1,2,3]
B = [2,4]

i want to check for each number in B how any numbers in A are less than or equal.
for example first element in B is 2, there are 2 numbers in A which are less than or equal to this. tehen next element in B is 4, there are 3 elements in A which are less than this. 

therefore output should be [2,3]

def count_less_equal(A, B):
    result = []
    for b in B:
        count = 0
        for a in A:
            if a <= b:
                count += 1
        result.append(count)
    return result
