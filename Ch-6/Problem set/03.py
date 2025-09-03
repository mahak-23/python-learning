# 3. A spam comment is defined as a text containing following keywords: "Make a lot of money", "buy now", "subscribe this", "click this". Write a program to detect these spams.

k1 = "Make a lot of money"
k2 = "buy now"  
k3 = "subscribe this"  
k4 = "click this"

message = input("Enter your comment: ")

if((k1 in message) or (k2 in message )or (k3 in message) or (k4 in message)):
    print("This comment is a spam")

else:
    print("This comment is not a spam")