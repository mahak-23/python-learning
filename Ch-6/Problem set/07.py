# 7. Write a program to find out whether a given post is talking about "John" or not.

post = input("Enter post: ")


if("john" in post.lower()):
    print("This post is talking about john")

else:
    print("This post is not talking about john")