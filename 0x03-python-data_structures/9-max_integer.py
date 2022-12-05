#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        x = my_list[0]
        for y in my_list:
            if y > x:
                y = x
            return x
        return None

