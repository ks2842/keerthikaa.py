niz1=input().split()
niz2=input().split()
niz3=input().split()
if(niz1[0]==niz2[0]==niz3[0] or niz1[1]==niz2[1]==niz3[1] or (niz1[0]==niz1[1] and niz2[0]==niz2[1] and niz3[0]==niz3[1])):
    print('yes')
else:
    print('no')
