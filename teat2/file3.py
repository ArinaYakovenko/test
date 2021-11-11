#test number 1
n = int(input())
factorial = 1
while n > 1:
    factorial *= n
    n -= 1
print(factorial)

#test number 2
n=int(input())
a=n%10
b=n%100//10
c=n//100 
print(a+b+c)
print(a*b*c)

#test number 3
min=int(input('Min: '))
max=int(input('Max: '))
shag=int(input('Shag: '))
for i in range(min, max+1, shag):
    print(i)
