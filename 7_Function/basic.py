
# Declare a Function
def call():
    print("Hello Func")
    
call()   #call it

# Function with Parameter
def info1(name,dept):
    print("Name:",name,"Dept:",dept)
info1("Alamgir","CSE")  
    
# use default parameter
def info2(name="Default"): # always in the end
   return f"Hello {name}"

print(info2())
print(info2("Alamgir"))

# Passing any number of arguments

    # touple
def info3(*args):
    print(args)
print(info3("A","B","C"))    

    # Dictionary
def info4(**args):
    print(args)
print(info4(name="X",dept="Y"))     

# Return value
def info5(x):
    return x+10
print(info5(2))


# Return multiple value
def info6():
    name="Alamgir"
    dept="CSE"
    sid="CE21012"
    return name,dept,sid
name,dept,sid=info6()
print(name,dept,sid)


