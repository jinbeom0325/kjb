# print("Python programming")
# 10+20
import keyword
# print(keyword.kwlist)

#변수 저장공간
#변수 생성에 식별자 사용
# false=10
# b=20
# print(false+b)

# ---식별자규칙-----
# 1키워드 x
# 2특수문자 _만 허용
# 3숫자로 시작x
# 4공백 포함x
# 5한국어x
# 6대소문자 구분
# ----------------

# a=10
# _A=20
# print(a)
# print(_A)

# print(52)
# print(273)
# print(52,273,"Hello")
# print()

#하나만 출력합니다.
# print("#하나만 출력합니다.")
# print("Hello python Programming...!")
# print()
#
# 여러 개를 츨력합니다.
# print("#여러 개를 출력합니다.")
# print(10,20,30,40,50)
# print("안녕하세요","저의","이름은","윤인성입니다!")
# print()
#
# 아무것도 입력하지 않으면 단순하게 줄바꿈합니다.
# print("#아무것도 출력하지 않습니다.")
# print("---확인 전용선---")
# print()
# print()
# print("---확인 전용선---")

# print(type("안녕하세요"))
# print(type(273))
# print(type(print(123)))

# ---문자열 표현 방법---
# 따옴표로 감싸 표현
# print('"안녕하세요"라고 말했습니다.')
# print('\'안녕하세요 라고 말했다\'')
# print("안녕하세요\n안녕")
# print('\\ \\ \\ \\')
# print(3*"301")
# print('''\안녕하세요안녕하세요안녕하
# 세요안녕하세요
# 안녕하세요안
# 녕하
# 세요\
# ''')

# 문자 선택 연산자: 인덱싱 []
# 문자 선택 연산자는 문자열 내부 특정 하나의 문자만 선택하는 연산자
# 대괄호 안에 선택할 문자의 번호를 입력
# 위 문자의 번호를 인덱스 번호라고 표현
# print("301호"[0])

# 슬라이싱
# print("안녕하세요"[-4:-2])
# print("안녕하세요"[:])
# print("안녕"[10]) index out of range 범위 벗어남

# 길이
# print(len("안녕"))

# print(type(type(len("안녕"))))
# x="엑스"
# print(x)
# print(type(x))

# print(type(3)) #int
# print(type(0.0)) #float
#
# 숫자연산은 숫자끼리
# print("5+7=",5+7)
# print("5-7=",5-7)
# print("5*7=",5*7)
# print("5/7=",5/7) #소수점 이하의 자릿수를 떼어 버린 후 정수 부분만 남김:몫

#제곱 print(10**2)
#연산자 우선순위
# print("안녕"+"하세요"*3)
# print(("안녕"+"하세요")*3)
# print("안녕"+("하세요"*3))

#변수 선언과 할당
# pi =3.14159265
# r = 10
# 변수 참조
# print("원주율=",pi)
# print("반지름=",r)
# print("원의둘레=", 2*pi*r)
# print("원의 넓이=", pi*r*r)