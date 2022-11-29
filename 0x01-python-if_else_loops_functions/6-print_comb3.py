#!/usr/bin/python3
number = 0
for number in range(0, 9):
    print("{:02d}".format(number), end="\n" if number == 89 else ", ")
