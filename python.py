#git init -> repo bnane k baad
# git add .
#git commit -m " "
#git push

print("hello world")

age=30
Age=20

print (age)
print(Age)

a=b=c=20
#camel case
myNameIs="Avanya"
#Snake Case
My_name_Is="Sangal"
#pascal case

#unpack a collection
#A collection of values in a list, tuple ect Python allows u to extract values
fruits=["Apple","Bannana","Cherry"]
x,y,z= fruits
print(x)
print(y)
print(z)

print(myNameIs)
print(My_name_Is)

#global variable without keyword
x="awesome"


def myfunc():
       print("Pythonis"+x)

myfunc()

    #with global keyword
def myfunct():
     global x
     x="fantastic" 

myfunct()

print("Python is"+x)

#datatype-> 4 types
var1 =1        #int data type
var2 = True    #bool data type
var3= 10.023   #float data type
var4= 10+3j    #complex data type

print(var1)
print(var2)
print(var3)
print(var4)


#slicing strings
#modify strings
#upper case-> upper()
#lower case -> lower()
#remove whitespace 
#a="Hello world!"
#print(a.strip()) = returns "Hello, World!"


#reaplace string
#the replace() method replaces a string with another string 
a="hello world!"
print(a.replace("h","J"))
#split string
#the split() method returns a list when the text between the sepecified seperator becomes the list items

print(a.split(","))

#concatenation method
b="kaise ho"
c="ji"
d=b+" "+c
print(d)

#format string
#we cannot print number and string like this
age=35
txt="my name is Avanya" +age
print(txt)

