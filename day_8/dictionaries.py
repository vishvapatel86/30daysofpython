# day 8 : dictionaries 

dog = {}
dog = {
    'name' : 'Buddy',
    'color' : 'brown',
    'breed' : 'german shepherd',
    'legs' : 4,
    'age' : 3
}
print(dog)

student = {
    'first_name':'vishva',
    'last_name':'patel',
    'gender':'female',
    'age':19,
    'country':'india',
    'is_marred':False,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'city':'ahmedabad',
    'address':'naranpura'
    }
print(student)

student_len = len(student)
print(f"length of student dictionary : {student_len}")

skills_value = student['skills']
print(f"skills value : {skills_value}")
print(f"data type of skills : {type(skills_value)}")

student['interest']='singing'
student['fav_sport']='cricket'
print(student)

keys = student.keys()
print(keys)
values = student.values()
print(values)

print(student.items())

student.pop('interest')
print(student)

del student 
