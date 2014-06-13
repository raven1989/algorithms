#!/usr/bin/python

def triplet(array):
  '''Given an array, find every combination of 3 elements whose sum is 0,
  namely, a+b+c=0. Such (a,b,c) is called triplet, and its repetations like
  (a,c,b) are not wanted.
  
        This problem is a straight forward extension of the problem below
        if the equation above is transformed as b+c=-a:
          Given a set S of n integers, find all pairs of integers of b and c such that c+b=k.(Solved in targetSum.py)
        Here,since k=-a, we just iterate all 'a's in array and 
        find b and c in sets whose elements are all behind a such that b+c=-a.
        '''
  if(array==None or len(array)<3):
    return None
  array.sort()
  n=len(array)
  res=[]
  for a in range(n):
    b=a+1
    c=n-1
    sum2=-array[a]
    while(b<c):
      if(array[b]+array[c]<sum2):
        b+=1
      elif(array[b]+array[c]>sum2):
        c-=1
      else:
        res.append((array[a],array[b],array[c]))
        b+=1
        c-=1
  return res

if(__name__=='__main__'):
  s=[-1,0,1,2,-1,4]
  print s
  print triplet(s)

