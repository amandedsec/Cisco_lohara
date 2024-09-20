"""print(sum([10,20,30]))

def find_sum(first, second, *others):
    s = first + second
    if(len(others)>0):
        for num in others:
            s += others[KeyboardInte]
        #end for
    return s
print(find_sum(10,20))#30
print(find_sum(10,20,30,40))#110
print(find_sum(10,20,30,40,50))#150"""

# def find_diff(a=1, b= 0):
def find_diff(a:int=1, b:int= 0)-> int:
    return a-b

print(find_diff (20,10))#10
print(find_diff (b=10,a=20))#10
print(find_diff (b=10))#-9
print(find_diff ())#1
print('==========================================================')

# ===================================================================================

def change_name(names, index, name):
    names [index] = name
    
names = ['rahul', 'modi']
print (names)

change_name (names,1,'modiji')
print(names)
print('==========================================================')

# ===================================================================================

def find_sum(first, second, *others):
    s = first + second
    if(len(others) > 0):
        for num in others:
            s += num
        # end for
    # end if
    return s
print(find_sum (20,10))#30
print(find_sum (first=50,second=40,))#90
print(find_sum (10,20,30,))#60
print('==========================================================')

# ===================================================================================

def find_sum(a,b, **others):
    s = a+b
    if(len(others) > 0):
        for key in others:
            s += others[key]
        # end for
    # end if
    # print (type(others))
    return s
print(find_sum (a=10,b=20))#30
print(find_sum (a=50,b=40,c=50))#90
print(find_sum (a=50,b=40,c=50, d=10))#60
print('==========================================================')


# ================================================================
def fact (N):
    if N <= 1:
        return 1
    # end if
    return N * fact(N-1)

print(fact(5))
print(fact(4))
print('==========================================================')

#_______________________________________________


import math
def isprime(num):
    sqrt_num = int(math.sqrt(num))
    for i in range(2,sqrt_num+1):
        if num%i==0:
            return "Not a prime number"
        #end if
    #end for
    return "Prime Number"

num = int(input())
print(isprime(num))



