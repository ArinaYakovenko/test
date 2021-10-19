list_guests=['olya','nastya','sergey','natasha']
list_guests[1]='yula' #added new name 
print(list_guests)
guest_0='hello my dear ' + list_guests[0].title() #list by guest
guest_1='hello my dear ' + list_guests[1].title()
guest_2='hello my dear ' + list_guests[2].title()
guest_3='hello my dear ' + list_guests[3].title()
print(guest_0)
print(guest_1)
print(guest_2)
print(guest_3)
print('Nastya, waiting for you next time!')
print('I will a new, more bigger list guests:')
list_guests.insert(0, 'vika') #added new guest in first
list_guests.insert(3, 'david') #added guest in middle
list_guests.append('lera') #added guest at the and 
print(list_guests)
print('Ssory, but I must have 2 guest :(')
guest_00='i am sorry ' + list_guests[0].title() + '. See you late:('
guest_01='i am sorry ' + list_guests[1].title() + '. See you late:('
guest_02='i am sorry ' + list_guests[2].title() + '. See you late:('
guest_03='i am sorry ' + list_guests[3].title() + '. See you late:('
guest_04='I am waiting for you at my place at 16:00 ' + list_guests[0].title()
guest_05='I am waiting for you at my place at 16:00 ' + list_guests[1].title()
list_guests.pop() #delite guest
list_guests.pop(-1)
list_guests.pop(-2)
list_guests.pop(-3)
list_guests.pop(2)
print(list_guests)
print(guest_00)
print(guest_01)
print(guest_02)
print(guest_03)
print(guest_04)
print(guest_05)
del list_guests[0] # delite guest
print(list_guests)
del list_guests[0] #delite guest
print(list_guests)

print(len(list_guests))