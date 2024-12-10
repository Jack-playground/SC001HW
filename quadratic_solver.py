"""
File: quadratic_solver.py
Name: Shawn
-----------------------
This program should implement a console program
that asks 3 inputs (a, b, and c)
from users to compute the roots of equation:
ax^2 + bx + c = 0
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

import math


def main():
	"""
	input: a, b, c
	calculate a discriminant to determine which condition to get in to it
	"""
	a = int(input('Enter a: '))
	b = int(input('Enter b: '))
	c = int(input('Enter c: '))
	discriminant = b*b-4*a*c
	if discriminant < 0:
		print('No Real Roots')
	elif discriminant == 0:
		print('One Root: '+str((-b + math.sqrt(discriminant))/2*a))
	else:
		print('Two Roots: '+str((-b + math.sqrt(discriminant))/2*a)+', '+str((-b - math.sqrt(discriminant))/2*a))


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()
