#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def hanoi(n,x,y,z):
    if n==1:
        print(x,'-->',z)
    else:
        hanoi(n-1,x,z,y)#将前n-1个盘子从x移动到y上
        hanoi(1,x,y,z) #将最底下的最后一个盘子从x移动到z上
        hanoi(n-1,y,x,z)#将y上的n-1个盘子移动到z上
n=int(input('请输入汉诺塔的层数：'))
hanoi(n,'a','b','c')


"""
hanoi(3,'a','b','c')
      ↓

              ↗ hanoi(1,'a','b','c') a-->c
hanoi(2,'a','c','b')→ hanoi(1,'a','c','b') a-->b
              ↘ hanoi(1,'c','a','b') c-->b


hanoi(1,'a','b','c')    a-->c


              ↗ hanoi(1,'b','c','a') b-->a
hanoi(2,'b','a','c')→ hanoi(1,'b','a','c') b-->c
              ↘ hanoi(1,'a','b','c') a-->c
"""
