#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    reversed_list = my_list[:]
    if idx >= 0 or idx < len(reversed_list):
         reversed_list[idx] = element
         return(reversed_list)
    return(my_list)
