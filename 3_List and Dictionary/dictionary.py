"""
        1. Access key value
        2. Loop
            i. use items
            ii. Loop comprehension
        3. Add
        4. Delete
        5. 2D Dictionary
        6. Create Dictionary from an Array 
"""

info={"name":"Alamgir","id":"CE21012","Age":23}
print(info)  #{'name': 'Alamgir', 'id': 'CE21012', 'Age': 23}

# Access 
info["name"]="Alamgir Hosain"
print(info) #{'name': 'Alamgir Hosain', 'id': 'CE21012', 'Age':  23}       

# Loop
for i in info:
    print(i,info[i])
    """
    name Alamgir Hosain
    id CE21012
    Age 23

    """
 # loop with items
for key,val in info.items():
    print(key,val)

#Loop comprehension
sqrt_number={x:x**2 for x in range(5)}
print(sqrt_number) #{0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
sqrt_number.clear()
print(sqrt_number) #{}

# Add
info["cgpa"]=3.50 
info["email"]="a@gmail.com"

# Delete
del info["cgpa"]
info.pop("email") 

# 2D dictionary
infos={
    "info1":{
        "name":"Hosain",
        "dept":"CSE",
        "status":"Fail"
    },
      "info2":{
        "name":"JK",
        "dept":"CSE",
        "status":"PASS"
    }
}
print(infos["info2"])         #{'name': 'JK', 'dept': 'CSE', 'status': 'PASS'}
print(infos["info2"]["name"]) #JK
print(infos)

#Dictionary from an Array 
arr=["Alamgir","JK"]
val="Pass"
new_dict=dict.fromkeys(arr,val)
new_dict2=dict.fromkeys(arr,arr)
print(new_dict)  #{'Alamgir': 'Pass', 'JK': 'Pass'}
print(new_dict2) #{'Alamgir': ['Alamgir', 'JK'], 'JK': ['Alamgir', 'JK']}      