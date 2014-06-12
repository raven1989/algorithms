#!/usr/bin/python

def intersection(a,b):
  '''Given 2 sorted arrays, find their intersection.'''
  res=[]
  if(a==None or b==None):
    return res
  m=len(a)
  n=len(b)
  i=j=0
  while(i<m and j<n):
    if(a[i]<b[j]):
      i+=1
    elif(a[i]>b[j]):
      j+=1
    else:
      res.append(a[i])
      i+=1
      j+=1
  return res

if(__name__=='__main__'):
  a=[1,4,5,6,7,10]
  b=[1,2,3,4,5,6,7,8,9]
  print a
  print b
  print intersection(a,b)
