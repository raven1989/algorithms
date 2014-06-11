#!/usr/bin/python
#Design a stack that supports push, pop, and retrieving the minimum element in constant time.
import stack
class MinStack:
  '''A stack is able to retrive the mininum element.'''
  def __init__(self):
    self.s=stack.Stack()
    self.min_s=stack.Stack()
  def push(self,item):
    self.s.push(item)
    if(self.min_s.isEmpty or self.min_s.top()>item):
      self.min_s.push(item)
  def top(self):
    return self.s.top()
  def pop(self):
    if(self.min_s.top()==self.s.top()!=None):
      self.min_s.pop()
    return self.s.pop()
  def min(self):
    return self.min_s.top()
  def length(self):
    return len(self.s)
  def clear(self):
    self.s.clear()
    self.min_s.clear()

if __name__=='__main__':
  ss=MinStack()
  for i in range(7):
    ss.push(7-i)
  print ss.min()
  ss.pop()
  print ss.s.s
  print ss.min_s.s
  print ss.min()
