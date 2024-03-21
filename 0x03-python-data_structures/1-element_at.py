#!/usr/bin/pyton3
def element_at(my_list, idx):
    try:
        my_list[idx]
    except IndexError:
        if idx < 0 or idx >= len(my_list):
            return None
