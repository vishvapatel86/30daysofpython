#'day 2:30 Days of python programming'

#variables

first_name = "vishva"
last_name = "patel"
full_name = first_name + " " + last_name
country = "india"
city = "ahmedabad"
age = 20
year = 2026

is_married = False
is_true = True
is_light_on = True

#multiple variables in one line 
a , b , c = 10, 20, 30

#checking data types 

print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))

# length of variable
print(len(first_name))
print(len(last_name))
print(len(first_name) > len(last_name))
#numbers
num_one = 5
num_two = 4
total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
divison = num_one / num_two
remainder = num_one % num_two
exp = num_one ** num_two
floor_division = num_one // num_two

print("total:", total)
print("diff:", diff)
print("product:", product)
print("divison:", divison)
print("remainder:", remainder)
print("exp:", exp)
print("floor_division:", floor_division)

#circle area and circumference
r = 30 
area_of_circle = 3.14 * r ** 2
print("area_of_circle:", area_of_circle)
circum_of_circle = 2 * 3.14 * r
print("circum_of_circle:", circum_of_circle)

 # built- in input function

radius = input("Enter radius of circle: ")
area_of_circle = 3.14 * float(radius) ** 2
print("area_of_circle:", area_of_circle)

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
country = input("Enter your country: ")
age = input("enter your age:")
print("first_name:", first_name)
print("last_name:", last_name)
print("country:", country)
print("age:", age)

#python keywords
help("keywords")
