#!/usr/bin/python
#!encoding:utf-8

def reproduct(mon, m):
  '''有一种细菌寿命为5个月，从第三个月开始，每个月繁殖一代，一个细菌一次可以繁殖m个。此时有一个细菌，第n个月时有多少个这种细菌'''
#timeline[i]表示第i+1个月出生的细菌数量，因为同时最多能共存5代，所以用一个长度为5的数组，做成循环队列
  front = -1
  rear = 0
  timeline = [0,0,0,0,0]
  timeline[0] = 1 
  rear=(rear+1)%5
  timeline[1] = 0
  rear=(rear+1)%5
  timeline[2] = 1*m
  rear=(rear+1)%5
  timeline[3] = 1*m
  rear=(rear+1)%5
  timeline[4] = (1+m)*m
  rear=(rear+1)%5

  res = 0
  if mon>5:
    for i in range(5,mon):
#      print front,rear,timeline
      front = (front+1)%5 #dequeue
      #cur是新生的一代，由5,4,3岁的细菌群落产生
      cur = ( timeline[(front+1)%5]+timeline[(front+2)%5]+timeline[(front+3)%5] )*m
      timeline[rear] = cur
      rear = (rear+1)%5   #enqueue
#      print front,rear,timeline
    for item in timeline:
      res += item
  else:
    for i in range(0,mon):
      res += timeline[i]

  return res

if __name__=='__main__':
  for i in range(1,11):
    print i,reproduct(i, 2)

