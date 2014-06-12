#!/usr/bin/python

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

class BTNode_RS(BTNode):
  '''Binary Tree Node with Right Sibling pointer.'''
  def __init__(self,item=None,l=None,r=None,rs=None):
    BTNode.__init__(self,item,l,r)
    self.rSibling=rs

class BTree_RS:
  '''A Binary Tree whose nodes are BTnode_RS.'''

  def __init__(self,ro=None):
    self.root=ro
  
  def __isFullBT__(self,ro):
    if(ro.isLeaf()):
      return True
    elif(ro.left==None or ro.right==None):
      return False
    else:
      return self.__isFullBT__(ro.left) and self.__isFullBT__(ro.right)

  def __inOrderPrint__(self,ro):
    if(ro!=None):
      self.__inOrderPrint__(ro.left)
      print ro.data,
      self.__inOrderPrint__(ro.right)

  def inOrderPrint(self):
    if(self.root!=None):
      print 'in rder:',
      self.__inOrderPrint__(self.root)
      print 'end'

  def isFullBT(self):
    '''If a binary tree is FULL binary tree, return true, otherwise return false.
    
            A full binary tree is a binary tree whose all none-leaf nodes have both left and right child.'''
    if(self.root==None):
      return False
    return self.__isFullBT__(self.root)

  
  def __connectRSiblings__(self,ro):
    if(ro==None):
      return True
    parent=ro
    firstChild=None #first child of the current level
    while(parent!=None):
      if(parent.left!=None): #if full binary tree has left, then it must have right
        if(firstChild==None):
          firstChild=parent.left
        parent.left.rSibling=parent.right
        if(parent.rSibling!=None):
          parent.right.rSibling=parent.rSibling.left
        else:
          parent.right.rSibling=None
      parent=parent.rSibling
    return self.__connectRSiblings__(firstChild)
    
  def connectRSiblings(self):
    '''Connect rSibling pointers which requires a FULL binary tree.
    
            Assume rSibling pointers of nodes of last level have been connected, therefore there is a list of parents connected by rSiblings. For current level, just iterate the parents list and connect every left child's rSibling to rigjt child, right child's to the next parent's left child if it exists. By starting with root and doing this recursively, the whole tree is accordingly connected.'''
    if(self.root==None or (not self.isFullBT()) ):
      return False
    return self.__connectRSiblings__(self.root)

if(__name__=='__main__'):
  leaf1=BTNode_RS(6)
  leaf2=BTNode_RS(7)
  leaf3=BTNode_RS(8)
  leaf4=BTNode_RS(9)
  lv3_1=BTNode_RS(4,leaf1,leaf2)
  lv3_2=BTNode_RS(5,leaf3,leaf4)
  lv2_1=BTNode_RS(2)
  lv2_2=BTNode_RS(3,lv3_1,lv3_2)
  lv1=BTNode_RS(1,lv2_1,lv2_2)

  bt=BTree_RS(lv1)
  bt.inOrderPrint()
  if(bt.connectRSiblings()):
    lv=leaf1#lv3_1
    #print lv.rSibling
    while(lv!=None):
      print lv.data,
      lv=lv.rSibling
    else:
      print "end for this level"
