#!/usr/bin/python3

if __name__ == "__main__":
    """Import variable 'a' from variable_load_5 and print its value."""
    from variable_load_5 import a

    if 'a' in globals():
        print("a =", a)
    else:
        print("Variable 'a' is missing.")
