#!/usr/bin/python
#!encoding:utf-8

def jump(stairs):
  '''有一排台阶，每一个台阶上有一个非负整数，代表在该台阶上时最多能向前跳几个台阶。判断是否能到达最后一个台阶。
比如：4 2 3 1 0 2 ture
      3 1 1 1 0 2 false'''
  length = len(stairs)
  if length <=0:
    return False
  poineer = 0
  for i in range(0,length):
    cur = stairs[i]+i
    if cur > poineer:
      poineer = cur
    if i >= poineer:
      break
    elif poineer >= length-1:
      return True
#  if poineer < length-1:
#    return False
  return False

if __name__ == '__main__':
  s = [3,1,1,0,2]
  print s,jump(s)
  s = [3,1,1,1,0]
  print s,jump(s)
  s = [4,2,3,1,0,2]
  print s,jump(s)
  s = [4,3,2,1,0,2]
  print s,jump(s)

