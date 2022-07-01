#readable
#comment :  Developers

class Clac:
    def __init__(self):
        print("Welcome")

    def sum (self,x,y):
        #return the sum of x,y
        return x+y # BUG: return the sum of x,y
                    #HOTFIX: return the sum of x,y
                    #TODO: return the sum of x,y



#documentation :  User , manual
class Clac:
    ''' class for for clac '''
    def __init__(self):
        print("Welcome")

    def sum (self,x,y):
        '''
            simple function to sum 2 value [x,y]
            input:
                x: int
                y: int
            output :
                 int
        '''
        
        return x+y

c=Clac()
print(help(c))


#documentation ---> type Hints
def mysum(x:int,y:int)->int:
    result=x+y
    return result
v= mysum(5,10)
print(v)





