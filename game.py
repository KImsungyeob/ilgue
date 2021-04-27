name = input("이름을 입력하시오: ")
print(name, "님 반갑습니다. {0}(HP 100)으로 게임을 시작 합니다.".format(name))
print("길을 가다가 퉁퉁이를 만났습니다.")
print("퉁퉁이의 정보")
dict_a = {"name" : "이름:퉁퉁이"}
print(dict_a["name"])
list_a = [170, 90, 40]
print("퉁퉁이 키: " , list_a[0] ,"cm")
print("퉁퉁이 몸무게: " , list_a[1] ,"kg")
print("퉁퉁이 골격근량: " , list_a[2] ,"kg")
print("1. 싸운다 2. 도망간다")
num = int(input("선택: "))
if num == 1:
    print("퉁퉁이에게 이겼다!")
elif num == 2:
    print("도망가다 퉁퉁이에게 잡혀서 게임오버!")
else:
    print("입력 잘못 해서 게임 오버!")

def my(money):
    return money
print("이제 퉁퉁이한테 돈을 뜯어보자!")
money = input("뜯을 돈을 입력하세요")
print(money,"원을 뜯었다!")


