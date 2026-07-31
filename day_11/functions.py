#day 11 : functions
#exercise 1
#1
def add_two_numbers(a, b):
    return a + b

# Example usage:
print(add_two_numbers(5, 7))  

#2
import math

def area_of_circle(r):
    return math.pi * r * r

# Example usage:
print(area_of_circle(5)) 

#3
def add_all_nums(*args):
    # Check if all items in the arguments are int or float
    for item in args:
        if not isinstance(item, (int, float)):
            return f"Error: All items must be numbers. Found invalid type '{type(item).__name__}' for value: {item}"
    
    # If all items are valid, return the sum
    return sum(args)

# Example usage:
print(add_all_nums(1, 2, 3, 4.5))       
print(add_all_nums(1, "two", 3))       
print(add_all_nums(1, [2, 3]))         
