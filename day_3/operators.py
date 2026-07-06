# day 3 : operators 

age = 20
height = 5.2
complex_number = 4 + 4j

#enter base and height of the triangle and calculate an area of this triangle.
base = float(input("Enter base:"))
height = float(input("Enter height:"))
area = 0.5 * base * height
print("The area of the triangle is:", area)

#enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle.
side_a = float(input("Enter side a:"))
side_b = float(input("Enter side b:"))
side_c = float(input("Enter side c:"))
perimeter = side_a + side_b + side_c
print("The perimeter of the triangle is:", perimeter)

 # area and perimeter of rectangle
length = float(input("Enter length of rectangle:"))
width = float(input("Enter width of rectangle:"))
area = length * width                    
print("The area of the rectangle is:", area)

perimeter = 2 * (length + width)
print("The perimeter of the rectangle is:", perimeter)

# area and circumference of circle
pi = 3.14
r = float(input("Enter radius of circle:"))
area = pi * r ** r 
print("The area of the circle is:", area)
circumference = 2 * pi * r
print("The circumference of the circle is:", circumference)

#Calculate the slope, x-intercept and y-intercept of y = 2x -2
slope = 2
x_intercept = 1
y_intercept = -2
print("The slope is:", slope)
print("The x-intercept is:", x_intercept)
print("The y-intercept is:", y_intercept)

#Find the slope and Euclidean distance.
x1 , y1 = 2 , 2
x2 , y2 = 6 , 10
slope = y2 - y1 / x2 - x1
print("The slope is:", slope)
distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
print("The Euclidean distance is:", distance)
 
#compare the slopes in tasks 8 and 9.
if slope == 2:
    print("The slopes are equal.")
else:
    print("The slopes are not equal.")  

#Calculate the value of y. and check at what x value y is going to be 0.

for x in range(-5 , 6):
    y = x*2 + 6*x + 9
    print("x:", x, "y:", y)

#comparison operators.
print(len("python") > len("dragon"))
print("on" in "python" and "dragon")
print("jargon" in " i hope this course is not full of jargon")
print("on" not in "python" and "dragon")
  
print(len("python"))
print(float(len("python")))
print(str(len("python")))

# check if number is even or not .
number = int(input("Enter a number:"))
if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

#check.
print(7 // 3 == int(2.7))
print(type('10') == type(10))
print(int(float('9.8'))== 10)

#Calculate pay of the person.
hours = float(input("Enter hours:"))
rate = float(input("Enter rate per hour:"))
pay = hours * rate
print("your weekly earnings:", pay)

#Calculate the number of seconds a person can live.
years = int(input("Enter number of years you have lived:"))
seconds = years * 365 * 24 * 60 * 60
print("You have lived for", seconds, "seconds.")

#Python script that displays the following table
for i in range(1, 6):
    print(i, 1, i, i**2, i**3)
    
