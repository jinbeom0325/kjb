#변수
#변수에는 모든 자료형의 값을 저장할 수 있다.
#변수의 선언
#변수의 생성
# x= 10
# a= 20
# abc= 30
# 복합 대입 연산자
# a=100
# print(a,15)
# a+=100
# print(a,18)
# a**=10
# print(a)
# b="안녕하세요"
# b*=2
# print(b)
# b+="안녕"
# print(b)
# from curses.ascii import isalnum
# from idlelib.pyshell import restart_line

# number= 100
# number+=10
# number+=20
# number+=30
# print("number:",number)
# number:160

# 데이터타입에는
# 숫자: + - * / // % **
# 문자열: 연결(문자+문자) 반복(문자*숫자)
# 문자열에 += *=가능
# str1="안녕하세요"
# str1+="!"
# str1*=2
# print("str1=",str1)

# 사용자 입력 input()
# 식별자 뒤에 괄호=>함수

#사용자로부터 입력을 받아 활용하는 방법
# 파이썬: 인터프리터 방식 원시코드 -> 기계어

# int_a=int(input("입력a"))
# print(type(int_a))

# 두 수를 입력받아 합해서 출력1
# name=input("숫자입력1>")
# name2=input("숫자입력2>")
# print(float(name)+int(name2))

# 두 수를 입력받아 합해서 출력2
# name3=input("숫자입력1")
# int_name3 = int(name3)
# name4=input("숫자입력2")
# int_name4 = int(name4)
# print("숫자형:",int_name3+int_name4)
# print("문자형:",name3+name4)

# 두 수를 입력받아 합해서 출력3 간단하게
# result=int(input("숫자입력1"))+int(input("숫자입력2"))
# print(result)

# result=float(input("실수입력:"))
# print(result)
# print(result+100)
# 정수+실수연산 = 실수형태
# print(int(result+100))
# print(type(type(result)))

# input_a = float(input("첫 번째 숫자>"))
# input_b = float(input("두 번째 숫자>"))
# print("덧셈 결과:",input_a+input_b)
# print("뺄셈 결과:",input_a-input_b)
# print("곱셈 결과:",input_a*input_b)
# print("나눗셈 결과:",input_a/input_b)

#문자열을 int로 변환할 수 있는 것: "123" 없는 경우: "abc"
#숫자를 문자열로 바꾸기
# a= 32
# print(type(a))
# a= str(32)
# print(type(a))
# print(type(str(int(input("str함수 테스트")))))
# print("52.273"[3:6])

# raw_input = input("inch 단위의 숫자를 입력해주세요.:")
# inch = int(raw_input)
# cm = inch * 2.54
# print(inch,"inch는 cm단위로",cm,"cm입니다.")

#사용자 입력으로 키(m)와 체중(kg)을 입력 받아서 BMI 결과 출력 코드 BMI = 체중/신장의 제곱
# h = float(input("키를 입력해주세요."))
# w= int(input("체중을 입력해주세요."))
#
# bmi= w/h**2
# print("BMI결과",bmi)

# 스왑
# a=input("문자1")
# b=input("문자2")
# print(a,b)
# c=a
# a=b
# b=c
# print(a,b)

# "안녕하세요".find() #문자열 전용 함수
# print()#문자열 함수
# input()
# .찍고 사용하는 함수는 .앞 데이터 형태 전용 함수라고 생각

#문자열 format()함수

# xx="{1}{0}{2}".format(10,"포맷",20)
# print(xx)

# format_a = "{}만 원".format(5000)
# format_b = "파이썬 열공하여 첫 연봉 {}만 원 만들기".format(5000)
# format_c="{} {} {}".format(3000,4000,5000)
# format_d = "{} {} {}".format(1,"문자열",True)
#
# print(format_a)
# print(format_b)
# print(format_c)
# print(format_d)

# bmi계산에 format함수 활용 사용자 입력 이름/키/체중
# name=input("사용자 이름입력:")
# h=float(input("키를 입력(m):"))
# w=int(input("몸무게 입력(kg):"))
# bmi= w/h**2
# format_a = "{}님의 bmi는 {}입니다.".format(name,bmi)
# print(format_a)

