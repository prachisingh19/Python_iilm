#1
d = {"name": "Prachi", "age": 21, "gender": "Female", "education": "B.Tech"}
print(d)
#2
print(d["name"])
#3
print(d.values())
#4
d["age"] = 22
print(d)
#5
for key in d:
    print(key, ":", d[key])
#6
d= {"d1":{"name":"A","age":"20"},"d2":{"name":"B","age":"30"},"d3":{"name":"C","age":"40"}}
print(d)
#7
d1 = {"age": 20}
d2 = {"age": 21}
final_dict = {"dict1":d1, "dict2":d2}
print(final_dict)
#8
d1=["name","age","gender"]
d2=["Prachi","21","Female"]
final_dict = dict(zip(d1,d2))
print(final_dict)
#9
d1 = {"a":1, "b":2 }
d2 = {"b":3, "c":4 }
d1.update(d2)
print(d1)
#10
sample_dict = {"emp1": {"name": "John", "salary": 7500},
               "emp2": {"name": "Emma", "salary": 8000}}
min_key = min(sample_dict, key=lambda k: sample_dict[k]['salary'])
print("Employee with minimum salary:", min_key) 