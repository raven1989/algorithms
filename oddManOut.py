#!/usr/bin/python
# Given an unsorted array within which all integers appear even times except for one that appears odd times. Find this integer.

def oddMan(a):
  '''Find the only integer that appears odd times within an array whose other integers all appear even times.
  
        XOR is optimal solution: a^b^c^a^c=b.
        The equation above requires subjection of XOR to commutative law, which it is:
          For every bit: 0x1^0x0^0x1=0x0^0x1^0x1 
    '''
  if(a==None or len(a)<1):
    return None
  odd_man=0   # any integer XOR itself does not change.
  for i in a:
    odd_man^=i
  return odd_man

if(__name__=='__main__'):
  a=(4,2,1,6,3,4,2,2,1,3,3,6,3)
  print a
  print 'the one appears odd times:'
  print oddMan(a)
