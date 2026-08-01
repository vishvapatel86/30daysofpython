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

#4
def convert_celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Example usage:
print(convert_celsius_to_fahrenheit(25))

#5
def check_season(month):
    month = month.strip().capitalize()
    
    if month in ["December", "January", "February"]:
        return "Winter"
    elif month in ["March", "April", "May"]:
        return "Spring"
    elif month in ["June", "July", "August"]:
        return "Summer"
    elif month in ["September", "October", "November"]:
        return "Autumn"
    else:
        return "Invalid month entered"

# Example usage:
print(check_season("march"))

#6
def calculate_slope(x1, y1, x2, y2):
    if x2 - x1 == 0:
        raise ValueError("Slope is undefined for vertical lines (division by zero).")
    return (y2 - y1) / (x2 - x1)

# Example usage:
print(calculate_slope(1, 2, 3, 4))
