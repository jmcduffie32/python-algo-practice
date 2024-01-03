"""Euclid's algorithm for finding the greatest common divisor of two integers"""
import math

def euclid_gcd(x, y):
    larger = max(x,y)
    smaller = min(x,y)
    remainder = None
    
    while remainder != 0:
        remainder = larger % smaller
        larger, smaller = smaller, remainder

    return larger

print(euclid_gcd(105, 33))
print(math.gcd(105, 33))
