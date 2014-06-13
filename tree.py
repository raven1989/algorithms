#!/usr/bin/python
#Trees
import sys
import stack

class BTNode:
  '''Binary Tree Node.'''
  def __init__(self,item=None,l=None,r=None):
    self.data=item
    self.left=l
    self.right=r
  def setLeft(self,l):
    self.left=l
  def setRight(self,r):
    self.right=r
  def isLeaf(self):
    return self.left==self.right==None

class StackElement:
  '''Stack element used in binary tree post order iteration.'''
  def __init__(self,node=None,tag=0):
    self.node=node
    self.tag=tag

class BTree:
  '''Binary Tree.'''
  def __init__(self,ro=None):
    self.root=ro

  def __isBST__(self,root,mmin,mmax):
    if(root==None):
      return True
    if(mmin<root.data<mmax):
      return self.__isBST__(root.left,mmin,root.data) \
          and self.__isBST__(root.right,root.data,mmax)
    else:
      return False

  def isBST(self):
    '''Binary search tree validity
    
            It will return None if it is a none tree;
            Return True if it is a Binary search tree;
            Return False if it is not.'''
    if(self.root==None):
      return None
    return self.__isBST__(self.root,-sys.maxint-1,sys.maxint)

  def __maximalDepth_R__(self,r):
    if(r==None):
      return 0
    l=self.__maximalDepth_R__(r.left)
    r=self.__maximalDepth_R__(r.right)
    return 1+max(l,r)

  def maximalDepth_R(self):
    '''Count the maximal depth of a binary tree recursively.'''
    return self.__maximalDepth_R__(self.root)

  def maximalDepth_I(self):
    '''Count the maximal depth of a binary tree iteratively.
    
            Iterate the tree in post order, 
            the maximal length of stack is the maximal depth.'''
    if(self.root==None):
      return 0
    maxlvl=0
    s=stack.Stack()
    e=StackElement()
    p=self.root
    while(p!=None or not s.isEmpty()):
      while(p!=None):
        e.node=p
        e.tag=0
        s.push(e)
        p=p.left
      e=s.top()
      s.pop()
      while(e.tag==1):
#be aware that the current element has been popped out
#so the current level should +1
        curlvl=s.length()+1
        if(maxlvl<curlvl):
          maxlvl=curlvl
        if(s.isEmpty()):
          return maxlvl
        e=s.top()
        s.pop()
      p=e.node
      e.tag=1
      s.push(e)
      p=p.right
    return maxlvl


class BSTree:
  '''Binary search tree.'''
  def __init__(self,ro=None):
    self.root=ro


if(__name__=='__main__'):
  root=BTNode(10)
  l=BTNode(5)
  r=BTNode(15)
  root.left=l
  root.right=r
  print root.data
  print root.left.data,root.right.data
  none=BTNode()
  print none.data

  bt=BTree(root)
  print bt.isBST()
  r.left=BTNode(13)
  l.left=BTNode(-9)
  print bt.isBST()
  l.right=BTNode(7)
  r.right=BTNode(11)
  print bt.isBST()

  print bt.maximalDepth_R()
  print bt.maximalDepth_I()
