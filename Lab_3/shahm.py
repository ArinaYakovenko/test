figura=input('chose a figure - ') #name
x1=int(input())
y1=int(input())
x2=int(input())
y2=int(input())
if figura=='psh':
    if y1==2 and y2-y1==1 or 2:
      print('yes')
    elif x1==x2 and y2-y1==1:
      print('yes')
    else:
      print('no')
if figura=='ladya':
    if x1==x1 or x2==y1:
      print('yes')
    else:
      print('no')
if figura=='horse':
    if abs(y1-y2)<=2:
      print('yes')
    else:
      print('no')
if figura == 'slon':
    if abs(x1-x2)==abs(y1-y2):
      print('yes')
    else:
      print('no')
if figura=='king':
    if abs(x1-x2)<=1 and abs(y1-y2)<=1:
      print('yes')
    else:
      print('no')
if figura=='ferz':
    if abs(x1-x2)==abs(y1-y2) or (x1==x1 or x2==y1):
      print('yes')
    else:
      print('no')
