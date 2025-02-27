# In this I will test Is and In keywords in python

# we start with Is


# Is keyword is used to check if an object is an instance of a class or not.
# es ya check kiya ya a jo ha wo b  ek ha  jase hum ne pass kiya  b=a  
# es ya check kare c  m to  false ho ga 
a = [1,4,8,20,50]
b=a
c= [1,2,4,6,7,]

print(a is b)

print(a is b is c)
# In keywords  check in code 
# es code mn ya check kiya a jo ha wo bhi m na to 

print(a in b)

d=[1,4,8,20,50]

print(1 in a and 1 in d)