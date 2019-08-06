p=print
w='Hello World!'
c='*'
n=4
def s():
 for _ in range(n):
  p(c*(2*n+2+len(w)))
s()
p(c*n+' '+w+' '+c*n)
s()