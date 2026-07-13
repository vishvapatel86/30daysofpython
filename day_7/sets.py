# day 7 : sets 

# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print(len(it_companies))
it_companies.add('twitter')
print(it_companies)
it_companies.update(["Tesla","Netflix","Intel"])
print(it_companies)
it_companies.remove("Tesla")
print(it_companies)

# remove() raises an error if the item is not found.
# discard() does not raise an error if the item is not found.

print(A.union(B))
print(A.intersection(B))
print(A.issubset(B))
print(A.isdisjoint(B))
print(A.union(B))
print(B.union(A))
print(A.symmetric_difference(B))
del A
del B

age_set = set(age)

print(len(age))
print(len(age_set))

# String: Ordered sequence of characters, immutable.
# List: Ordered collection, mutable, allows duplicates.
# Tuple: Ordered collection, immutable, allows duplicates.
# Set: Unordered collection, mutable, does not allow duplicates.

sentence = "I am a teacher and I love to inspire and teach people."

words = sentence.replace(".", "").split()
unique_words = set(words)

print(unique_words)
print(len(unique_words))
