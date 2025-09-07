# -----------------------------------------------FILE I/O-------------------------------------------------------
'''
TYPE OF FILES.
There are 2 types of files:
1. Text files (.txt, .c, etc)
2. Binary files (.jpg, .data, etc)
Python has a lot of functions for reading, updating, and deleting files.
'''

# -----------------------------------------------OPENING AND READING A FILE IN PYTHON-------------------------------------------------------
'''
a = "a very long string with emails"

emails = []
3 seconds
'''

f = open("read.txt", "r")
data = f.read()
print(data)
print("using readline")
print(f.readline()) # We can also use f.readline() function to read one full line at a time. Read one line from the file.
f.close()
 
# -----------------------------------------------MODES OF OPENING A FILE------------------------------------------
'''
r-open for reading
w-open for writing
a- open for appending
+ - open for updating.
'rb' will open for read in binary mode.
'rt' will open for read in text mode.
'''

# -----------------------------------------------WRITE FILES IN PYTHON-------------------------------------------------------

st = "Hey John you are amazing"

# f = open("write.txt", "w")
# f.write(st)
# f.close()

# -----------------------------------------------MORE FILE FUNCTIONS-------------------------------------------------------

# append
f = open("write.txt", "a")
f.write(st)
f.close()

print('------more funs----------')
f = open("read.txt")

# lines = f.readlines()
# print(lines, type(lines))

line1 = f.readline()
print(line1, type(line1))

line2 = f.readline()
print(line2, type(line2))

line3 = f.readline()
print(line3, type(line3))

line4 = f.readline()
print(line4, type(line4))

line5 = f.readline()
print(line5 =="")
line = f.readline()
while(line != ""):
    print(line)
    line = f.readline()

f.close()

# -----------------------------------------------WITH STATEMENT-------------------------------------------------------
# The best way to open and close the file automatically is the with statement.
print('---------with statement------------')
with open("read.txt") as f:
    print(f.read())
