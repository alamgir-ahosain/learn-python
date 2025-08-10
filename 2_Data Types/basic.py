
 #  variable don't have fixed data type 
 #  values(object) have data type which store in memory 
 # variable are just references to object in memory 
    #  x=5 ;type(5)==int
    #  type (x)-> <class,'int'>
 
 
# Integer : positive and negative
x=10 ; print(x)

# Float : decimal number
pi=3.14 ; print(pi)

s= 100.3+0.1+0.1-0.3
s2= (0.1+0.1+0.1)-0.3
print(s) #5.551115123125783e-17
print(s2) #5.551115123125783e-17
# we have to use  Decimal library
#Floating-point precision error happens because numbers like 0.1 can't be exactly represented in binary.
from decimal import Decimal
ss = Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.3')
ss2 = (Decimal('0.1') + Decimal('0.1') + Decimal('0.1') )- Decimal('0.3')
print(ss)  # Output: 0.0
print(ss2)  # Output: 0.0




# Complex : real and imaginary part
z=2+3j ; print(z)

# Boolean : True or False Value
check=True ; print(check)

# String: text ,immutable object
name="Alamgir" ; print(name)
#name[0]='B'  #TypeError: 'name' object does not support item assignment

# List : ordered,mutable
fruits=['Mango','Banana','Jack Fruit'] ; print(fruits)

# Touple : ordered , immutable
colors=('Red','Green','Blue') ; print(colors)

# Set : unique,unordered,mutable
st={1,2,3,1} ; print(st) # output : 1,2,3

# Dictionary : key value pairs,mutable
dt={'name':'Alamgir','id':'CE21012','cgpa':3.5} ; print(dt)

# None Type
val=None ; print(val) # output :None

# Bytes : immutable binary data
b = b'hello'
print(type(b))  # Output: <class 'bytes'>

# Range : sequence  ,used in loop
r=range(5) ; print(r)   # output : range(0,5)
