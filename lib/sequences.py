#!/usr/bin/env python3
def print_fibonacci(n):
    """
    Prints the Fibonacci sequence up to the specified length.

    Args:
        n (int): The length of the Fibonacci sequence to print.

    Returns:
        None
    """
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    print(fib_sequence[:n])