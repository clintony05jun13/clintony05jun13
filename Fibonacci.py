# This file will print the first ten numbers in the Fibonacci Sequence

num1 = 1
num2 = 1
print(num1)
print(num2)

for i in range(8):
    fib = num1 + num2
    num2 = num1
    num1 = fib
    print(fib)