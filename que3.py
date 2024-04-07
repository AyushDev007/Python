# With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.

mydict={}
n=int(input("Enter num to which upto add in dict: "))
for i in range(1,n+1):
    mydict[i]=i**i
print(mydict)