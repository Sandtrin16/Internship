#!/usr/bin/env python
# coding: utf-8

# In[1]:


#code to find factorial of any number
x = int(input(" Enter a number for finding factorial: "));
y = 1;
Factorial = z = x;
if x <=1:
    x = x*0;
    print(x);
else:
    while y<x:
        #print (Factorial);
        z = z -1
        Factorial= Factorial * z;
        y =y+1;
    #print(Factorial)
    print(" the  required factorial of", x ,"is", Factorial)


# In[38]:


# code to find if numbe ris prime or composite;

x = int(input(" Enter a number "));
i = 2 
composite =0
while(i < x):
    output = x%i
   # print(x,i,output,composite)
    i =i+1
    if output == 0:
        composite += 1
    else:
        prime = 1  
if composite >= 1:
    print(x,"is composite")
else:
    print(x, "is prime")        

    


# In[40]:


# code to find if string is palindrome or not 
def read_back(x):
    return x[::-1]
x = str(input("enter string : "))
print  (" Forward read",x)
y = read_back(x)
print ('Read Backward',y)

if x == y:
    print("The given word is a palindrome")
    

    


# In[41]:


# python program to get third side of right angled triangle
import math as mt
x = float(input("Enter side 1: "))
y = float( input ("Enter side 2: "))

z = mt.sqrt((x**2 + y**2))
print('The third side of the right angled triangle is:' ,z)


# In[43]:


# python program to find the frequency of each character present in string

import pandas as pd
string = str(input("Enter String"))
splitstring = string.split()
print(splitstring)
newdf= pd.DataFrame(splitstring, columns =['name'])
print(newdf)
newdf['name'].value_counts()

     


# In[ ]:





# In[ ]:




