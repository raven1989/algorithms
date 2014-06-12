#!/usr/bin/python
def Partition(a,left,right):
  pivot=(left+right)/2
  #print pivot,a[pivot]
  tmp=a[pivot]
  a[pivot]=a[right]
  while(left<right):
    while(a[left]<tmp and left<right):
      left+=1
    if(left<right):
      a[right]=a[left]
      right-=1
    while(a[right]>tmp and left<right):
      right-=1
    if(left<right):
      a[left]=a[right]
      left+=1
  pivot=left
  a[pivot]=tmp
  return pivot

def kthSmallest(a,k,left,right):
  n=right-left+1
  #print '%d th out of %d' %(k,n)
  if(k>n or left>right):
    return False
  if(left==right):
    return a[left]
  pivot=Partition(a,left,right)
  #print 'pivot=',pivot
  #print a[left:pivot],a[pivot],a[pivot+1:right+1]
  if(pivot+1<k):
    return kthSmallest(a[pivot+1:right+1],k-pivot-1,0,right-pivot-1)
  elif(pivot+1>k):
    return kthSmallest(a[left:pivot],k,0,pivot-1)
  else:
    return a[pivot]

a=[3,6,7,1,4,2,5]
for k in range(7):
  print 'find %dth in' %(k+1),a
  res=kthSmallest(a,k+1,0,6)
#print a
  if(res!=False):
    print res
