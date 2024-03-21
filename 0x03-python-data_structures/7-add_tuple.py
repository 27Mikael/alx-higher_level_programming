#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    new_tup = ()

    a = tuple_a[:2] + (0, 0)
    b = tuple_b[:2] + (0, 0)

    new_tup = a(a[0] + b[0], a[1] + b[1])

    return new_tup
