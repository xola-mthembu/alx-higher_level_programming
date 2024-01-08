#!/usr/bin/python3

def no_c(my_string):
    """
    This function removes all characters 'c' and 'C' from a string.
    It returns the new string.
    """
    return ''.join(char for char in my_string if char not in 'cC')

if __name__ == "__main__":
    # Example usage
    print(no_c("Best School"))
    print(no_c("Chicago"))
    print(no_c("C is fun!"))
