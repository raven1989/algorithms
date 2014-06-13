#!/usr/bin/python

def binarySearchRoated(a,x):
  '''Given a rotated sorted array, find a specified element.'''
  if(a==None or len(a)<1):
    return None
  l=0
  r=len(a)-1
  while(l<=r):
    m=(l+r)/2
    if(a[m]==x):
      return m
#if former half is not rotated
    if(a[l]<a[m]):
      if(a[l]<=x<a[m]):
        r=m-1
      else:
        l=m+1
#if latter falf is not rotated
    else:
      if(a[m]<x<=a[r]):
        l=m+1
      else:
        r=m-1
  return None

if(__name__=='__main__'):
  a=[4,5,6,7,0,1,2]
  print a
  x=0
  print 'find %d in a:'%x,binarySearchRoated(a,x)
  x=7
  print 'find %d in a:'%x,binarySearchRoated(a,x)
  x=4
  print 'find %d in a:'%x,binarySearchRoated(a,x)
  x=3
  print 'find %d in a:'%x,binarySearchRoated(a,x)
  x=9
  print 'find %d in a:'%x,binarySearchRoated(a,x)
