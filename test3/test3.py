#test number 1
list=['1','2','3']
print(list[::-1])

#test number 2
lst=['1','2','3']
lst[0],lst[-1]=lst[-1],lst[0]
print(lst)

#test number 3
to_list=input()
list=[]
list.append(to_list)
print(list)

#test number 4
def useless(s):
    print(max(s)/len(s))
useless([1, 3, 6, 8, 9])
