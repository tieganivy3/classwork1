mylist=[]
mylist1=[]
mylist2=[]
mylist3=[]
r=int(input('How Many students: '))
#for r in range(1, 30):
if r not in range(1,30):
    print("wrong amount of students")
    r.append(input('wrong amount of students: '))
for i in range(r):

    mylist.append(input('Enter The Name Of Student: '))
    mylist1.append(int(input('Enter Results for fractions: ')))
    mylist2.append(int(input('Enter Results for algebra: ')))
    mylist3.append(int(input('Enter Results for trigonometry: ')))
print(mylist)
print(mylist1)
print(mylist2)
print(mylist3)
print("Good bye")
