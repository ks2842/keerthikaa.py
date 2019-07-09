pp=int(input())
for kk in range(2,pp+1):
  if(pp%kk==0):
      s=0
      for m in range(2,kk+1):
          if(kk%mm==0) and (mm!=kk):
              s=1
              break
      if(s==0):
          print(kk,end=' ')
