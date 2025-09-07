# 8. Write a program to make a copy of a text file "this.txt"
with open("../files/this.txt") as f:
    content = f.read()

with open("../files/this_copy.txt", "w") as f:
    f.write(content)