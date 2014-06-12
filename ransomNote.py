#!/usr/bin/python
# Given a string of arbitrary words, decide whether you can write a specified ransom note by cutting letters from it.

import string

def ransomNote(note,s):
  ss=s.replace(' ','').lower()
  ns=note.replace(' ','').lower()
  sn=len(ss)
  nn=len(ns)
  table={}
  for letter in string.lowercase:
    table[letter]=0
  j=0
  for i in ns:
    if(table[i]>0):
      table[i]-=1
    else:
      while(ss[j]!=i):
        table[ss[j]]+=1
        j+=1
        if(j==sn):
          return False
  return True

note1='no scheme'
s='programming interviewers are wired'
print '''to write "%s" out of "%s" is'''%(note1,s),ransomNote(note1,s)
note2='is pamm'
print '''to write "%s" out of "%s" is'''%(note2,s),ransomNote(note2,s)
