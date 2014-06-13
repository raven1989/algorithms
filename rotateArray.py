#!/usr/bin/python
#encoding:utf-8
def reverseArray(a,left,right):
  if(a==None or left<0 or right>=len(a)):
    return False
  i=left
  j=right
  while(i<j):
    a[i]^=a[j]
    a[j]^=a[i]
    a[i]^=a[j]
    i+=1
    j-=1

def rotateSortedArray(a,x):
  '''Rotate a sorted array x steps.'''
  if(a==None or len(a)<1):
    return False
  n=len(a)
  xx=x%n
  if(xx>0):
    reverseArray(a,0,n-1) #a.reverse()
    reverseArray(a,0,xx-1)
    reverseArray(a,xx,n-1)
  return True

def xStepsRotated(a):
  '''find out how many steps a sorted array is rotated.
  
        Be aware that array such as a=[1,2,3,4] is rotated 0 steps'''
  if(a==None or len(a)<1):
    return None
  n=len(a)
  l=0
  r=n-1
  while(l<=r):
    m=(l+r)/2
#when it's 0 step rotated, m-1<0
    if(m-1<0 or a[m-1]>a[m]):
      return m
#这里使用条件a[l]<a[m] r=m-1 else ...和 a[l]>a[m] l=m+1 else ...都会在
#移0步时发生错误，使用a[r]>a[m]排除法：
#当a[r]>a[m]时，pivot一定不在m~r里面
#用r做判断条件的另一个原因是m=(l+r)/2，l是可能等于m的，r是一定不会被干扰的
    elif(a[r]>a[m]):
      r=m-1
    else:
      l=m+1

if(__name__=='__main__'):
  a=[1,2,3,4,5,6]
  x=3
  print a
  print rotateSortedArray(a,x),a
  a.sort()
  x=0
  print rotateSortedArray(a,x),a
  a.sort()
  x=len(a)
  print rotateSortedArray(a,x),a
  a.sort()
  x=len(a)+2
  print rotateSortedArray(a,x),a

  a.sort()
  print a,'is rotated',xStepsRotated(a),'steps'
  rotateSortedArray(a,len(a)-1)
  print a,'is rotated',xStepsRotated(a),'steps'
