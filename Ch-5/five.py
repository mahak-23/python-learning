# -----------------------------------------------DICTIONARY & SETS-------------------------------------------------------
d = {} # Empty dictionary
marks = {
    "John": 100,
    "Shubham": 56,
    "Rohan": 23,
    0: "John",
}

print(marks, type(marks))
print(marks["John"])

# -----------------------------------------------PROPERTIES OF PYTHON DICTIONARIES-------------------------------------------------------
# 1. It is unordered.
# 2. It is mutable.
# 3. It is indexed.
# 4. Cannot contain duplicate keys.

# -----------------------------------------------DICTIONARY METHODS-------------------------------------------------------

print(marks.items())
print(marks.keys())
print(marks.values())
marks.update({"John": 99, "Renuka": 100})
print(marks)

print(marks.get("John2")) # Prints None
# print(marks["John2"]) # Returns an error KeyError: 'John2'


# -----------------------------------------------SETS IN PYTHON-------------------------------------------------------
e = set() # Dont use s = {} as it will create an empty dictionary
s = {1, 5, 32, 54,5, 5, 5, "John"}
print(type(e))
print(s)

# -----------------------------------------------PROPERTIES OF SETS-------------------------------------------------------
# 1. Sets are unordered => Element's order doesn't matter
# 2. Sets are unindexed => Cannot access elements by index
# 3. There is no way to change items in sets.
# 4. Sets cannot contain duplicate values.

# -----------------------------------------------OPERATIONS ON SETS-------------------------------------------------------

print(s, type(s))

s.add(566)
print(s, type(s))
s.remove(1)
print(s, type(s))

s1 = {1, 45, 6, 78}  
s2 = {7, 8, 1, 78}
print(s1.union(s2))
print(s1.intersection(s2))