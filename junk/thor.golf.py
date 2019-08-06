r=input
a,b,c,d=[int(i)for i in r().split()]
while 1:
 r()
 e=a-c
 f=b-d
 x=y=""
 if e<0:x="W";c-=1
 elif e>0:x="E";c+=1
 if f<0:y="N";d-=1
 elif f>0:y="S";d+=1
 print(y+x)