names=['ahmed','ali','mohammad','mahmood']
new_name=[]
for name in names:
    new_name.append(name.title())

print(new_name)


#list comperhension
new_names2 =[x.title() for x in names  ]
print(new_names2)


for i in range(5):
    for j in range(3):
        print(i,j)


numbers = [  (i,j) for i in range(5)   for j in range(3)  ]
print (numbers)


#condition in list comperehension

even = [i for i in range(1,100+1) if i%2==0 ]
print(even)


#condition in list comperehension(else)

even2 = [i if i%2==0 else 0 for i in range(1,100+1)  ]
print(even2)


#Enumerate
names3=['ahmed','ali','mohammad','mahmood']
for index, name in enumerate (names3):
    if index ==2:
        print("in tow")
    print(f"{index}: {name}")
