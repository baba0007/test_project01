#lambda
s = lambda a, b, c: a if a > b and a > c else b if b > c else c
print(f'The bigger number is {s(10, 20, 5)}')
