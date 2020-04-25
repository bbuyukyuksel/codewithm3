import math
min_3digit = 100
max_3digit = 999

def is_palindrome(num):
    num = str(num)
    digits = len(num)
    if digits % 2 == 0:
        # Even digits
        positive_to = digits//2
        negative_to = digits//2 - (digits+1)
    else:
        # Odd  digits
        positive_to = digits//2
        negative_to = digits//2 - (digits)

    first_half  = num[:positive_to]
    second_half = num[-1:negative_to:-1]
    return True if first_half == second_half else False


# Generate each numbers from : 100 x 100 , to 999 x 999
max = -1
for index, num in enumerate(
    [x*y for x in range(min_3digit, max_3digit+1) 
         for y in range(min_3digit, max_3digit+1)]):

        print(" Searching [{:<5}], {:^10}".format('.' * (index % 5), num), end='\r')
        if is_palindrome(num):
            max = num if num > max else max
print("\n", u'\u2713', "Largest palindrome product is ", max)
