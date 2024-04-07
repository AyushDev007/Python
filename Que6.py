# Write a program that calculates and prints the value according to the given formula:
# Q = Square root of [(2 * C * D)/H]
# Following are the fixed values of C and H:
# C is 50. H is 30.
# D is the variable whose values should be input to your program in a comma-separated sequence.

import math
L=[]
Ans=[]
C=50
H=30
print("Calculation using formula Square root of [(2 * C * D)/H]")
n=int(input("Enter how many values of D will be given: "))

for i in range(1,n+1):
    D=int(input("Enter the value of D: "))
    L.append(D)

for i in range(len(L)-1):
    print(L[i],end=",")
print(L[-1])

for i in range(0,len(L)):
    calc=math.sqrt((2*C*L[i])/H)
    ans=int(calc)
    Ans.append(ans)

for i in range(len(Ans)-1):
    print(Ans[i],end=",")
print(Ans[-1])
