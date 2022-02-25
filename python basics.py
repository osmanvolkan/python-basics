from pickle import FALSE
from re import T
from xmlrpc.server import SimpleXMLRPCDispatcher


print ("Osman Volkan")
print("o----")
print(" ||||")
print("*"*10)
price=10
price=20
rating=4.9
name="Mosh"
is_published=False 
print(price)
name="John Smith"
age=20
is_new_patient=True
name=input("What is your name? ")
print("Hi "+ name)
color=input("Whats your favourite color? ")
print(name+ " likes "+color)
birth_year=input("Birth year: ")
print(type(birth_year))
int(age)
print(type(birth_year))
age=2022-birth_year
print(age)
weight=input("How many pounds are you weight? ")
float(weight)
kilo=weight*0.45
print("Your weight is "+kilo +" kilograms")
course= "Python for Beginners"
print(course)
course= 'Python for Beginners'
print(course)
course= '''Python for Beginners
        Welcome to our course
        
        Best of luck
                    Osman'''
print(course)
course= "Python for Beginners"
    
print(course[0])
print(course[-1])
print(course[-2])
print(course[0:3])
print(course[:5])
print(course[3:])
print(course[:])
another=course[:]
print(another)
first="John"
last="Smith"
message=first+" ["+last+"] is a coder"
print(message)
msg=f"{first} [{last}]is a coder"
print(msg)
course="Python for Beginners"
print(len(course))
course.upper()
course.lower()
print(course.upper())
print(course.lower())
print(course.find("P"))
print(course.find("o"))
print(course.find("O"))
print(course.find("Beginners"))
print(course.replace("Beginners","Absolute Beginners"))
print("Python" in course)
print(10/3)
print(10//3)
print(10%3)
print(10**3)
x=10
x=x+3
print(x)
x+=3
print(x)
x-=3
x=10+3*2
print(x)
x=2**3
x=2*3/2
x=3+2-3
x=2.9
print(round(x))
x=2.9
print(abs(-2.9))
import math
print(math.ceil(2.9))
print(math.floor(2.9))
is_hot=False
is_cold=True
if is_hot:
        print("Its a hot day")
        print("Drink plenty of water")
elif is_cold:
        print("Its a cold day")
        print("Wear warm clothes")
else:print("Its a lovely day")

print("Enjoy your day!")

price=1000000
credit_good=True
if credit_good:
        print("You must pust down "+price*0.1)
else:
        print("you must pay "+price*0.2)

has_high_income=True
has_good_credit=True
if has_high_income and has_good_credit:
        print("Eligible for loan")

has_high_income=False
has_good_credit=True
if has_high_income or has_good_credit:
        print("Eligible for loan")

has_high_income=True
has_criminal_record=False
if has_high_income or not has_criminal_record:
        print("Eligible for loan")

temperature=30

if temperature>30:
        print("Its a hot day")
else:
        print("Its not a hot day")

name=input("write your name")
if len(name)<3:
        print("name too short")
elif len(name)>50:
        print("name too long")        
else: print("name looks good")

weight=float(input("weight: "))
convert=input("(L)bs or (K)g:")
if convert.upper=="K":
        weight=weight/0.45
        print(f"you are {weight} pounds")
else:
        weight=weight*0.45 
        print(f"you are {weight} kilos")

i=1
while i<=5:
        print(i)
        i=i+1
print("Done")

i=1
while i<=5:
        print("*" * i)
        i=i+1
print("Done")  

secret_number=9
guess_count=0
guess_limit=3
while guess_count<guess_limit:
        guess=int(input("Guess "))
        guess_count+=1
        if guess==secret_number:
                print("you won")
                break
else:
        print("you failed")


command=""
started=False
while True:
        command=input("> ").lower
        if command=="help":
                print("""
                start - to start the car
                stop - to stop the car
                quit - to exit game
                """)
        elif command=="start":
                if started:                 
                        print("the car is already started")
                else:
                        started=True
                        print("the car has started")

        elif command=="stop":
                if not started:
                        print("car is already stopped")
                else:
                        started=False
                        print("the car has stopped")
                
        elif command=="quit":
                break
        else:
                print("bad command")


for item in "Python":
        print(item)
for item in [1,2,3,4]:
        print(item)
for item in range(10):
        print(item)
for item in range(5,10,2):
        print(item)

prices=[10,20,30]
total=0
for i in prices:
        total=total+i
print(f"Total: {total}")

for x in range(4):
        for y in range(3):
                print(f"({x},{y}")

numbers=[5,2,5,2,2]
for i in numbers:
        print(i*"x")

numbers=[5,2,5,2,2]
for x_count in numbers:
        output=""
        for output in range(x_count):
                output+="x"
        print(output)

names=["John","Bob","Mosh","Sarah","Mary"]
print(names)
print(names[0])
print(names[-1])
print(names[2:])
print(names[:])
names[0]="Jon"

numbers=[3,6,2,8,4,10]
max=numbers[0]
for i in numbers:
        if i>number:
                number=i
print(max)

matrix=[
 [1,2,3],
 [4,5,6],
 [7,8,9]
]
matrix[0],[0]

for row in matrix:
       for item in row:
               print("item")


numbers=[5,2,1,7,4]
numbers.append(20)
print(numbers)
numbers.insert(0,10)
print(numbers)
numbers.remove(4)
print(numbers)
numbers.pop()
print(numbers)
print(numbers.index(5))
print(numbers.index(50))
print(50 in numbers)
print(numbers.count(5))
numbers.sort()
numbers.reverse()
numbers2=numbers.copy()
print(numbers)
print(numbers2)
numbers.clear()
print(numbers)


numbers=[1,2,3,5,2,7,5,6,3,2,9,4,8,9,5,7,8,9,4,6,8,9]
uniques=[]
for number in numbers:
        if number not in uniques:
                uniques.append(number)
print(uniques)

numbers=(1,2,3)
numbers[0]
print(numbers.count(2))
numbers.index(2)

coordinates=(1,2,3)
x=coordinates[0]
y=coordinates[1]
z=coordinates[2]
x,y,z = coordinates
print(y)
coordinates=[1,2,3]
x,y,z = coordinates
print(y)

Customer={
        "name":"John Smith",
        "age":30,
        "is_verified":True
}        
print(Customer["name"])
print(Customer.get("birthdate","Jan 5 1990"))
Customer["birthdate"]="Jan 1 1980"
Customer["name"]="Jack Smith"

phone=input("Phone number> ")
digits_mapping={"1":"one","2":"two","3":"three","4":"four"}

output=""
for ch in phone:
       output += digits_mapping.get(ch,"!")+" "
print(output)
























































