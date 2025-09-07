# Learning python from scratch

print("Hello World!") #no use of semicolon
print("I'm Avanya") #only print not printf

# comma s same line mai code ate hai
print("My age is 18."," Currently pursuing b.tech")

#all operations like addition subtraction are allowed in python
print(19)
print(18+2)

#variables , kisi string y words ko likhna hai then double quotes k andar
name="Avanya" 
#strings ko single,double and triple .. teeno quotes s denote kr skte hai!
#but commonly double quote s krenge
age=18
price=25.99
print(name)
print(age)
print(price)
print("My name is :",name)

# type likhne s dataype k pta chlta hai
print(type(name))
print(type(age))
print(type(price))

#Datatypes -> 1)Integers ,2)String, 3)Float, 4)Boolean, 5)None
old=True
a=None
print(type(old))
print(type(a))

#Arithmetic Operators
a=5
b=2
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b) #for remainder
print(a**b) #for a^b

#Relational Operators
a=50
b=20
print(a==b) #false
print(a!=b) #true
print(a>=b) #true
print(a>b) #true

#Assignment operators
#num=num+10
#num+=10  , both works same here
#this works same for all operators

#Logical Operators -> not , and ,or
print(not False)
print(not True)
# and operator ->dono notes true hone chaiye tbhi true ayega
#or operator -> ek value true hogi tb bhi true ayega

#Type Conversion-> automatic Conversion
a=2
b=3.4
sum=a+b #it automaticalyy give the output in the form of float
 
 #Type Casting-> Manual Conversion
a=1
b="2"
c=int(b) #string ko int mai convert kiya
sum=a+c

#input in python
#name=input("Enter your name:")
#print("Welcome",name)

#prgrm to input 2 num and print their sum
#first=int(input("First:"))
#second=int(input("Second:"))
#print("sum=",first+second)

#prgrm for area of square
#side=int(input("Side:"))
#area=print(side*side)

#prgrm for average of 2 floating number
#a=float(input("a:"))
#b=float(input("b:"))
#average=print((a+b)/2)

#boolean prgrm
a=int(input("a:"))
b=int(input("b:"))
print(a>=b)