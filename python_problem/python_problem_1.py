import random 

num = 0
orderA = 0


def brGame():
  global num
  global orderA
  orderA += 1
  if(orderA%2 ==0):
    n = input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) : ")
    while(n != '1' and n != '2' and n != '3'):
      if(not(n.isdigit())):
        n = input("정수를 입력하세요 : ")
      else:
        n = input("1, 2, 3 중 하나를 입력하세요 : ")
  else:
    n = random.randint(1,3)
  

  #n입력 받은만큼 숫자 출력
  if(orderA%2 ==0):
    for i in range(int(n)):
      num += 1
      print("playerA : {}".format(num))
      if(num == 31):
        print("computer win!")
        break
  else:
    for i in range(int(n)):
      num += 1
      print("computer : {}".format(num))
      if(num == 31):
        print("player win!")
        break 
  


while(num < 31):
  brGame()
  