k=input()
b='0ABCDEFGHIJKLMNOPQRSTUVWXYZABC'
c=''
for i in k:
  if i in b:
    t=b.index(i)
    t=t+3
    c=c+b[t]
print(c)
