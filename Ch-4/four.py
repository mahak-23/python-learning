# -----------------------------------------------LISTS AND TUPLES-------------------------------------------------------
friends = ["Apple", "Orange", 5, 345.06, False, "Aakash", "Rohan"]
print(type(friends))

# -----------------------------------------------LIST INDEXING-------------------------------------------------------
print(friends[0])
friends[0] = "Grapes" # Unlike Strings lists are mutable

print(friends[0])
print(friends[1:4])

# -----------------------------------------------LIST METHODS.-------------------------------------------------------

print(friends)
friends.append("John")
print(friends)

l1 = [1, 34,62, 2, 6, 11]
l1.sort()
l1.reverse()
l1.insert(2, 333333) # Insert 333333 such that its index in the list is 3
print(l1)
value = l1.pop(3)
print(value)

l1.remove(2)
print(l1)

# -----------------------------------------------TUPLES IN PYTHON-------------------------------------------------------
a = () # empty tuple
a = (1,) #tuple with only one element needs a comm
a = (1,45,342,3424,False, "Rohan", "Shivam") # tuple with more than one element
print(a)
print(type(a))


# -----------------------------------------------TUPLE METHODS-------------------------------------------------------
no = a.count(45)
print(no)

i = a.index(3424)
print(i)

print(len(a))