#!/usr/bin/env python
# coding: utf-8

# In[36]:


def read_input():
    # Initialize empty lists for the two numbers
    list1 = []
    list2 = []
    
    # Open file
    with open("input.txt") as f:
        for line in f:
            left, right = map(int, line.split())
            list1.append(left)
            list2.append(right)
    list1.sort()
    list2.sort()
    return list1, list2
    
def first_part(list1, list2):
    list3 = [abs(a-b) for a,b in zip(list1, list2)]
    return sum(list3)

def second_part(list1, list2):
    
    score = 0
    for num in list1:
        freq = list2.count(num)
        score += freq*num
    return score

