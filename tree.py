#!/usr/bin/python
#Trees
import sys

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

