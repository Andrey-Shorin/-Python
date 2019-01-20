f = open('111.txt', 'r')
A ={a:[] for a in range(ord('А'), ord('Я')+1)}
for i in f:
     a = i
     if ord(a[0]) != 10:
         q =  ord(a[0])
         A[q].append(i)
for i in A.keys():
    d = open(chr(int(i)), 'x')
    b = A[i]
    for g in A[i]:
        d.write(str(g))
    d.close()
f.close()