"""
1. Generate all prime numbers which are there within N number
let's say if n = 10
output = 2, 3, 5, 7
"""

def generate_prime_numbers_within_a_range():
    number = int(input("Enter the range value to generate prime numbers:"))
    list1 = []
    for n in range(2,number+1):
        for i in range(2,n):
            if n % i == 0:
               break
        else:
                list1.append(str(n))
    print(','.join(list1))

generate_prime_numbers_within_a_range()

import sys