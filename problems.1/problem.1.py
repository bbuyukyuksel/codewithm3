'''
# Question:

    (?) Find the sum of all the multiples of 3 or 5 below 1000.

'''

# multiples of 3
m_of_3 = list(range(3, 1000, 3))
# or
#max_step = 1 + (999 - 3) // 3 
#m_of_3 = [3*i for i in range(1, max_step+1)]

# --------------------------------------------------

# multiples of 5
m_of_5 = list(range(5, 1000, 5))
# or
#max_step = 1 + (999 - 5) // 5 
#m_of_5 = [5*i for i in range(1, max_step+1)]

#print(m_of_5)
#print(m_of_3)

# Combine multiples of 3 and 5
common_elements = []
common_elements.extend(m_of_3)
common_elements.extend(m_of_5)

# Eliminate same elements
common_elements = list(set(common_elements))

# Result
sums = sum(common_elements)
print(">> Result =", sums)
