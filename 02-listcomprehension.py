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
