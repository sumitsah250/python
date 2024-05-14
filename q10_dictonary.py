dict ={
    "name":"sumit",
    "roll":44,
    "age":21,
    "marks":{
        "physics":99,
         "chemistary":89,
         "math":100
    }
}
print(dict)
dict["gender"]="male"
# print(dict)
# print(dict["marks"]["physics"])

# print(dict.keys())#returns all the keys of the directory
# print(dict.values())#returns all the values of the directory
# print(dict.items())#return all the item of the directory
print(dict.get("marks"))





