#!/usr/bin/python3
'''Minimum Operations Challenge or task'''

def minOperations(n: int) -> int:
    """
    Calculate the fewest number of operations needed to result in exactly n H characters in the file.
    :param n: the number of H characters to produce
    :return: the fewest number of operations needed, or 0 if n is impossible to achieve
    """
    if n < 1:
        return 0
    if n == 1:
        return 0
    # Find the largest factor of n
    for i in range(n // 2, 0, -1):
        if n % i == 0:
            # Recursively calculate the number of operations needed
            return minOperations(i) + (n // i)
    # If no factors are found, n is prime and cannot be achieved
    return 0
