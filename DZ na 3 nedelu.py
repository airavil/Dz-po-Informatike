#Простая задача

a=input('a = ')
b=input('b = ')
a, b= int(a,2), int(b,2)
c=str(bin(a+b))
print(c[2:len(c)+1])

#Более сложная задача

a=int(input())
if a == 1: print('A')
else:
    c=[]
    while a!=0:
        c.append(chr(a%26+64))
        a//=26
    c=c[::-1]
    while '@' in c:
        if c[0]=='A' and c[1]=='@':
            c.pop(0)
            c[0]='Z'
        else:
            b=c.index('@')
            c[b]='Z'
            c[b-1]=chr(ord(c[b-1])-1)
    c=''.join(c)
    print(c)

#Задача со *

l = int(input('left = '))
r= int(input('right = '))
if l > r: print('райт должен быть больше или равен лэфт')
else:
    c=l
    for i in range (l+1, r+1):
        c &= i
    print(c)