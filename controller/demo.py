import pandas as pd
import fractions
import array as arr

#df = pd.read_csv('Sample.csv',encoding='windows-1252')
#print(df.to_string())
#for i in range(3, 7):
   # print(f"{i} % 3 =", i % 3)
#for i in range(2, 5):
 #   print(f"{i} ** {i} =", i ** i)

#for i in range(9, 20, 4):
 #  print(f"$ {i} // 5 =", i // 5)
#x = 1
#x *= 5
#print(x)
##one_ninth = fractions.Fraction(3, 9, _normalize=False)
#one_seventh = fractions.Fraction(1, 9)
#large_number = 7323843829343
#large_number= format(large_number,",")
#x=12
#sum=1
#for i in range (1,x+1):
#    sum=sum*i;
#print(sum)

#armstroong number
#371

#num= 371
#sum=0

#length =len(str(num))
#for i in range(1,length+1):
#    mod=num%10
#    sum=sum+(mod**length)
#    num= num//10
#print(sum)

#000000000000000000000000000000000cvbnmdkjbhvshbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb

#print all prime numbers

#sum =12
#list=[]
#for i in range(3,12):
#    flag=0
#    for j in range(2,i):
##        if(i%j==0):
#            flag=1
#            break
#   if (flag==0):
#        list.append(i)
#print(list)

#=============================================

#x=[i for i in range(5)]
#print(x)

#x = [i : i+1 for i in range(5)]
#print(x)

# 443u9839u12j qs7777777777777777777777777777777777777777777777
# ternary operator
x =12
y=20

big = x if x<y else y
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
"""
a=arr.array('d',[1.1 , 2 ,3.1] )
s=[]
n = int(input("size of list"))
for i in range(n):
    l=input()
    s.append(l)
print(s)
"""
"""
a=int(input("Number of elements in the array:-"))
n=list(map(int, input("elements of array:-").strip().split()))
print(n)
"""
"""
list=[]
size =int(input())
for i in range(size):
    list.append(input())
list.sort()
print(list)
"""
"""
import numpy as np
a = np.array([1,2,3,4,5])
p = np.percentile(a, 50) #Returns 50th percentile, e.g. median
print(p)

===========================

"""
"""
dict={}
dict ["s1"]= "abcd jkhd abcd jhsjs"
dict ["s2"]= "iodhd abc"
dict ["s3"]= "idhd djnjd abc"
list=[]
for i in dict:
    if "abc" in dict[i]:
        list.append(i)
print(list)

import pandas as pd

# Creating and initializing a nested list
age = [['Aman', 95.5, "Male"], ['Sunny', 65.7, "Female"],
       ['Monty', 85.1, "Male"], ['toni', 75.4, "Male"]]
df = pd.DataFrame(age)
print(df)
"""
"""
a = {'V': '5', "I": '1', 'X': '10', 'L': '50', 'C': '100', 'D': '500', 'M': '1000'}
sum = 0
#s="MCMXCIV"
s="LVIII"
for i in range(len(s)):
    sum=sum+int(a[s[i]])
print(sum)
"""
"""
num = 0
digits=[1,2,3]
for i in range(len(digits)):
    num = num * 10 + digits[i]
print(num)
num = num + 1
print(num)

s = num
s = str(s)
arr = []
for i in range(len(s)):
    modulus = num % 10
    arr.append(modulus)
    num = int(num /10)
print(arr[::-1])
"""
"""
accounts=[[2,8,7],[7,1,3],[1,9,5]]
max=0
for i in accounts:
    sum=0
    for j in i:
        sum=sum+j;
    if(sum>max):
        max=sum
        index=i
"""

"""
nums=[3,2,4]
target=6
arr = []
for i in range(len(nums)):
    for j in range(len(nums)):
        if (nums[i] + nums[j] == target and (i < j)):
            arr.append(i)
            arr.append(j)
            break
print(arr)
"""
"""
nums1=[1,2]
nums2=[3,4]
mergedArray= [None] * (len(nums1)+len(nums2))
i=0
j=0
k=0
value=float(0)
while(i<len(nums1) and j<len(nums2)):
    if nums1[i]>nums2[j]:
        mergedArray[k]=nums2[j]
        j=j+1
    else:
        mergedArray[k]=nums1[i]
        i=i+1
    k=k+1
while(i<len(nums1)):
    mergedArray[k]=nums1[i]
    i=i+1
    k=k+1
while(j<len(nums2)):
    mergedArray[k]=nums2[j]
    j=j+1
    k=k+1
print(mergedArray)

if(len(mergedArray)%2==0):
    index1=int(len(mergedArray)/2)
    index2=index1-1
    value=float((mergedArray[index1]+mergedArray[index2])/2)
else:
    index=int(len(mergedArray)/2)
    value=float(mergedArray[index])
print(value)
"""

