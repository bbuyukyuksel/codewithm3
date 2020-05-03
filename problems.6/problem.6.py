def SquareGenerator(_list_):
    for _item_ in _list_:
        yield _item_ ** 2

## Create Range List
_from_, _to_ = 1, 100

# [1, 2, 3, ..., n]
_from_to_ = range(_from_, _to_+1)

# (1 + 2 + 3 + ... + n) x (1 + 2 + 3 + ... + n)
square_of_sums = sum(_from_to_) **2

# (1x1) + (2x2) + (3x3) + ... (nxn)
sum_of_squares = 0
for item in SquareGenerator(_from_to_):
    sum_of_squares += item

subtraction = square_of_sums - sum_of_squares

print("Square of Sums  :", square_of_sums)
print("Sum of Squares  :", sum_of_squares)
print("Subtraction     :", subtraction)
print(f"Operation       : {square_of_sums} - {sum_of_squares} = {subtraction}")

