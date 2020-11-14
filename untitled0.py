# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 12:19:49 2019

@author: 17101538
"""

#task1
ab=int(input("Enter a percentage :"));
b1=ab/100
print(b1)


#task2
temp=int(input("Enter a percentage :"));
btemp=1.8*temp+32
print(btemp)


#task3
i=int(input("Enter a number :"));
feet=int(i*(1/12));
inch=i%feet 
print(i," inches if ",feet," feet ","and ",inch," inches")


#task4
num=int(input("Number of copy :"))
if num>100 :
    n=num-100
    cost=(50*100)+(30*n)

elif num<=100 :
    cost=50*100

print("total cost : ",cost);    


#task5
year=(input("Ekta year den :"))
year=int(year.strip('0'))
if (year/4)==0 :
        print("huraahhh leap year !!")
else :
    print("sorry onno bochor dekho :( ")


#task6
sum=0
n=0
for num in range(1,100):
    
    if (num%3) == 0:
        sum=sum + num
        n=n+1

avg=sum/n
print("Average : ",avg)

#task7
import math 
a = 1
b = -1
c = -1980 
x1=(-b+math.sqrt(b*b-4*a*c))/(2*a)
x2=(-b-math.sqrt(b*b-4*a*c))/(2*a)
print("the value of x is :",x1)


#task8
#st=input("6ta input den")
numList=[1,2,3,4,5,6]
numList.sort()
sum1=numList[1] + numList[4]
sum2=numList[2] + numList[3] 
print("sum of second smallest and second largest ",sum1)
print("sum of third  smallest and third largest ",sum2)

#task9
l = [1,2,3,4,5,6,7,8,9,10]
l.sort()
sum=0
for num in range(0,10):
    sum=sum+num
avg=sum/10
diff1=avg-l[0]
diff2=avg-l[9]
print("difference between smallest ",diff1)
print("difference between largest ",diff2)

#task10
import math 
s1=int(input())
s2=int(input())
s3=int(input())
s=(s1+s2+s3)/2
a=math.sqrt(s*(s-s1)*(s-s2)*(s-s3))
print(a)

    
    
