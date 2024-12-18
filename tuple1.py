tuple1=("Aditya",78,"o grade",56000,"navi mumbai")
print(tuple1)

print(type(tuple1))

#slicing a tuple

print(tuple1[1:4])
print(tuple1[2:])
print(tuple1[:5])

#negative indexing
print(tuple1[-2])
print(tuple1[-1])






# another tuple example
t1=("Aditya",35,78,"o grade,35")
print(type(t1))
print(t1)

#tuple slicing 
print(t1[1:])
print(t1[:3])
print(t1[1:3])

#find length of the tuple 

print("the length of the tuple is:",len(t1))

#you can also give negative indexing.
print(t1[-2])
print(t1[-1])

#note:
#list is a collection which is ordered and changeable.
#list allows duplicate members.
#Tuple is a collection which is ordered and unchangeable.
#Tuple allows duplicate members.

t2=list(t1)
print(t2)

t2[2]="A in sports"
print(t2) 
for i in t2:
    print(i)