# day 9 : conditionals 
# exercise 1;

#1
age = int(input("Enter your age : "))
if age >= 18 :
   print("you are old enough to learn to drive.")  
else:
    years_left =  18-age
    if years_left == 1:
        print(f"You need {years_left} more year to learn to drive.")
    else:
        print(f"You need {years_left} more years to learn to drive.")
   

#2
my_age = 19
your_age = int(input("Enter your age: "))
if my_age == your_age:
  print("we are the exact same age!")

else:
    if your_age > my_age:
       age_difference = your_age - my_age
       if age_difference == 1:
        print(f"you are {age_difference} year older than me.")
       else:
        print(f"you are {age_difference} years older than me.")     
    else:
      age_difference = my_age - your_age
      if age_difference == 1:
        print(f"I am {age_difference} year older than you.")
      else:
        print(f"I am {age_difference} years older than you.")  

#3 
num_1 = int(input("Enter number one :"))
num_2 = int(input("Enter number two :"))
if num_1 == num_2:
   print("num_1 is equal to num_2.")
else: 
   if num_1> num_2:
      print("num_1 is greater than num_2.")
   else:
      print("num_1 is less than num_2.")  

# exercise 2 
#1
score = int(input("Enter score (0-100): "))

if 90 <= score <= 100:
    grade = "A"
elif 80 <= score <= 89:
    grade = "B"
elif 70 <= score <= 79:
    grade = "C"
elif 60 <= score <= 69:
    grade = "D"
else:
    grade = "F"

print("Grade:", grade)

#2
month = input("Enter month name: ")

if month in ("september", "october", "november"):
    print("The season is Autumn.")
elif month in ("december", "january", "february"):
    print("The season is Winter.")
elif month in ("march", "april", "may"):
    print("The season is Spring.")
elif month in ("june", "july", "august"):
    print("The season is Summer.")
else:
    print("Invalid month name.") 

#3
fruits = ["banana", "orange", "mango", "lemon"]

# Get input and normalize it to lowercase
new_fruit = input("Enter a fruit name: ").strip().lower()

# Check existence and modify list
if new_fruit in fruits:
    print("That fruit already exist in the list")
else:
    fruits.append(new_fruit)
    print("Modified list:", fruits)
