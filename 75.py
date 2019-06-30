p=str(input())
q=list(p)
r=len(p)
s=""
if r % 2==0:
   q[int(r/2)]="*"
   q[int((r/2)-1)]="*"
else:
   q[int(r/2)]="*"
s=s.join(q)
print(s)
