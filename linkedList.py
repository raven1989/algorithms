#!/usr/bin/python

class ListNode:
  '''Linked list node.'''
  def __init__(self,item=None,n=None):
    self.data=item
    self.link=n

class List:
  '''A linked List.'''
  def __init__(self,h=None):
    self.head=h
    self.length=0
    while(h!=None):
      self.length+=1
      h=h.link
  
  def display(self):
    i=self.head
    while(i!=None):
      print i.data,
      i=i.link
    print '$'

