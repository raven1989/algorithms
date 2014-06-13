#!/usr/bin/python

def multiplication(a):
  '''Given an array a[n] of n integers, compose an array out[n] such that
  out[i] will equal to multiplication of all integers of a[n] except for itself.
  Solve this without division and in O(n).'''
  if(a==None or len(a)<=1):
    return None
  out=[]
  b=[]
  n=len(a)
  mul=1
  i=0
  while(i<n):
    b.append(mul)
    mul*=a[i]
    i+=1
  mul_backwards=1
  i-=1
  while(i>=0):
    out.append(b[i]*mul_backwards)
    mul_backwards*=a[i]
    i-=1
  out.reverse()
  return out

if(__name__=='__main__'):
  a=[4,3,2,1,2]
  print a
  print multiplication(a)
  
