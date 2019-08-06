m,n=12,1
a=[*range(n*m)]
X=[a[i::n] for i in range(n)]
for i in range(n):
 print(*X[i][::-1])