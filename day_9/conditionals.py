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
