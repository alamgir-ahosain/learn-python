
# Declare a Function
def call():
    print("Hello Func")
    
call()   #call it

# Function with Parameter
def info1(name,dept):
    print("Name:",name,"Dept:",dept)
info1("Alamgir","CSE")  
    
# use default parameter
def info5(name="Default"): # always in the end
   return f"Hello {name}"

print(info5())
print(info5("Alamgir"))

# Passing any number of arguments

    # touple
def info6(*args):
    print(args)
print(info6("A","B","C"))    

    # Dictionary
def info8(**args):
    print(args)
print(info8(name="X",dept="Y"))     

# Return value
def info2(x):
    return x+10
print(info2(2))


# Return multiple value
def info3():
    name="Alamgir"
    dept="CSE"
    sid="CE21012"
    return name,dept,sid
name,dept,sid=info3()
print(name,dept,sid)


