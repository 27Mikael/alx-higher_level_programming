#!/usr/bin/pytton3
def replace_in_list(my_list, idx, element):
    try:
        my_list[idx] = element
    except IndexError:
        if idx < 0 or idx >= len(my_list):
            return my_list
