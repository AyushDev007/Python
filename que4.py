# Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.

n=int(input("Enter numbers you want: "))
L=[]
T=()
for i in range(1,n+1):
    num=int(input("Enter num: "))
    L.append(num)
    temp=list(T)
    temp.append(num)
    T=tuple(temp)
print(L)
print(T)
