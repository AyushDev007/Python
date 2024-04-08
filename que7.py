# Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i*j.

L=[]
R=int(input("Enter Row: "))
C=int(input("Enter Column: "))
for i in range(R):
    row=[]
    for j in range(C):
        num=int(input("Enter value: "))
        row.append(num)
    L.append(row)

print(L,end=" ")

# for i in range(R):      
#     for j in range(C):
#         print(L[i][j],end=" ")
#     print()
