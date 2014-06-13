#!/usr/bin/python
import linkedList

def reverseLL_I(l):
  '''Reverse a linked list iteratively.'''
  if(l==None or l.head==None):
    return l
  pre=None
  nExt=l.head.link
  while(nExt!=None):
    l.head.link=pre
    pre=l.head
    l.head=nExt
    nExt=nExt.link
  else:
    l.head.link=pre
  return l

def reverseLL_R_helper(l): #in c++, a ListNode*& serves as a parameter so
  if(l.head.link!=None):#that list's head could be changed simultaneously.
    cur=l.head  #However,in python,in order to achieve this, 
    l.head=l.head.link #the list itself has to be passed in as a parameter
    reverseLL_R_helper(l) #so that the list.head can be changed.
    cur.link.link=cur
    cur.link=None

def reverseLL_R(l):
  '''Reverse a linked list recursively.'''
  if(l==None or l.head==None):
    return l
  reverseLL_R_helper(l)
  return l

if(__name__=='__main__'):
  l5=linkedList.ListNode(5)
  l4=linkedList.ListNode(4,l5)
  l3=linkedList.ListNode(3,l4)
  l2=linkedList.ListNode(2,l3)
  l1=linkedList.ListNode(1,l2)
  ll=linkedList.List(l1)
  ll.display()
  reverseLL_I(ll)
  ll.display()
  reverseLL_R(ll)
  ll.display()

