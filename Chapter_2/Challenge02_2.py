# 피타고라스의 정리 공식에 따라 파이써능로 밑변과 높이를 입력하면 빗변의 길이를 구하는 프로그램을 만들어 보세요.

base = float(input("밑변의 길이를 입력해주세요 >> "))
height = float(input("높이의 길이를 입력해주세요 >> "))

Hypotenuse =(float)((base**2) + (height**2))**(1/2)

print(f"빗변의 길이는 {Hypotenuse} 입니다.")