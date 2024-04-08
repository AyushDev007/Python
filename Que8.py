# Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
# Suppose the following input is supplied to the program:
# without,hello,bag,world
# Then, the output should be:
# bag,hello,without,world

mylist=[]
x=input("Enter words using comma: ")
spl=x.split(",")
for i in range(len(spl)):
    mylist.append(spl[i])
    mylist.sort()
print(mylist)
