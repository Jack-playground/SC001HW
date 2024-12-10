"""
File: hailstone.py
Name:Shawn
-----------------------
This program should implement a console program that simulates
the execution of the Hailstone sequence, defined by Douglas
Hofstadter. Output format should match what is shown in the sample
run in the Assignment 2 Handout.
"""


def main():
    """
    TODO:
    """
    print('This programs computes Hailstone Sequence.')
    num = int(input('Enter a number: '))
    step = 0
    while num != 1:
        step += 1
        if num % 2 != 0:
            print(str(num)+' is odd, so I make 3n+1: ', end='')
            num = num * 3 + 1
            print(num)
        else:
            print(str(num) + ' is even, so I take half: ', end='')
            num = int(num / 2)
            print(num)
    print('It took ' + str(step) + ' steps to reach 1.')


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
    main()
