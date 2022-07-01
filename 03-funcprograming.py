import functools
from functools import reduce

#map
names=['mohammad','ahmed','ali','saher']
def mytitle(x):
    return x.title()
new_names = map(mytitle,names)
print(list(new_names))

#filter
numbers=[20,100,80,25,110,50,55,18]
def bigger(x):
    if x>50:
        return True
    else:
        return False

mynumbers=filter(bigger,numbers)
print(list(mynumbers))


#reduce
numbers2=[20,100,80,25,110,50,55,18]
def mysum(x,y):
    return x+y
result = reduce(mysum,numbers)
print(result)
