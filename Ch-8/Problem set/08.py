# 8. Write a python function to print multiplication table of a given number.

def table(n, i):
    
    if(i==11): 
        return
    
    print(f"{n} x {i} = {n*i}")

    table(n, i+1)

table(5, 1)