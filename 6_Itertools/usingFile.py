

f = open(r"E:\typeOFlanguage\python\learn-python\6_Iterator\text_file.txt")
# f.iter()  ;  by defult its implemented

# When open the file ,by default it has iter
# When open a file in Python, the file object is already an iterator over its lines.
if iter(f) is f  and iter(f) is f.__iter__()  :
    print("True")  

  
print(f.readline()) #Name:Alamgir Hosain ,pointer moves to line 2
print(f.__next__()) #Dept:CSE ,pointer moves to line 3
print(f.__next__()) #ID:CE21012 ,pointer moves to line 4
# print(f.__next__())  #StopIteration
print(f.readline()) #  tries to read line 4, but file might already be done or empty — pointer moves to end.

f.seek(0)  # Go back to start of file
while True:
    line=f.readline()
    if not line:
        break
    print(line,end=' ')


  
    
f.close()

