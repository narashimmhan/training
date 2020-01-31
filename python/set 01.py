1. 
x=int(input())
y=int(input())
z=int(input())
if x%2 != 0 and x > y and y > z:
    print("x is the large")
elif y%2 != 0 and y > z and z > x:
    print("y is the large")
elif z%2 != 0 and z > y and y > x:
    print("z is the large")
elif x%2 == 0 or y%2 == 0 or z%2 == 0:
    print("even")

2.    
def right_justify(s):
    print (s.rjust(65))    

right_justify('cigna')


3.
a = []
b = []
for i in range(0,5):
    aa=int(input())
    if(aa%2==0):
        a.append(aa)
    else:
        b.append(aa)
if(len(b)==0):
    print("add odd no")
else:
    b.sort()
    b.reverse()
    print(b[0])

4.
import math
a = int(input())
b=(4*math.pi*a*a*a)/3
print(b)

5.
import math
a=int(input())
for pwr in range(1,6):
    aa = (a ** (1.0/pwr))
    if math.ceil(aa) == aa:
        print aa, pwr

6.
s = '1.23,2.4,3.123'
a = s.split(',')
sum = 0
for i in a:
    sum += float(i)
print(sum)

7.
def isIn(a,b):
    if a in b or b in a:
        print("true")
    else:
        print("flase")
aa="raj kumar"
bb="kumar"
isIn(aa,bb)

8.
def getRatios(vect1, vect2):
    aa=[]
    if len(vect1) == len(vect2):
        for i in range(0,len(vect1)):
            a = vect1[i]/vect2[i]
            aa.append(a)
    return aa
try:
    x=[5,10,15,20,25]
    y=[2,20,30,40,50]
    print(getRatios(x,y))
except:
    print(" NotImplemented")

9.
w=17
w/2
w/2.0
h=12
h/3
1+2*5
de="."
de * 5
---------------------------------------------------------------------------------------------------------------------------
					
