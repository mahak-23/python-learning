# 9. Write a program to find out whether a file is identical & matches the content of another file.
with open("../files/this.txt") as f:
    f1 = f.read()

with open("../files/this_copy.txt") as f:
    f2 = f.read()

isIdenticle = f1 == f2

print(f"Files identicle: {isIdenticle}")