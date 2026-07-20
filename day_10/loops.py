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
