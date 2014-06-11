#!/usr/bin/python

class Stack:
  '''A simple stack.'''
  def __init__(self):
    self.s=[]
  def push(self,item):
    self.s.append(item)
  def top(self):
    if(self.s!=[]):
      return self.s[-1]
    else:
      return None
  def pop(self):
    if(self.s!=[]):
      return self.s.pop(-1)
    else:
      return None
  def length(self):
    return len(self.s)
  def isEmpty(self):
    return self.s==[]
  def clear(self):
    self.s=[]

if __name__ == '__main__':
  s=Stack()
  for i in range(5):
    s.push(i)
  print s.s
  a=s.top()
  print a
  a=7
  print s.top()
  s.pop()
  print s.top()
  t=s.s
  s.clear()
  print t,s.s
  print s.isEmpty()
