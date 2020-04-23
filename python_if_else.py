# https://www.hackerrank.com/challenges/py-if-else/problem?h_r=next-challenge&h_v=zen

#!/bin/python3

import math
import os
import random
import re
import sys


"""
if __name__ == '__main__':
    n = int(input().strip())
""" 
n = 3

def weird_or_not(n):
    weird_numbers = [3, 5]
    for i in range(6, 21, 2):
        weird_numbers.append(i)
    print(weird_numbers)
    if n % 2 != 0:
        print("Weird")
    elif n not in weird_numbers:
        print("Not Weird")
    else:
        print("Weird")


weird_or_not(n)


"""
Task
Given an integer n, perform the following conditional actions:

If n is odd, print Weird
If n is even and in the inclusive range of 2 to 5, print Not Weird
If n is even and in the inclusive range of 6 to 20, print Weird
If n is even and greater than 20, print Not Weird

Input Format
A single line containing a positive integer,

.

Constraints

Output Format

Print Weird if the number is weird; otherwise, print Not Weird.

Sample Input 0

3

Sample Output 0

Weird

Explanation 0


is odd and odd numbers are weird, so we print Weird.

Sample Input 1

24

Sample Output 1

Not Weird

Explanation 1


and is even, so it isn't weird. Thus, we print Not Weird.
"""