lt=[]
space=5*2-2
for l in range(1,5+1):
    v=''
    for sp in range(space):
        print('',end='')
        v+=''
    space=space-2
    for c in range(l):
        print(c,end=' ')
        v+=str(c)+' '
    lt.append(v)
    print()
print(lt)
for i in lt:
    print(i)