function = input('Введите ф-цию: ') #number 1
if function != '+' and '-' and '%' and '/' and '*':
    print('Ф-ція неправильна!')
number_1=int(input('Введите первое число: '))
number_2=int(input('Введите второе число: '))
if function == '+':
    print(number_1 + number_2)
if function == '-':
    print(number_1 - number_2)
if function == '%':
    print(number_1 % number_2)
if function == '/':
    print(number_1 / number_2)
if function == '*':
    print(number_1 * number_2)

a=int(input('катет 1: ')) #number 2
b=int(input('Катет 2 :'))
S=1/2*a*b
print(S)

zala1=int(input('1 зала - ')) #number3
zala2=int(input('2 зала - '))
zala3=int(input('3 зала - '))
zala4=int(input('4 зала - '))
zala=zala1+zala2+zala3+zala4
print (zala*2)

name=input('Твоє ім’я: ') #number 4
surname=input('Твоє прізвище: ')
age=input('Твій вік: ')
friend=input("Ім'я кращого друга: ")
colour=input('Улюблений колір: ')
animal=input('Улюблена тварина: ')
dream=input('Твоя мрія: ')
flower=input('Улюблена квітка: ')
star=input('Улюблена зірка: ')
print("Ім'я: "+name)
print('Прізвище: '+surname)
print('Вік:'+age)
print('Кращий друг: '+friend)
print('Кольор: '+ colour)
print('Тварина: ' +animal)
print('Мрія: '+dream)
print('Улюблена квітка: '+flower)
print('Зірка: '+star)

print('Введіть спочатку години а потім хвилини!') #number 5
hour=int(input('type a hour: '))
minute=int(input('type a minute: '))
if hour <= 24 and minute <=60:
    print((hour*60)+minute)
else:
    print('try again: ')
secunda=(hour*60*60)+(minute*60)
print(secunda)

number=input('type number: ') #number 6
print(number)

import math #number 7
a=int(input('a: '))
b=int(input('b: '))
print(math.gcd(a,b))

import math #number 8
x1=int(input())
x2=int(input())
y1=int(input())
y2=int(input())
AB=((x2-x1)**2)+((y2-y1)**2)
result=math.sqrt(AB)
print(result)
