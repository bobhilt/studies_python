s='111111233441'
a=s[0]
for c in s[1:]:
 if a[-1] != c:
  a+=c
print(a)
