"""
        1. Create
        2. Replace
        3. Insert
        4. Delete 
        5. Add
        6. Loop
        7. Loop Comprehension
        8. Copy

"""
# ----------- Create -----------
ls1 = ["Mango", "Apple", "Banana", "Jack Fruit"]
print(ls1)      # ['Mango', 'Apple', 'Banana', 'Jack Fruit']
print(ls1[1:3]) # ['Apple', 'Banana']

# ----------- Replace -----------
ls1[1] = "Orange"
print(ls1)      # ['Mango', 'Orange', 'Banana', 'Jack Fruit']

ls1[1:2] = "AB "
print(ls1)      # ['Mango', 'A', 'B', ' ', 'Banana', 'Jack Fruit']

ls1[1:2] = ["Litchi"]
print(ls1)      # ['Mango', 'Litchi', 'B', ' ', 'Banana', 'Jack Fruit']

ls1[2:3] = ["Coconut", "Pinaple"]
print(ls1)      # ['Mango', 'Litchi', 'Coconut', 'Pinaple', ' ', 'Banana', 'Jack Fruit']

# ----------- Insert -----------
ls1[1:1] = ["test", "test"]
print(ls1)      # ['Mango', 'test', 'test', 'Litchi', 'Coconut', 'Pinaple', ' ', 'Banana', 'Jack Fruit']

# ----------- Delete -----------
ls1[3:9] = []
print(ls1)      # ['Mango', 'test', 'test']

ls1.pop()
print(ls1)      # ['Mango', 'test']

ls1.remove("test")
print(ls1)      # ['Mango']

# ----------- Add -----------
ls1.append("Banana")
print(ls1)      # ['Mango', 'Banana']

ls1.insert(1, "Mango")
print(ls1)      # ['Mango', 'Mango', 'Banana']

# ----------- Loop -----------
for fruit in ls1:
    print(fruit, end="-")   # Mango-Mango-Banana-
print()  # For newline

# ----------- Loop Comprehension -----------
num = [x**2 for x in range(4)]
print(num)      # [0, 1, 4, 9]

# ----------- Copy -----------
ls2 = ls1        # Same memory reference
print(ls2)       # ['Mango', 'Mango', 'Banana']

ls3 = ls2.copy() # Different memory reference
print(ls3)       # ['Mango', 'Mango', 'Banana']
