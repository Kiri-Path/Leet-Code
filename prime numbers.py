### Write a function to identify prime numbers


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



## approach 2 : check if the number is less than 2 so we ignore 1. now we know if 2 numbers mutliply to give a new number, either one of those numbers must be less than the sqrt of the number.
for example a* b = c then therefore either a<=sqrt(c) or b <= sqrt(c). so all we need to do is iterate from 2 through the numbers up to the sqrt of n


def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True



##approach 3:
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
