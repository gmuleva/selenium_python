a = 20
print(type(a))# integer data type is used to store integer value

print("************************************************************************")

b = 20.9
print(type(b)) #float datatypes is used to store float value

print("************************************************************************")

c = {"age":20,"name":"jay"}
print(type(c)) # dict data type is value to use key value pair values ,dictionary is mutable hence we can change edit the values inside the dictionary
c["age"] = 23
print(c) #updating dictionary value
print("************************************************************************")

d = ["harish","gourav",20]
print(type(d))
d[0] = "jay"
print(d)
d.append("aaditya")
print(d)
d.remove("jay")
print(d)

print("************************************************************************")

e = "gourav"
print(type(e))

print("************************************************************************")


f = True
print(type(f))

print("************************************************************************")

g = {1,2,3}
print(type(g))

print("************************************************************************")

h = None
print(type(h))

print("************************************************************************")

i = ("name","age","rollno")
print(type(i))

print("************************************************************************")
print("we can store list inside tuple see how,tuple is immutable but we can change the value of list inside tuple")

tup = (1,2,3,[4,5])
tup[3][1] = "gourav"
print(tup)

print("_________________________COMPLETED__________________________________________________")
