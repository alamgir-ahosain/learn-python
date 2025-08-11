
"""
   * A closure is a function that remembers variables from its outer function, even after the   outer function has finished.
   * Remember variable form outer function,even the outer function is closed.
   * it can access and use those outer function captured variable.
   * Unlike global variables, closures capture local variables from their scope.

"""

# Proved that : Each closure has its own copy of captured variables—changes in one don't affect others.
def counter():
    cnt=0
    def inner():
        nonlocal cnt
        cnt+=1
        return cnt
    return inner

cnt1=counter()
cnt2=counter()
print(cnt1(),cnt1())   # 1 2 
print(cnt2(),cnt2())   # 1 2


# Proved that : Outer function variable will be stored
def add(x):
    def inner(y):
        return x+y
    return inner

res1=add(5)    #return inner function and remember x=5
res2=add(10)   #return inner function and remember x=10
print(res1(5)) # 10
print(res2(2)) # 12