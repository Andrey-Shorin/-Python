import math
A = input()
B = A.split(' ')
A1=B[0].split('/')
A2=B[2].split('/')
if len(A1) == 2:
    A12=int(A1[1])
    A11=int(A1[0])
else:
    A11=(A1[0])
    A12=1
if len(A2) == 2:
    A22=int(A2[1])
    A21=int(A2[0])
else:
    A21=int(A2[0])
    A22=1
a = A12
A12=A12*A22
A11=A11*A22
A21=A21*a
if B[1] == '+':
    A11=A11+A21
else:
    A11=A11-A21
a= math.gcd(A11,A12)
A11=A11/a
A12=A12/a
if A11//A12 ==0:
    print(int(A11),int(A12),sep='/')
else:
    print(int(A11//A12),end = ' ')
    print(int(A11%A12),int(A12),sep='/')
