#variables with chessboard pieces
r1=('[r1] ')
n1=('[n1] ')
b1=('[b1] ')
q=('[q ] ')
k=('[k ] ')
r2=('[r2] ')
n2=('[n2] ')
b2=('[b2] ')
#variables with pawns
psh1=('[p1] ')
psh2=('[p2] ')
psh3=('[p3] ')
psh4=('[p4] ')
psh5=('[p5] ')
psh6=('[p6] ')
psh7=('[p7] ')
psh8=('[p8] ')
#variables with first line of spaces
prop1=('[  ] ')
prop2=('[  ] ')
prop3=('[  ] ')
prop4=('[  ] ')
prop5=('[  ] ')
prop6=('[  ] ')
prop7=('[  ] ')
prop8=('[  ] ')
#variables with a second line of spaces
prop01=('[  ] ')
prop02=('[  ] ')
prop03=('[  ] ')
prop04=('[  ] ')
prop05=('[  ] ')
prop06=('[  ] ')
prop07=('[  ] ')
prop08=('[  ] ')
#variables with chessboard Pieces
R1=('[R1] ')
N1=('[N1] ')
B1=('[B1] ')
Q=('[Q ] ')
K=('[K ] ')
R2=('[R2] ')
N2=('[N2] ')
B2=('[B2] ')
#variables with Pawns
Psh1=('[P1] ')
Psh2=('[P2] ')
Psh3=('[P3] ')
Psh4=('[P4] ')
Psh5=('[P5] ')
Psh6=('[P6] ')
Psh7=('[P7] ')
Psh8=('[P8] ')
#variables with first line of Spaces
Prop1=('[  ] ')
Prop2=('[  ] ')
Prop3=('[  ] ')
Prop4=('[  ] ')
Prop5=('[  ] ')
Prop6=('[  ] ')
Prop7=('[  ] ')
Prop8=('[  ] ')
#variables with a second line of Spaces
Prop01=('[  ] ')
Prop02=('[  ] ')
Prop03=('[  ] ')
Prop04=('[  ] ')
Prop05=('[  ] ')
Prop06=('[  ] ')
Prop07=('[  ] ')
Prop08=('[  ] ')
#propusk
prop=('[  ] ')
#field
field=(r1+n1+b1+q+k+b2+n2+r2+'\n'
+psh1+psh2+psh3+psh4+psh5+psh6+psh7+psh8+'\n'
+prop1+prop2+prop3+prop4+prop5+prop6+prop7+prop8+'\n'
+prop01+prop02+prop03+prop04+prop05+prop06+prop07+prop08+'\n'
+Prop01+Prop02+Prop03+Prop04+Prop05+Prop06+Prop07+Prop08+'\n'
+Prop1+Prop2+Prop3+Prop4+Prop5+Prop6+Prop7+Prop8+'\n'
+Psh1+Psh2+Psh3+Psh4+Psh5+Psh6+Psh7+Psh8+'\n'
+R1+N1+B1+Q+K+B2+N2+R2+'\n')
#1   2   3   4   5   6   7   8
print(field)
#start
print('to start the game press "start"')
first=input()
while first=='start':
   figura=input('chose a figure - ') #figure name
   x1=int(input()) 
   y1=int(input()) 
   x2=int(input())
   y2=int(input())
   #pawms
   match figura:
       case 'psh1': #if figura pawn1
          if x1==x2 and y1-y2==1 or y1-y2==2: #check if a pawn can get there
            print('yes')
          else:
            print('no')
          if x1==x2:
             if y1==7 and y2==6: #if the pawn wants to move 1 square forward
              buf=psh1
              psh1=prop1 #swap them
              prop1=buf
             if y1==7 and y2==5: #if the pawn wants to move 2 square forward
              buf=psh1
              psh1=prop01 #swap them
              prop01=buf
             if y1==6 and y2==5: #if the pawn wants to move 2 square forward
              buf=prop1
              prop1=prop01 #swap them
              prop01=buf
       case'psh2': #if figura pawn2
          if x1==x2 and y1-y2==1 or y1-y2==2: #check if a pawn can get there
            print('yes')
          else:
            print('no')
          if x1==x2:
             if y1==7 and y2==6: #if the pawn wants to move 1 square forward
              buf=psh2
              psh2=prop2 #swap them
              prop2=buf
             if y1==7 and y2==5: #if the pawn wants to move 2 square forward
              buf=psh2
              psh2=prop02 #swap them
              prop02=buf
             if y1==6 and y2==5: #if the pawn wants to move 1 square forward
              buf=prop2
              prop2=prop02 #swap them
              prop02=buf
       case'psh3': #if figura pawn3
          if x1==x2 and y1-y2==1 or y1-y2==2: #check if a pawn can get there
            print('yes')
          else:
            print('no')
          if x1==x2:
             if y1==7 and y2==6: #if the pawn wants to move 1 square forward
              buf=psh3
              psh3=prop3 #swap them
              prop3=buf
             if y1==7 and y2==5: #if the pawn wants to move 2 square forward
              buf=psh3
              psh3=prop03 #swap them
              prop03=buf
             if y1==6 and y2==5: #if the pawn wants to move 1 square forward
              buf=prop3
              prop3=prop03 #swap them
              prop03=buf
       case'psh4': #if figura pawn4
          if x1==x2 and y1-y2==1 or y1-y2==2: #check if a pawn can get there
            print('yes')
          else:
            print('no')
          if x1==x2:
             if y1==7 and y2==6: #if the pawn wants to move 1 square forward
              buf=psh3
              psh4=prop4 #swap them
              prop4=buf
             if y1==7 and y2==5: #if the pawn wants to move 2 square forward
              buf=psh4
              psh4=prop04 #swap them
              prop04=buf
             if y1==6 and y2==5: #if the pawn wants to move 1 square forward
              buf=prop4
              prop4=prop04 #swap them
              prop04=buf
       case'psh5': #if figura pawn5
          if x1==x2 and y1-y2==1 or y1-y2==2: #check if a pawn can get there
            print('yes')
          else:
            print('no')
          if x1==x2:
             if y1==7 and y2==6: #if the pawn wants to move 1 square forward
              buf=psh5
              psh5=prop5 #swap them
              prop5=buf
             if y1==7 and y2==5: #if the pawn wants to move 2 square forward
              buf=psh5
              psh5=prop05 #swap them
              prop05=buf
             if y1==6 and y2==5: #if the pawn wants to move 1 square forward
              buf=prop5
              prop5=prop05 #swap them
              prop05=buf
       case'psh6': #if figura pawn6
          if x1==x2 and y1-y2==1 or y1-y2==2: #check if a pawn can get there
            print('yes')
          else:
            print('no')
          if x1==x2:
             if y1==7 and y2==6: #if the pawn wants to move 1 square forward
              buf=psh6
              psh6=prop6 #swap them
              prop6=buf
             if y1==7 and y2==5: #if the pawn wants to move 2 square forward
              buf=psh6
              psh6=prop06 #swap them
              prop06=buf
             if y1==6 and y2==5: #if the pawn wants to move 1 square forward
              buf=prop6
              prop6=prop06 #swap them
              prop06=buf
       case'psh7': #if figura pawn7
          if x1==x2 and y1-y2==1 or y1-y2==2: #check if a pawn can get there
            print('yes')
          else:
            print('no')
          if x1==x2:
             if y1==7 and y2==6: #if the pawn wants to move 1 square forward
              buf=psh7
              psh7=prop7 #swap them
              prop7=buf
             if y1==7 and y2==5: #if the pawn wants to move 2 square forward
              buf=psh7
              psh7=prop07 #swap them
              prop07=buf
             if y1==6 and y2==5: #if the pawn wants to move 1 square forward
              buf=prop7
              prop7=prop07 #swap them
              prop07=buf
       case'psh8': #if figura pawn8
          if x1==x2 and y1-y2==1 or y1-y2==2: #check if a pawn can get there
            print('yes')
          else:
            print('no')
          if x1==x2:
             if y1==7 and y2==6: #if the pawn wants to move 1 square forward
              buf=psh8
              psh8=prop8 #swap them
              prop8=buf
             if y1==7 and y2==5: #if the pawn wants to move 2 square forward
              buf=psh8
              psh8=prop08 #swap them
              prop08=buf
             if y1==6 and y2==5: #if the pawn wants to move 1 square forward
              buf=prop8
              prop8=prop08 #swap them
              prop08=buf
       case 'Psh1': #if figura pawn1
          if x1==x2 and y2-y1==1 or y2-y1==2: #check if a pawn can get there
            print('yes')
          else:
            print('no')
          if x1==x2:
             if y1==2 and y2==3: #if the pawn wants to move 1 square forward
              buf=Psh1
              Psh1=Prop1 #swap them
              Prop1=buf
             if y1==2 and y2==4: #if the pawn wants to move 2 square forward
              buf=Psh1
              Psh1=Prop01 #swap them
              Prop01=buf
             if y1==3 and y2==4: #if the pawn wants to move 2 square forward
              buf=Prop1
              Prop1=Prop01 #swap them
              Prop01=buf
       case 'Psh2': #if figura pawn1
          if x1==x2 and y2-y1==1 or y2-y1==2: #check if a pawn can get there
            print('yes')
          else:
            print('no')
          if x1==x2:
             if y1==2 and y2==3: #if the pawn wants to move 1 square forward
              buf=Psh2
              Psh2=Prop2 #swap them
              Prop2=buf
             if y1==2 and y2==4: #if the pawn wants to move 2 square forward
              buf=Psh2
              Psh2=Prop02 #swap them
              Prop02=buf
             if y1==3 and y2==4: #if the pawn wants to move 2 square forward
              buf=Prop2
              Prop2=Prop02 #swap them
              Prop02=buf
       case 'Psh3': #if figura pawn1
          if x1==x2 and y2-y1==1 or y2-y1==2: #check if a pawn can get there
            print('yes')
          else:
            print('no')
          if x1==x2:
             if y1==2 and y2==3: #if the pawn wants to move 1 square forward
              buf=Psh3
              Psh3=Prop3 #swap them
              Prop3=buf
             if y1==2 and y2==4: #if the pawn wants to move 2 square forward
              buf=Psh3
              Psh3=Prop03 #swap them
              Prop03=buf
             if y1==3 and y2==4: #if the pawn wants to move 2 square forward
              buf=Prop3
              Prop3=Prop03 #swap them
              Prop03=buf
       case 'Psh4': #if figura pawn1
          if x1==x2 and y2-y1==1 or y2-y1==2: #check if a pawn can get there
            print('yes')
          else:
            print('no')
          if x1==x2:
             if y1==2 and y2==3: #if the pawn wants to move 1 square forward
              buf=Psh4
              Psh4=Prop4 #swap them
              Prop4=buf
             if y1==2 and y2==4: #if the pawn wants to move 2 square forward
              buf=Psh4
              Psh4=Prop04 #swap them
              Prop04=buf
             if y1==3 and y2==4: #if the pawn wants to move 2 square forward
              buf=Prop4
              Prop4=Prop04 #swap them
              Prop04=buf
       case 'Psh5': #if figura pawn1
          if x1==x2 and y2-y1==1 or y2-y1==2: #check if a pawn can get there
            print('yes')
          else:
            print('no')
          if x1==x2:
             if y1==2 and y2==3: #if the pawn wants to move 1 square forward
              buf=Psh5
              Psh5=Prop5 #swap them
              Prop5=buf
             if y1==2 and y2==4: #if the pawn wants to move 2 square forward
              buf=Psh5
              Psh5=Prop05 #swap them
              Prop05=buf
             if y1==3 and y2==4: #if the pawn wants to move 2 square forward
              buf=Prop5
              Prop5=Prop05 #swap them
              Prop05=buf
       case 'Psh6': #if figura pawn1
          if x1==x2 and y2-y1==1 or y2-y1==2: #check if a pawn can get there
            print('yes')
          else:
            print('no')
          if x1==x2:
             if y1==2 and y2==3: #if the pawn wants to move 1 square forward
              buf=Psh6
              Psh6=Prop6 #swap them
              Prop6=buf
             if y1==2 and y2==4: #if the pawn wants to move 2 square forward
              buf=Psh6
              Psh6=Prop06 #swap them
              Prop06=buf
             if y1==3 and y2==4: #if the pawn wants to move 2 square forward
              buf=Prop6
              Prop6=Prop06 #swap them
              Prop06=buf
       case 'Psh7': #if figura pawn1
          if x1==x2 and y2-y1==1 or y2-y1==2: #check if a pawn can get there
            print('yes')
          else:
            print('no')
          if x1==x2:
             if y1==2 and y2==3: #if the pawn wants to move 1 square forward
              buf=Psh7
              Psh7=Prop7 #swap them
              Prop7=buf
             if y1==2 and y2==4: #if the pawn wants to move 2 square forward
              buf=Psh7
              Psh7=Prop07 #swap them
              Prop07=buf
             if y1==3 and y2==4: #if the pawn wants to move 2 square forward
              buf=Prop7
              Prop7=Prop07 #swap them
              Prop07=buf
       case 'Psh8': #if figura pawn1
          if x1==x2 and y2-y1==1 or y2-y1==2: #check if a pawn can get there
            print('yes')
          else:
            print('no')
          if x1==x2:
             if y1==2 and y2==3: #if the pawn wants to move 1 square forward
              buf=Psh8
              Psh8=Prop8 #swap them
              Prop8=buf
             if y1==2 and y2==4: #if the pawn wants to move 2 square forward
              buf=Psh8
              Psh8=Prop08 #swap them
              Prop08=buf
             if y1==3 and y2==4: #if the pawn wants to move 2 square forward
              buf=Prop8
              Prop8=Prop08 #swap them
              Prop08=buf
   #ladya1
       case'ladya1': #if figura ladya1
        if x1==x2 or y2==y1: #check if a ladya can get there
          print('yes')
        else:
          print('no')
        if psh1==prop and y1-y2==1: #if the ladya wants to move 1 square forward
            buf=r1
            r1=psh1 #swap them
            psh1=buf
        if prop1==prop and y1-y2==2: #if the ladya wants to move 2 square forward
            buf=r1
            r1=prop1 #swap them
            prop1=buf
   #ladya2
       case'ladya2': #if figura ladya1
        if x1==x2 or y2==y1: #check if a ladya can get there
          print('yes')
        else:
          print('no')
        if psh8==prop and y1-y2==1: #if the ladya wants to move 1 square forward
            buf=r2
            r2=psh8 #swap them
            psh8=buf
        if prop8==prop and y1-y2==2: #if the ladya wants to move 2 square forward
            buf=r2
            r2=prop8 #swap them
            prop8=buf
   #horse1
       case'horse1': #if figura horse
        if (abs(y1-y2)<=2 and abs(x1-x2)==1) and (x2==1 and y2==6):
            if prop1==prop:
                buf=n1
                n1=prop1 #swap them
                prop1=buf
        if (abs(y1-y2)<=2 and abs(x1-x2)==1) and (x2==3 and y2==6):
            if prop1==prop:
                buf=n1
                n1=prop3 #swap them
                prop3=buf
   #horse2
       case'horse2': #if figura horse
        if (abs(y1-y2)<=2 and abs(x1-x2)==1) and (x2==6 and y2==6):
            if prop6==prop:
                buf=n2
                n2=prop6 #swap them
                prop6=buf
        if (abs(y1-y2)<=2 and abs(x1-x2)==1) and (x2==8 and y2==6):
            if prop8==prop:
                buf=n2
                n2=prop8 #swap them
                prop8=buf
   field=(r1+n1+b1+q+k+b2+n2+r2+'\n'
+psh1+psh2+psh3+psh4+psh5+psh6+psh7+psh8+'\n'
+prop1+prop2+prop3+prop4+prop5+prop6+prop7+prop8+'\n'
+prop01+prop02+prop03+prop04+prop05+prop06+prop07+prop08+'\n'
+Prop01+Prop02+Prop03+Prop04+Prop05+Prop06+Prop07+Prop08+'\n'
+Prop1+Prop2+Prop3+Prop4+Prop5+Prop6+Prop7+Prop8+'\n'
+Psh1+Psh2+Psh3+Psh4+Psh5+Psh6+Psh7+Psh8+'\n'
+R1+N1+B1+Q+K+B2+N2+R2+'\n')
#1   2   3   4   5   6   7   8
   print(field)
