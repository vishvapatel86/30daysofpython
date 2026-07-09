#  day 4 : string 

concatenate_string = 'Thirty' , 'Days', 'Of' , 'Python' 
single_string = 'Thirty' +  ' '  + 'Days' +  ' '  + 'Of' +   ' '  + 'Python'
print(single_string)
 
print("coding" + " " + "for" + " " + "all")

company = "Coding For All"
print(company)
print(len(company))
print(company.upper())
print(company.lower())
print(company.capitalize())
print(company.title())
print(company.swapcase())
print(company[7:14]) 
print(company.index("Coding"))
print(company.find("Coding"))
print(company.replace("Coding", "Python"))
print(company.replace("Coding For All", "Python For All"))
print(company.split())
 
company_name = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(company_name.split(","))

print(company[0])
print(len(company)-1)
print(company[10])
print(company.index("C"))
print(company.index("F"))
print(company.rfind("l"))

sentence = "You cannot end a sentence with because because because is a conjunction"
print(sentence.index("because"))
print(sentence.find("because"))
print(sentence.rindex("because"))

start = sentence.find("because")
end = start + len("because because because")
print(sentence[start:end])

print(sentence.find("because"))

print(company.startswith("Coding"))
print(company.endswith("Coding"))
print("   Coding For All      ".strip())
print("30Daysofpython".isidentifier())
print("thirty_days_of_python".isidentifier())

list=["Django", "Flask", "Bottle", "Pyramid", "Falcon"]
print("#".join(list))
print("I am enjoying this challenge.\nI just wonder what is next.")
print("Name\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki")

radius = 10
area = 3.14 * radius ** 2
print(f'The area of a circle with radius{radius} is {area} meters square.')

a = 8
b = 6 
print(f"{a} + {b} = {a+b}")
print(f"{a} - {b} = {a-b}")
print(f"{a} * {b} = {a*b}")
print(f"{a} / {b} = {a/b}")
print(f"{a} % {b} = {a%b}")
print(f"{a} // {b} = {a//b}")
print(f"{a} ** {b} = {a**b}") 
