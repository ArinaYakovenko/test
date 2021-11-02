a=int(input()) #1
b=int(input())
c=int(input())
if a>b and a>c :
    print('Найбільше число: ',a)
elif b>a and b>c:
    print('Найбільше число: ',b)
else:
    print('Найбільше число: ',c)
if a<b and a<c :
    print('Найменше число: ',a)
elif b<a and b<c:
    print('Найменше число: ',b)
else:
    print('Найменше число: ',c)

import math #2
a=float(input())
b=float(input())
c=float(input())
Deskrimenant = (b**2) -4*(a*c)
if Deskrimenant <=0:
    print("Дискримінант не може бути війд'ємним!")
D=math.sqrt(Deskrimenant)
if D<0:
    print('Рівняння не має коренів!')
elif D==0:
    print('Рівняння має 1 корінь: ')
    x = -b / (2 * a)
    print('x = ' + str(x))
else:
    print('Рівняння має 2 корені: ')
    x1 = (-b + D ** 0.5) / (2 * a)
    x2 = (-b - D ** 0.5) / (2 * a)
    print('x₁ = ' + str(x1))
    print('x₂ = ' + str(x2))

a=int(input('Ввід: ')) #3
b=range(1, a+1)
i=[]
for c in b:
    if a%c==0:
        i.append(c)
print('Ввивід:'+str(i))

d=[] #4
a=int(input('Перше число - '))
b=int(input('Друге число - '))
c=int(input('Третє число - '))
d.append(a)
d.append(b)
d.append(c)
d1=set(d)
print('К-сть НЕ одинакових чисел:')
print(len(d1))

number1=int(input()) #5
number2=int(input())
number3=int(input())
number4=int(input())
parni=[]
ne_parni=[]
if number1%2==0:
    parni.append(number1)
else:
    ne_parni.append(number1)
if number2%2==0:
    parni.append(number2)
else:
    ne_parni.append(number2)
if number3%2==0:
    parni.append(number3)
else:
    ne_parni.append(number3)
if number4%2==0:
    parni.append(number4)
else:
    ne_parni.append(number4)
print('Парні числа: '+ str(parni))
print('Не парні числа: '+ str(ne_parni))

right=[] #6
not_right=[]
question1=('Скільки буде 2*2?') 
print(question1)
variable=('''a) 2
б) 4
в) 5''')
print(variable)
reply=input('Ваша відповідь: ')
if reply == 'б':
    right.append(1)
else:
    not_right.append(1)
question2=('\nСкільки буде 7*8?') 
print(question2)
variable=('''a) 56
б) 52
в) 50''')
print(variable)
reply=input('Ваша відповідь: ')
if reply == 'а':
    right.append(1)
else:
    not_right.append(1)
question3=('\nСкільки буде 5*5?') 
print(question3)
variable=('''a) 10
б) 30
в) 25''')
print(variable)
reply=input('Ваша відповідь: ')
if reply == 'в':
    right.append(1)
else:
    not_right.append(1)
question4=('\nСкільки буде 10*10?') 
print(question4)
variable=('''a) 100
б) 1000
в) 200''')
print(variable)
reply=input('Ваша відповідь: ')
if reply == 'а':
    right.append(1)
else:
    not_right.append(1)
question5=('\nСкільки буде 6*4?') 
print(question5)
variable=('''a) 24
б) 42
в) 15''')
print(variable)
reply=input('Ваша відповідь: ')
if reply == 'а':
    right.append(1)
else:
    not_right.append(1)
question1=('\nСкільки буде 25*5?') 
print(question1)
variable=('''a) 255
б) 445
в) 125''')
print(variable)
reply=input('Ваша відповідь: ')
if reply == 'в':
    right.append(1)
else:
    not_right.append(1)
print('Правильні відповіді: ')
print(len(right))
print('Не павильні відповіді: ')
print(len(not_right))

print('Відповідь має бути так або ні!')
start=50
result=[]
name=input("\nВведіть ваше ім'я - ")
que1=input('\nВам э 18 років? - ')
if que1 == 'так':
    result.append(10)
else:
    result.append(0)
que2=input('\nВи знаєте що таке кофе-машина? - ')
if que2 == 'так':
    result.append(10)
else:
    result.append(0)
que3=input('\nМолоко потрібно взбивати менше 15 хвилин - ')
if que3 == 'ні':
    result.append(10)
else:
    result.append(0)
que4=input('\nСироп добавляють з початку - ')
if que4 == 'так':
    result.append(10)
else:
    result.append(0)
que5=input('\nКапучино роблять з молоком? - ')
if que5 == 'так':
    result.append(10)
else:
    result.append(0)
result=sum(result)
if result == start:
    print(name+ ' \nВи прийняті!')
else:
    print('\nВаш результат: ' + str(result) + '/' + str(start))
print('Вибачте, але ви нам не підходите:(')

name=input("Ім'я - ") #8
surname=input('Призвіще - ')
fake_name1=('Аріна')
fake_surnae1=('Яковенко')
fake_name2=('Іван')
fake_surnae2=('Франко')
if name == fake_name1 and surname == fake_surnae1 or name == fake_name2 and surname == fake_surnae2:
    print('Ви у розшуку!')
else:
    print(surname+' '+name + '. Гарного дня!')
