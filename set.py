#1
l1= {"Python","Java"," c","c++"}
print(l1)
#2
l1={"Prachi singh","21","female","b.tech"}
print(l1)
#3
myset= {"python","java"}
print(type(myset))
#4
t= {"java","python","c"}
if "python" in t:
    print("python is present in the set")
else:
    print("python is not present in the set")   
#5
s= {"java","python","c++","c"}
sec ={"c","c++"}
s.update(sec)
print(s)
#6
s= {"java","python","c++","c"}
mylist = ["html","css"]
s.update(mylist)
print(s)
#7
s= {"java","python","c++","c"}
s.pop()
print(s)
#8
s= {"java","python","c++","c"}
del s
#9
s= {"java","python","c++","c"}
for item in s:
    print(item) 
#10
s={10,20,30,40,50}  
print("Max",max(s))
print("Min",min(s))