"""
def findMedianSortedArrays():
    nums1 = [1, 2,12]
    nums2 = [3, 4,15]
    mergedArray = [None] * (len(nums1) + len(nums2))
    i = 0
    j = 0
    k = 0
    value = float(0)
    while (i < len(nums1) and j < len(nums2)):
        if nums1[i] > nums2[j]:
            mergedArray[k] = nums2[j]
            j = j + 1
        else:
            mergedArray[k] = nums1[i]
            i = i + 1
        k = k + 1
    while (i < len(nums1)):
        mergedArray[k] = nums1[i]
        i = i + 1
        k = k + 1
    while (j < len(nums2)):
        mergedArray[k] = nums2[j]
        j = j + 1
        k = k + 1

    if (len(mergedArray) % 2 == 0):
        index1 = int(len(mergedArray) / 2)
        index2 = index1 - 1
        value1=mergedArray[index1]
        value2=mergedArray[index2]
        value=float((value1+value2)/2)
    else:
        index = int(len(mergedArray) / 2)
        value = float(mergedArray[index])
    print(mergedArray)
    return value
"""
"""
strs=["flower","flow","flight"]
arr=[]
for i in range(len(strs[0])):
    arr1=[]
    for j in range(i):
        arr1.append(strs[0][j])
    arr.append(arr1)
for i in range(len(strs))
    if()
"""
"""
#strs=["ab", "abcd","ab"]
#strs=["ab","abow","abcight"]
#strs=["fower","fow","fight"]
#strs=["dog","racecar","car"]
strs=["flower","flower","flower","flower"]

arr=[]
if len(strs)==0:
    arr=""
if len(strs)==1:
    arr=strs[0]
flag=0
for i in range(len(strs[0])):
    arr.append(strs[0][0:i+1])
print(arr)
for i in range(0,len(strs[0])):
    for j in range(1,len(strs)):
        if (strs[j].startswith(arr[i])!=True):
             flag=1
    if flag==1:
         if i==0:
            print("")
         else:
             print(arr[i-1])
         break
print(arr[i])

"""

"""
nums=[1,1,2]
m = list(set(nums))
m.sort()
print(m)
for i in range(len(m)):
    nums[i] = m[i]
print(len(nums))
"""
"""
nums= [1,2,3,10,12,45,56,78]
start=0
end=len(nums)-1
mid=0
x=12

while start<=end:
    mid=(start+end)//2
    if(nums[mid]>x):
        end=mid-1
    elif nums[mid]<x:
        start=mid+1
    else:
        print(mid)
        break
print("-1")
"""
"""
str="Hello worlddddd   "
lenth = 0
str=str.strip()
for i in range(len(str)):
    if str[len(str) - i-1] == " ":
        break
    lenth = lenth + 1
print(lenth)

l=[]
l.append("ssss")
print(l)
"""
"""nums=[0,1,2,2,2,3,0,4,2,2,2,2,2,2,2]
val=2
end=len(nums)
s = nums.count(val)

for i in range(s):
    nums.remove()
print(nums)
"""




# nums1=[1,2,3,0,0,0]
# nums2=[2,5,6]
#
# mergedArray=[None]*(len(nums1))
# i,j,k=0,0,0
# for r in range(len(nums2)):
#     nums1.remove(0)
# while(i<len(nums1) and j<len(nums2)):
#     if nums1[i]<nums2[j]:
#         mergedArray[k]=nums1[i]
#         i=i+1
#     else:
#         mergedArray[k]=nums2[j]
#         j=j+1
#     k=k+1
# while(i<len(nums1)):
#     mergedArray[k]=nums1[i]
#     i=i+1
#     k=k+1
# while(j<len(nums2)):
#     mergedArray[k] = nums2[j]
#     j = j + 1
#     k = k + 1
#
# nums1=mergedArray
# import random
# print(hex(random.randint(0, 1800000000)))
# x=(hex(random.randint(0, 1800000000))[2:])
# print(x)
# print(x[2:])