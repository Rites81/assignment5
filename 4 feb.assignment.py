#!/usr/bin/env python
# coding: utf-8

# # lambda function

# In[3]:


cricket_Score=[('Sachin Tendulkar',34357),('Ricky Ponding',27483),('Jack kallis',25534),('Virat Kohli',24936)]
print("Original list of tuple::")
print(cricket_Score)
cricket_Score.sort(key=lambda x:x[1])
print("\n Sorting the list lo tuples is::")
print(cricket_Score)


# # Square of function

# In[1]:


def square(num):
 return num*num

number=[1,2,3,4,5,6,7,8,9,10]
square=list(map(square,number))
print(square)


# In[1]:


num=[2, 3, 6, 9, 27, 60, 90, 120, 55, 46]
li=list(filter(lambda x: (x % 2==0),num))
print("Number divisible by 2 is::",li)

li=list(filter(lambda x: (x%3==0),num))
print("Number is divisible by 3 is::",li)


# In[10]:


Given_String= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Origianl string is::")
print(Given_String)
result=tuple(map(str,Given_String))
print("Expectation Value is::")
print(result)


# In[8]:


from functools import reduce

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25] 
print ("The product is : ",end="") 
print (reduce(lambda x,y: x*y,list1))


# In[12]:


text=['python', 'php', 'aba', 'radar', 'level']
print("Original list of string:")
print(text)
result=list(filter(lambda x:(x=="".join(reversed(x))),text))
print("List of palindrom:")
print(result)


# In[ ]:




