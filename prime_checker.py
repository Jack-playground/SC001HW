"""
File: prime_checker.py
Name:
-----------------------
This program asks our user for input and checks if the input is a
prime number or not. First, ” Welcome to the prime checker” will be printed on Console.
And the program will continually ask the user to enter an integer 
that is greater than 1 and checks if it is a prime number.
The program ends when the user enter the EXIT number.
"""


def main():
	"""
	TODO:
	"""
	print('Welcome to the prime checker!')
	n = int(input('n: '))
	while True:
		is_prime_number(n)
		if n < 1:
			break


def is_prime_number(n):
	i = 1
	count = 0
	while not (i == n):
		if n % i == 0:
			count += 1
		if count > 2:
			break
		i += 1
# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()
