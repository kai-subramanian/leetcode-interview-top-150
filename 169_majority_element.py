#Given an array nums of size n, return the majority element.
#The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

def majority(nums):
    ct=0
    cn=0
    for i in nums:
        if(ct==0):
            cn=i
        if(cn==i):
            ct+=1
        else:
            ct-=1
    return cn

print(majority([2,2,1,1,1,2,2]))