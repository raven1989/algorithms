#!/usr/bin/python
#Given an array, to find the subarray with the maximal sum
import sys
def maxSubarray(a):
  '''Find the subarray with the maximal sum.
  
        Keep track of a sum_cur indicates the sum from 0 to i; 
        Keep track of a sum_min indicates the minimal sum from 0 to i;
        Noticing that the largest sum_cur-sum_min is what is wanted.
        This problem evolves from the Beat Stock problem.
        '''
  if(a==None or len(a)<1):
    return None
  sum_min=sum_cur=0
  dif_max=0
  i_min=i=j=0
  for k in range(len(a)):
    sum_cur+=a[k]
    if(sum_cur<sum_min):
      sum_min=sum_cur
      i_min=k+1
    elif(sum_cur-sum_min>dif_max):
      dif_max=sum_cur-sum_min
      i=i_min
      j=k
    else:
      continue
  res=[]
  while(i<=j):
    res.append(a[i])
    i+=1
  return res

if(__name__=='__main__'):
  a=(1,-3,5,-2,9,-8,-6,4)
  print a,maxSubarray(a)
  b=[-5]
  print b,maxSubarray(b)
  c=(1,-2)
  print c,maxSubarray(c)
  d=(3,6)
  print d,maxSubarray(d)
  e=(-2,2)
  print e,maxSubarray(e)
