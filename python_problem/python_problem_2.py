#함수 이름은 변경 가능합니다.

##############  menu 1
def Menu1(std) :
  #사전에 학생 정보 저장하는 코딩
  name_space.append(std[0])
  score1_space.append(int(std[1]))
  score2_space.append(int(std[2]))


##############  menu 2
def Menu2() :
  n = len(grade)
  for i in range(len(grade),len(name_space)):
    if (score1_space[i] + score2_space[i] >= 180):
      grade.append('A')
    elif(score1_space[i] + score2_space[i] >= 160):
      grade.append('B')
    elif(score1_space[i] + score2_space[i] >= 140):
      grade.append('C')
    else:
      grade.append('D')

##############  menu 3
def Menu3() :
  print("--------------------------------")
  print("name       mid   final   grade")
  for i in range(len(name_space)):
    print('{:<10} {:<6} {:<8} {:<6}'.format(name_space[i],score1_space[i],score2_space[i],grade[i]))
  



##############  menu 4
def Menu4(name_del):
  #학생 정보 삭제하는 코딩
  i = name_space.index(name_del)
  # print(name_space,'/',score1_space,'/',score2_space,'/',grade)
  # print(i)

  name_space.pop(i); score1_space.pop(i); score2_space.pop(i); 
  if(len(grade) >= i+1):
    grade.pop(i)
  # print(name_space,'/',score1_space,'/',score2_space,'/',grade)

#학생 정보를 저장할 변수 초기화
name_space = []
score1_space = []
score2_space = []
grade =[]
print("*Menu*******************************")
print("1. Inserting students Info(name score1 score2)")
print("2. Grading")
print("3. Printing students Info")
print("4. Deleting students Info")
print("5. Exit program")
print("*************************************")
while True :
  choice = input("Choose menu 1, 2, 3, 4, 5 : ")
  if choice == "1":
    #학생 정보 입력받기
    
    student = input("Enter name mid-score final-score : ").split()

    #예외사항 처리(데이터 입력 갯수, 이미 존재하는 이름, 입력 점수 값이 양의 정수인지)
    if(len(student)!=3):
      print("Num of data is not 3!")
      continue
    elif(student[0] in name_space):
      print("Already exist name!")
      continue
    elif(not(student[1].isdigit()) or not(student[2].isdigit()) or int(student[1]) <= 0 or int(student[2]) <=0):
      print("Score is not positive integer!")
      continue
    Menu1(student)


  elif choice == "2" :
    #예외사항 처리(저장된 학생 정보의 유무)
    if(len(name_space) == len(grade)):
      print("No student data!")
      continue
    #예외사항이 아닌 경우 2번 함수 호출
    #"Grading to all students." 출력
    Menu2()
    print("Grading to all students.")
    
  elif choice == "3" :
    #예외사항 처리(저장된 학생 정보의 유무, 저장되어 있는 학생들의 학점이 모두 부여되어 있는지)
    if(not(name_space)):
      print("No student data!")
      continue
    elif(len(name_space) != len(grade)):
      print("There is a student who didn't get grade.")
      continue
    #예외사항이 아닌 경우 3번 함수 호출
    Menu3()
    
  elif choice == "4" :
    #예외사항 처리(저장된 학생 정보의 유무)
    if(not(name_space)):
      print("No student data!")
      continue
    #예외사항이 아닌 경우, 삭제할 학생 이름 입력 받기
    name = input("Enter the name to delete : ")
    #입력 받은 학생의 존재 유무 체크 후, 없으면 "Not exist name!" 출력
    if(not(name in name_space)):
      print("No exist name!")
      continue
    #있으면(예를 들어 kim 이라 하면), 4번 함수 호출 후에 "kim student information is deleted." 출력
    Menu4(name)
    print("{} student information is deleted.".format(name))

  elif choice == "5" :
    #프로그램 종료 메세지 출력
    print("Exit Program")
    #반복문 종료
    break
    
  else:
    #"Wrong number. Choose again." 출력
    print("Wrong number. Choose again.")
    
