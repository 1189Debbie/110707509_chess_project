# -*- coding: utf-8 -*-
"""P1_4.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ofyWwQAozYuNiBR7MIn_bWrvLrsJOTYG
"""

checkerboard =[ [1, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 1, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0] ]

position1=input().split()
position2=input().split()

x1,y1 = int(position1[0]),int(position1[1])
x2,y2 = int(position2[0]),int(position2[1])

dx=abs(x2-x1)
dy=abs(y2-y1)

if (x1==x2 and y1==y2) or checkerboard[x2][y2]==1:
  print('No')
elif (dx==1 and dy==2) or (dx==2 and dy==1):
  print('Yes')
else:
  print('No')