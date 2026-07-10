# day 5 : lists 
# exercises : level 1 

empty_list = []
print(len(empty_list))

items = [1 , 2 , 3 , 4 , 5 , 6 , 7 , 8, 9 , 10]
print(len(items))
print(items[0])  # Print the first item
print(items[-1])  # Print the last item
print(items[len(items)//2])  # Print the middle item

mixed_data_types = ['vishva',19,5.2,False,'India']

companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print(companies)
print(len(companies))
print(companies[0])  # Print the first company
print(companies[-1])  # Print the last company
print(companies[len(companies)//2])  # Print the middle company
companies.append('Twitter')  # Add an item to the end of the list
print(companies)
companies.insert(3, 'Tesla')  # Insert an item at a specific position
print(companies)
companies[0] = 'Meta'
print(companies)
companies.insert(len(companies)//2, 'uber')
print(companies)
companies[2] = companies[2].upper()
print(companies)

print('#;' .join(companies))
print('Apple' in companies)
companies.sort()
print(companies)
companies.sort(reverse=True)
print(companies)
del companies[0:3]
print(companies)
del companies[-3: ]
print(companies)
companies.remove('Meta')
print(companies)
companies.pop(-1)
print(companies)
companies.clear()
print(companies)
del companies

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']
print(front_end)
print(back_end)
joined_list = front_end + back_end
print(joined_list)

full_stack = joined_list.copy()
index = full_stack.index('Redux')
full_stack.insert(index+1 , 'Python')
full_stack.insert(index+2 , 'SQL' )
print(full_stack)

#exercises : level 2

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print(ages)
print(min(ages))
print(max(ages))
ages.append(min(ages))
ages.append(max(ages))
print(ages)

ages.sort()
middle = len(ages)//2
median = (ages[middle-1]+ages[middle]) / 2
print(median)

avg = sum(ages) / len(ages)
print(avg)

print(max(ages)-min(ages))
print(abs(min(ages)-avg))
print(abs(max(ages)-avg))

countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
china , russia , usa , finland , sweden , norway , denmark = countries 
print(china)
print(usa)
print(denmark)






