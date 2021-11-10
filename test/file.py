#test number 1
a=0
for i in range(1,6):
    print(i, a)
    
#test number 2
summa=0
for i in range(1,100+1):
    summa+=i
print(summa)

#test number 3
a1=int(input())
a2=int(input())
a3=int(input())
if ((a1==a2) or (a1==a3) or (a2==a3)):
   print('yes')
else:
    print('ERROR')
    
#test number 4
a=int(input())
b=int(input())
c=int(input())
if ((a+b==c)or(a+c==b)or(b+c==a)):
    print('yes')
else:
    print('ERROR')

#Lesenka
n=int(input())
for i in range(1,n+1):
    for i2 in range(1,i+1):
        print(i2,sep='', end='')
    print()
