"""
LEGB Rule :Order in which Python looks for a variable:
    L – Local: Inside the current function.
    E – Enclosing: In the outer (enclosing) function’s scope (for nested functions).
    G – Global: Defined at the top level of the current file/module.
    B – Built-in: Python’s built-in names (e.g., len, print).

"""
 
name="Outer"
def func():
    name="Inner"
    print(name)

print(name) # outer
func()      # inner


#Example :Level
val=10 # global scope
def outer():
    val=15 # enclosing scope
    def inner():
        val=20 #local scope
        return val
    return inner
x=outer()
print(x()) # 20


# Modifies the enclosing scope variable
def outer2():
    num=10
    def inner():
        nonlocal num
        num+=2
        return num
    return inner
x2=outer2()
print(x2()) # 12
        
