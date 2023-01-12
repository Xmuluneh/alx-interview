#!/usr/bin/python3
'''
in a text file, there is a single character H.
Your text editor can execute only two operations in this file:
Copy All and Paste. Given a number n, write a method that calculates
the fewest number of operations needed to result
in exactly n H characters in the file.
'''


def minOperations(n):
    '''
    a function that calculates the fewest number of operations
    needed to result in exactly n & H characters in the file
    args:
        n:
        -number of charters to be displayed
    return:
          -: number of minimum operation
    '''
    if n <= 0:
        return 0

    count = 0
    prev = 0
    curr = 1

    while (curr < n):
        position = n - curr

        if (position % curr == 0):
            prev = curr
            curr += prev
            count += 2
        else:
            curr += prev
            count += 1
    return count
