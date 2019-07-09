mylist=[]
mylist1=[]
mylist2=[]
mylist3=[]    
print("enter username")
username=input()
while username !="teacher1":
      username=input("username incorrect,try again: ")
print("username correct, now enter password")
password=input()
while password !="maths123":
    password=input("password incorrect,try again")
print("password correct,access granted")
while True:
    try:
        r = int(input("How Many students: "))
    except ValueError:
        print("Sorry, But that's not a number.")
        continue

    if r not in range(1,31):
        print("Sorry, But class size can only be between 1 and 30.")
        continue
    else:
        #if the size of the class is correct.
        #we're ready to exit the loop.
        break
for i in range(r):
    mylist.append(str(input('Enter The Name Of Student: ')))
    while True:
          try:
              r1 = int(input("Enter Results for fractions: "))
          except ValueError:
              print("Sorry, But that's not a number.")
              continue

          if r1 not in range(1,51):
              print("Sorry, But marks for fractions only be between 1 and 50.")
              continue
          else:
        #if the size of the class is correct.
        #we're ready to exit the loop.
              break
    mylist1.append(r1)
    while True:
          try:
              r2 = int(input("Enter Results for algebra: "))
          except ValueError:
              print("Sorry, But that's not a number.")
              continue

          if r2 not in range(1,51):
              print("Sorry, But marks for algebra only be between 1 and 50.")
              continue
          else:
        #if the size of the class is correct.
        #we're ready to exit the loop.
              break
    mylist2.append(r2)
    while True:
          try:
              r3 = int(input("Enter Results for trigonometry: "))
          except ValueError:
              print("Sorry, But that's not a number.")
              continue

          if r3 not in range(1,51):
              print("Sorry, But marks for trigonometry only be between 1 and 50.")
              continue
          else:
        #if the size of the class is correct.
        #we're ready to exit the loop.
              break
    mylist3.append(r3)
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
