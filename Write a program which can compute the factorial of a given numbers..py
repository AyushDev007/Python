# Write a program which can compute the factorial of a given numbers.

def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n * fact(n-1)
    
num=int(input("Enter num: "))
factorial= fact(num)
print("The factorial is:",factorial)