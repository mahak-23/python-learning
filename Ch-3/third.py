# -----------------------------------------------STRINGS-------------------------------------------------------

a = 'Books' # Single quoted string
b = "Books" # Double quoted string
C = '''Books''' # Triple quoted string


# -----------------------------------------------STRING SLICING-------------------------------------------------------

name = "Books"

nameshort = name[0:3] # start from index 0 all the way till 3 (excluding 3)
print(nameshort)
character1 = name[1]
character2 = name[2]
print(character1, character2)

#       -5 -4 -3 -2 -1
#        B  o  o  k  s

print(name[-4: -1]) #ook
print(name[1:4])    
print(name[:4]) # is same as print(name[0:4])
print(name[1:]) # is same as print(name[1:5])
print(name[1:5])


# -----------------------------------------------SLICING WITH SKIP VALUE-------------------------------------------------------

word = "amazing"
word [1: 6: 2] # "mzn"    [start: end: skip]

# -----------------------------------------------STRING FUNCTIONS-------------------------------------------------------
name = "books"

print(len(name))
print(name.endswith("oks"))
print(name.startswith("Bo"))
print(name.capitalize())
print(name.count("o"))  # Books
print(name.find("ks"))  # index  -->   3
print(name.replace("o", "n"))  # Bnnks

# -----------------------------------------------ESCAPE SEQUENCE CHARACTERS-------------------------------------------------------
# Example:\n,        \t,        \',            \\         etc.
#         newline    Tab    Singlequote     backslash

a = 'John is a good boy\nbut not a bad \'boy\''
print(a)