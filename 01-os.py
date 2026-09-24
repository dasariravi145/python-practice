import os

c =1

kw= input("enter the searching keyword")

for i in dir(os): 
     if kw in i.lower():
        print(c,i)
        c += 1
