#!/usr/bin/env python
# coding: utf-8

# In[4]:


num=int(input("Enter a number. "))
factorial=1
if num<0:
    print("Factorial of this number not exist(because of negative number)")
elif num==0:
    print("The factorial of 0 is 1")
else:
    for i in range(1,num+1):
        factorial=factorial*i
    print("The factorial of " ,num,"is ",factorial)


# In[ ]:





# In[ ]:




