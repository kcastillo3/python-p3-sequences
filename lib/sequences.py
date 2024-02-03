#!/usr/bin/env python3
'''
Write a function print_fibonacci() 
that prints a list of the fibonacci sequence up to the length provided in the function's parameters.
'''
def print_fibonacci(length):
    if length <= 0:
        print([])
    elif length == 1:
        print([0])
    elif length == 2:
        print([0, 1])
    else:
        fibonacci_list = [0, 1]  # Corrected initialization of fibonacci_list
        for _ in range(2, length):  # Corrected the typo in 'length'
            next_fib = fibonacci_list[-1] + fibonacci_list[-2]
            fibonacci_list.append(next_fib)
        print(fibonacci_list)