#!/usr/bin/python
# Given an integer x and an unsorted array of integers, to find all the pair of integers that add up to x.

def combination2(x,a):
  if(a==None or len(a)<2):
    return None
  a.sort()
  #print a
  pairs=[]
  i=0
  j=len(a)-1
  while(i<j):
    if(a[j]==x-a[i]):
      pairs.append((a[i],a[j]))
      i+=1
      j-=1
    elif(a[j]<x-a[i]):
      i+=1
    else:
      j-=1
  return pairs

if(__name__=='__main__'):
  x=0
  a=[0,-3,1,2,3,-5,6,-1,-6,-1]
  print a
  print combination2(x,a)

