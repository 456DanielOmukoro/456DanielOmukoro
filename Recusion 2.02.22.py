'''
L = [1,2,3,4,5,6,7]

def factorial(n):
    if(n==1 or n==0):
        return 1
    else:
        return n * factorial(n-1)
    
print(factorial(7))

'''

L = [1234567]

def addList(L):
    if len (L)==1:
        return L[0]
    else:
        return L[0]+ addList(L[1:])
print(addList(L))
                            
                        






