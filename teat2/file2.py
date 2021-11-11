#test number 1
a=int(input())
b=int(input())
c=int(input())
d=[]
if a>0:
    d.append(a)
if b>0:
    d.append(b)
if c>0:
    d.append(c)
print(d)

#test number 2
for i in range(1, 497+1):
    if i%2==0:
        print(i)
      
#test number 3
summa=0
for i in range(0, 14+1):
    summa+=i
print(summa)

#test number 4
start=1
for i in range(start, 9425+1):
       if i%2!=0:
           start*=i
print(start)

#test number 5
a=[]
for i in range(54, 9184+1):
    if i%5==0:
        a.append(i)
print(a)

