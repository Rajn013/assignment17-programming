#!/usr/bin/env python
# coding: utf-8

# Create a function that takes three arguments a, b, c and returns the sum of the numbers that are evenly divided by c from the range a, b inclusive.

# In[33]:


def evenly_divisible(a , b, c):
    total_sum = 0
    
    for i in range(a, b+1):
        if i % c == 0:
            total_sum += i
            
    return total_sum


# In[35]:


print(evenly_divisible(1, 10, 20))
print(evenly_divisible(1, 10, 2))
print(evenly_divisible(1, 10, 3))


# Question2. Create a function that returns True if a given inequality expression is correct and False otherwise.
# 

# In[36]:


def is_inequality_correct(expr):
    return eval(expr)


# In[38]:


print(is_inequality_correct("3 < 7 < 11"))
print(is_inequality_correct("13 > 44 > 33 > 1"))
print(is_inequality_correct("1 < 2 < 6 < 9 > 3"))


# Question3. Create a function that replaces all the vowels in a string with a specified character.

# In[47]:


def replace_vowels(string, char):
    vowels = "aeiouAEIOU"
    result = ""
    for letter in string:
        if letter in vowels:
            result += char
        else:
            result += letter
    return result

print(replace_vowels("the aardvark", "#" ))
print(replace_vowels("minnie mouse" , "?"))
print(replace_vowels("shakespeare" , "*"))


# Question4. Write a function that calculates the factorial of a number recursively.
# 

# In[48]:


def factorial(n):
    if n == 0 or n ==1:
        return 1
    else:
        return n * factorial(n-1)


# In[51]:


print(factorial(5))
print(factorial(3))
print(factorial(1))
print(factorial(0))


# 5.Hamming distance is the number of characters that differ between two strings.
# To illustrate:
# 

# In[54]:


def hamming_distance(str1, str2):
    if len(str1) != len(str2):
        return None
    else:
        distance = 0
        for i in range (len(str1)):
            if str1[i] != str2[i]:
                distance += 1
        return distance


# In[56]:


print(hamming_distance("abcbba" , "abcbda"))
print(hamming_distance("abcde", "abcde"))
print(hamming_distance("strong", "strung"))
print(hamming_distance("abcde", "bcdef"))


# In[ ]:




