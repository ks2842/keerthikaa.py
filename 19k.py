pp=int(input())
for k in range(2,pp+1):
  if(pp%k==0):
      s=0
      for m in range(2,k+1):
          if(k%mm==0) and (mm!=k):
              s=1
              break
      if(s==0):
          print(kk,end=' ')
