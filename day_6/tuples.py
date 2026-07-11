# day 6 : tuples 

# exercise 1 and 2

empty_tuple = ()
sisters = ('vishva', 'ashi')
brothers = ('arsh', 'vandan')
siblings = sisters + brothers 
print(siblings)
print(len(siblings))
family_members = list(siblings)
print(family_members)
family_members.insert(4 , 'raju')
family_members.append('reeva')
print(family_members)

family_members= ['vishva', 'ashi','arsh', 'vandan','raju','reeva']
first_name,second_name,third_name,fourth_name,fifth_name,sixth_name = family_members 
print(sixth_name)

family_members = tuple(family_members)
print(family_members)

fruits = ('banana', 'apple', 'mango')
vegetables = ('tamato','patato','onion')
animal_products = ('honey','milk','eggs')
food_stuff_tp = fruits + vegetables + animal_products 
print(food_stuff_tp)
food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt)

middle_three_items = food_stuff_tp[3:6]
print(middle_three_items)

print(food_stuff_lt[ :3])
print (food_stuff_lt[-3: ])

del(food_stuff_tp)

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)

