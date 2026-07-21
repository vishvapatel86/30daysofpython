# day 10 : loops 

# exercise 1 
#Iterate 0 to 10 Using a For Loop
for i in range(11):
    print(i)
#Iterate 0 to 10 Using a While Loop
i = 0
while i <= 10:
    print(i)
    i += 1
#Iterate 10 to 0 Using a For Loop
for i in range(10, -1, -1):
    print(i)
#Iterate 10 to 0 Using a For Loop
i = 10
while i >= 0:
    print(i)
    i -= 1

#Seven Calls to print() to Draw a Triangle
for i in range(1, 8):
    print("#" * i)

# Creates a 6x6 grid of '#' characters
for i in range(6):
    for j in range(6):
        print("#", end=" ")
    print()

# Iterates from 0 to 10 to print formatted multiplication equations
for i in range(11):
    print(f"{i} x {i} = {i * i}")

#Iterate through a list
tech_list = ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']

for item in tech_list:
    print(item)

#Print only even numbers (0 to 100)

for i in range(101):
    if i % 2 == 0:
        print(i, end=" ")

#Print only odd numbers (0 to 100)
for i in range(101):
    if i % 2 != 0:
        print(i, end=" ")
  
  