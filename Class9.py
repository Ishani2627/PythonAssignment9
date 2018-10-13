#Que1
print("exception handling \n")
a=3
try:
    if(a<4):
        a = a/(a-3)
        print(a)
except ZeroDivisionError:
    print("Divide by Zero")
print("\n")

#Que2
print("exception handling \n")
l = [1,2,3]
try:
    print(l[3])
except IndexError:
    print("Out of Range")
print("\n")

#Que4
#Function which returns a/b
def AbyB(a , b):
    try:
        c = ((a+b) / (a-b))
    except ZeroDivisionError:
        print("a/b result in 0")
    else:
        print(c)
    
# Driver program to test above function
AbyB(2.0, 3.0)
AbyB(3.0, 3.0)

#OUTPUT
#-5.0
#a/b result in 0
print("\n")

#Que5
print("import, value and index error \n")
l = [1,2,3]
try:
    import acadview
    print(l[3])
    def value(self, string, char):
        if (string[i] == char):
            return i
    value('bababa','a')  
except:
    print("An exception and there is no such type of module, import error")
    print("Out of range, index error")      
    print("error, please enter correct type of value, value error")
print("\n")

#Que3
#Program to depict raising exception
try:
    raise NameError("Hi there")     #Raise error
except NameError:
    print("An exception")
    raise       #To determine whether the exception was raised or not
print("\n")

#OUTPUT
#An exception
#
# NameError