
            #itertools: preserve the n state of next value and  last value 
            

nums=[1,2,3,4,5]
it=iter(nums)
print(it) #<list_iterator object at 0x000002737A92B220>  reference at first position

print(it.__next__()) # 1
print(it.__next__()) # 2


# Create own object:Print 1 to 10
class TopTen:
    def __init__(self):
        self.num=1
    def __iter__(self):
        return self
    def __next__(self):
        if self.num<=10:
           val=self.num
           self.num+=1
           return val 
        else:
         raise StopIteration
     
values=TopTen()
print(values.__next__()) #1
print(values.__next__())  #2
for i in values:
    print(i)
    
    
# Dictionay as itertools
dict={'A':1,'B':2}
i=iter(dict)
print(next(i)) #A
print(next(i)) #B
# print(next(i)) #StopIteration

# Range as itertools
R=range(3)
r=iter(R)
print(next(r)) #0
print(next(r)) #1