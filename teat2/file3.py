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

#test number 4
from random import randint
random=randint(1,13)
a=11
pop=int(input('Відгадайте число! '))
while pop !=random and a!=20:
    print('Спробуй знову:( ')
    if pop == random:
        print('Ви виграли!')
    elif pop < random:
        print('Загадане число більше!')
    elif pop >random:
        print('Загадане число меньше!')
    pop=int(input('Нове число: '))
    a+=1
print('Спроби закінчились!')
