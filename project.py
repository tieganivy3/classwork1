print("enter username")
username=input()
while username !="teacher1":
      username=input("username incorrect,try again")
print("username correct, now enter password")
password=input()
while password !="maths123":
    password=input("password incorrect,try again")
print("password correct,access granted")


print("enter amount of students")
students=input()
if students == "30":
      print("input topic 1")
      topic1=input()
      while topic1 !="fractions":
            topic1=input("wrong topic, try again")
            for counter in range(1,30):
                  input("enter students name")
            studentsname=input()
            results=int(input("enter results for topic 1"))
            if results <=51:
                  print("result invalid")

                  print("now enter second topic")
                  topic2=input()
                  while topic2 !="algebra":
                              topic2=input("wrong topic,try again")
                              input("enter students name")
                              studentsname=input()
                              results=int(input("enter results for topic 1"))
                              if results <=51:
                                    print("result invalid")
                                    
                                    print("now enter third topic")
                                    topic3=input()
                                    while topic3 !="trigonometry":
                                          topic3=input("wrong topic, try again")
                                          print("correct topic")
                                          input("enter students name")
                                          studentsname=input()
                                          results=int(input("enter results for topic 1"))
                                          if results <=51:
                                                print("result invalid")
