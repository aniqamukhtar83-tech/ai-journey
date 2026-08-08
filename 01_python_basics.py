# =========================
# variables, data types
# =========================
print("hellow world!")
student_name="aniqa mukhtar"
print(student_name)
x=20
y=30
z=2
sum=x+y+z
print(sum)
name="aniqa"
name2="mukhtar ahmad"
print(name+name2)
data=9.11
print(data)
type(data)
# =========================
    lists , tuple , sets
# =========================
list=[1,2,3,4,5,6]
print(list)
list2=["apple","banana","guava"]
print(list2[0]) #index
print(list2[1])
print(list2[-1])
#--------method append=add elements in list at end 
#insert middle , delete  , pop --------
list2.append("orange")
print(list2)
list2.insert(1,'grapes')
print(list2)
list2.pop()
print(list2)
list2.sort()
print(list2)
for fruit in list2:
    print(fruit)
#-------tuple ()unchangeable duplicate allow ------
colors=("red","green","blue")
print(colors)
numbers=(1,2,3,4,2,3,4,3,2,2,3,5)
print(numbers.count(2))#how many time 2 come in tuple
print(numbers.index(3))# 3 no ki index

#-----set duplicate not allow but un ordered------
my_set={1,2,3,4,5,6,7,6}
print(my_set)
my_set.remove(2)
my_set.add(8)
print(my_set)
a={1,2,3}
b={5,2,7}
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))

#------dictionary values store in pairs---------
student={
    "name":"aniqa mukhtar",
    "age" : 21,
    "course":"databases"
}
student["age"]=22#update
student["city"]='LAHORE'#add
print(student["city"])
print(student)
# =========================
operations , conditions
# ========================= 
print(2+4)
print(4-3)
print(2*5)
print(20/4)
print(15//4)#floor division intergers instead of loationg values
print(2**4)
print(2%4)#remainder

val=10
print(val)
val +=3
print(val)
#------conditional statements ---
temp=30
if temp >40:
    print("its hot weather")
else:
    print("its normal")
tem=30 #int(input("Enter the temperature:")) #user input 
if tem >40:
    print("its hot weather")
else:
    print("its normal")
age=40
#------largest of 3 no
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    print("A is largest")
elif b >= a and b >= c:
    print("B is largest")
else:
    print("C is largest")
country="pakistan"