# 간단하게
# name=input("이름입력:")
# result=int(input("몸무게 입력(kg):"))/float(input("키입력(m):"))**2
# format_a = "{}님의 bmi는 {}입니다.".format(name,result)
# print(format_a)

# output_h = "{:+5d}".format(52) # +는 부호표현
# output_i = "{:+5d}".format(-52)
# output_j = "{:=+5d}".format(52) # =+ 부호앞으로출력
# output_k = "{:=+5d}".format(-52)
# output_l = "{:+05d}".format(52)
# output_m = "{:+05d}".format(-52)
# print("#조합하기")
# print(output_h)
# print(output_i)
# print(output_j)
# print(output_k)
# print(output_l)
# print(output_m)
#
# output_a = "{:15.3f}".format(52.273)
# output_b = "{:15.2f}".format(52.273)
# output_c = "{:15.1f}".format(52.273)
# output_d = "{:2.1f}".format(52.273)
# print(output_a)
# print(output_b)
# print(output_c)
# print(output_d)

# output_a = 52.0
# output_b = "{:g}".format(output_a) #소수점 표시 안함
# print(output_a)
# print(output_b)

# print("hello".upper()) #아스키코드 -32
# print("hello".lower())

#문자열 공백제거 strip()
# input_a = """
#         안녕하세요
#         문자열의 함수를 알아봅니다
# """
# print(input_a)
# print(input_a.strip())

#문자열 구성 파악
# print("123".isdigit())
# v= int(input("번호를 입력하세요"))
# print(v)

#문자열 찾기 find()
#문자열 내부에 특정 문자가 어디에 있는지 위치 리턴
# output_1 = "안녕안녕하세요".find("안녕")
# print(output_1)
# output_2 = "안녕안녕하세요".rfind("안녕")
# print(output_2)

# 문자열과 in연산자   있는지 여부 T/F
# print("안녕" in "안녕하세요")

#문자열 자르기 split()
# print(type("10 20 30 40 50".split(" ")))

# f-스트링 표기
# print(f"문자열={int(3+7)}")

#구의 부피와 겉넓이
# pi =3.141592
# r= float(input("구의 반지름을 입력해주세요:"))
#
# qnvl=(4/3)*pi*(r**3)
# rjxsjfqdl=4*pi*r**2
# print(f"구의 부피는 {qnvl}입니다.")
# print(f"구의 겉넓이는 {rjxsjfqdl}입니다.")

#피타고라스 정의
# alxqus = float(input("밑변의 길이를 입력해주세요:"))
# shvdl = float(input("높이의 길이를 입력해주세요:"))
#
# qltqus = (alxqus**2 + shvdl**2)**(1/2)
# print(f"빗변의 길이는 {qltqus}입니다.")

# pi =3.141592
# r= float(input("구의 반지름을 입력해주세요:"))
# qnvl=(4/3)*pi*(r**3)
# rjxsjfqdl=4*pi*r**2
# a = "구의 부피는 {}입니다.".format(qnvl)
# b = "구의 겉넓이는 {}입니다.".format(rjxsjfqdl)
# print(a)
# print(b)

#불 자료형과 if 조건문
# print(10==100)
# print("가방"<"하마")
# x=25
# print(10<x<30)

# 논리연산자 not and or
# x=10
# under_20 = x<20
# print("under_20:", under_20)
# print("not under_20:", not under_20)

# if 100==100:
#     print("123")

# 사용자 입력받기
# 숫자로만 구성되어 있다면 "숫자입니다"텍스트와
# 실제 숫자로 변환해서 30을 더한값을 한줄에 출력한다.
# 그렇지 않으면 무시
# a=input("숫자를 입력하세요:")
# if a.isdigit():
#     print("숫자입니다.{}".format(int(a)+30))
#     print(f"숫자입니다 {int(a)+30}")

#입력을 받습니다.
# number = input("정수 입력> ")
# number = int(number)
# if number > 0:  #양수조건
#     print("양수입니다")
# if number < 0:  #음수조건
#     print("음수입니다")
# if number == 0:  # 0조건
#     print("0입니다")

# x=int(input("숫자를 입력"))
#
# if x%2==0:
#     print("짝수")


# x=input("숫자를 입력")
# if x[-1] in "02468":
#     print("짝수")
#
# x=input("숫자입력")
# if x[-1]=="0":
#     print("0으로 끝나는 짝수")