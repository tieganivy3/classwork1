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
    mylist.append(str(input('Enter The Name Of Student: ')))
    mylist1.append(int(input('Enter Results for fractions: ')))
    mylist2.append(int(input('Enter Results for algebra: ')))
    mylist3.append(int(input('Enter Results for trigonometry: ')))
def Average(mylist1):
    return sum(mylist1) / len(mylist1)
average = Average(mylist1)
print("Average of the fractions =", round(average, 2))
def Average(mylist2):
    return sum(mylist2) / len(mylist2)
average2 = Average(mylist2)
print("Average of the algebra =", round(average2, 2))
def Average(mylist3):
    return sum(mylist3) / len(mylist3)
average3 = Average(mylist3)
print("Average of the trigonometry =", round(average3, 2))
print(mylist)
print(mylist1)
print(mylist2)
print(mylist3)
print("Good bye")
