#1
T=("Python","Java","SQL","C")
print(T)
#2
T1=12
print(T1)
#3
T2=("Prachi", "singh","B.tech")
print(T2[::-1])
#4
T1=("Python","Java","SQL","C")
T2=("Prachi", "singh","B.tech")
T1,T2 = T2,T1
print(T1)
print(T2)
#5
t=(10,10,10,10)
if t.count(t[0]) == len(t):
    print("items are same")
else:
    print("items are not same")
#6
T1=(100,200,300,400)
a,b,c,d = T1 
print(a, b ,c ,d,sep =" ") 
#7
t1= (1,2,3,4,5,6)
new_tuple = t1[3:5]
print(new_tuple)
#8
t1=(('a',21),('b',37),('c',11))
sorted_tuple =tuple(sorted(t1, key=lambda x:x[1]))
print(sorted_tuple)
#9
t1=("Python",[10,20,30],(2,4,16))
print(t1[1][1])
#10
t1= (11,[22,33],44,55)
t1[1][0] =222
print(t1)
                    
  






