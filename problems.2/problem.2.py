'''
# Question:
    
    (?) By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

'''
is_even = lambda x: True if x % 2 == 0 else False

def fibonacci(num):
    if num < 2:
        return num
    else:
        return fibonacci(num-1) + fibonacci(num-2)

# we'll start from second term index
# 0, 1, 1, 2, ... 

term = 2
sums = 0
while True:
    term_result = fibonacci(term)
    if(term_result > 4e6):
        print("Last term is", term, term_result)
        break
    if(is_even(term_result)):
        print("++ adding value", term_result)
        sums += term_result
    else:
        print('.. skipping value', term_result)
    term += 1

print("Result =", sums)