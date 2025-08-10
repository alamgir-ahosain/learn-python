
"""
__________Topic List__________

1. Slice
2. Convert Upper and Lower Case
3. use str,repr,print
4. Replace
5. Convert String to List
6. Convert List to String
7. Find
8. Count
9. String Format
10. Double Quota
11. SKip new Line
12. Check using Reference
12. Print using Loop
"""

# slice
str1="0123456789"
print(str1[:])    #0123456789
print(str1[3:])   #3456789
print(str1[:7])   #0123456
print(str1[2:7])  #23456
print(str1[0:7:2])#0246 increment by 2

# upper and lower
str2="Alamgir Hosain"
print(str2.lower()) #alamgir hosain
print(str2.upper()) #ALAMGIR HOSAIN


# str,repr and print 
str3=" With Space "
print(str(str3)) #  With Space 
print(repr(str3))#' With Space '
print(str3)      # With Space

# Replace
str4="replace string"
print(str4.replace("string","newString")) #replace newString

# string to List
str5="Mango,Apple,Jack Fruit"
# spilt on whitepace(spaces,tabs ,newline) . so Mango ,Apple,Jack as one word and Fruit is another word
print(str5.split()) #['Mango,Apple,Jack', 'Fruit'] 

# spilt with comma
print(str5.split(",")) #['Mango', 'Apple', 'Jack Fruit'] 

# List to string
list1=["Mango","Apple","Jack Fruit"]
print("".join(list1))   #MangoAPpleJack Fruit
print(" ".join(list1))  #Mango Apple Jack Fruit
print(", ".join(list1)) #Mango, Apple, Jack Fruit

# Find 
str6="Alamgir Hosain"
print(str6.find("Hosain")) #8,starting index
print(str6.find("alamgir")) #-1 ,not dound

# Count
str7="Alamgir Hosain Hosain"
print(str7.count("Hosain")) #2


# String Format ,{}-> Place Holder
country="Bangladesh"
me="I"
str8="{} Love {}"
print(str8.format(me,country)) # I Love Bangladesh

# Double Quote
str9="He said , \"You are the Best\"" #He said, "You are the Best"
print(str9)

# Skip New Line
str10="Alamgir\nHosain"  
str11=r"Alamgir\nHosain" # r->raw string
print(str10) #Alamgir Hosain
print(str11) #Alamgir\nHosain

# Check using
str12="Alamgir Hosain"
print("Hosain" in str12) #True
print("checkPart" in str12)     #False

#Print with  Loop
str15="Alamgir Hosain"
for letter in str15:
    print(letter)
