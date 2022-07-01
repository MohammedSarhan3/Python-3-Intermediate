import functools
from functools import reduce

#map
names=['mohammad','ahmed','ali','saher']
def mytitle(x):
    return x.title()
new_names = map(mytitle,names)
print(list(new_names))
