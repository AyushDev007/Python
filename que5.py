# Define a class which has at least two methods: getString: to get a string from console input
# printString: to print the string in upper case.
# Also please include simple test function to test the class methods.

def getstring():
    string= input("enter string: ")
    printstring(string)
    
def printstring(string):
    print(string.upper())
    
print("Do you want to enter string")
ch=input("Enter Y/N: ")
if ch == "Y":
    getstring()
elif ch == "N":
    print("Thank you for using program")
else:
    print("wrong choice!")
