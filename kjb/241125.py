import datetime
from calendar import weekday
from difflib import restore
from itertools import count

# import는 라이브러리,패키지,모듈을 불러오기
# 기본 내장이 아닌 외부 기능 모음
# 날짜/시간 관련 기능 모음을 불러옴
# 기본 내장이 아님, 불러오고 사용가능

# now = datetime.datetime.now()  #모듈>클래스>매서드
# print(type(now))               #now 변수에 담긴 것은 datetime.datetime객체
# print(now.year,"년")           #year=조회함
# print(now.month,"월")
# print(now.day,"일")
# print(now.hour,"시")
# print(now.minute,"분")
# print(now.second,"초")

# now=datetime.datetime.now()
# print("{}년 {}월 {}일 {}시 {}분 {}초".format(
#     now.year,
#     now.month,
#     now.day,
#     now.hour,
#     now.minute,
#     now.second))
# print(f"{now.year}년 입니다.")

# now=datetime.datetime.now()
# if now.hour <12:
#     print("현재 시각은 {}시로 오전입니다!".format(now.hour))
#
# if now.hour >= 12:
#     print("현재 시각은 {}시로 오후입니다!".format(now.hour))


# now = datetime.datetime.now()
# if now.month==11 and now.hour<12 and now.weekday()==0:
#     print(f"{now.month}월 {now.weekday()}요일 오전 {now.hour}시")

# zero = 0
# str1=""
# list1=[]
# false = False
# none= None #특수한 빈값타입
# print(zero==false) #t
# print(zero==none)   #f
# print(false==none) #f
# print(str1==false) #f print안에는 빈문자열이나 빈리스트는 False로 변경안됨
# print(type(none))

# else 조건문 활용
# else문은 if조건문 뒤에 사용
# if조건이 거짓(false)일 때 실행된다
# number = input("정수입력>")
# number = int(number)
# if number%2==0:
#     print("짝수")
# else:
#     print("홀수")

# elif구문
# 두 가지로 구분되지 않는 조건문 작성에 사용
# elif로 조건을 추가
# if와 else 사이에 위치
# elif는 여러개 가능

# now = datetime.datetime.now()
# month = now.month
# if 3<= month <= 5:
#     print("현재는 봄입니다.")
# elif 6<=month<=8:
#     print("현재는 여름입니다.")
# elif 9<= month <11:
#     print("현재는 가을입니다.")
# else:
#     print("현재는 겨울입니다.")

# if score==4.5
#     print("1")
# elif 4.2<=score:
#     print("2")

# pass 키워드
# 조건문 내 실행문이 없는 경우 오류 나지 않게 처리, 임시처리
# if문은 내부 실행문 없으면 문법적 오류가 발생
# if socre==4.5
#     pass
# elif 4.2<=score
#-------------도전문제----------------#
# res=input("입력:")
# now=datetime.datetime.now()
# if res in "안녕":
#     print("안녕하세요.")
# elif res in "몇 시":
#     print("지금은 {}시 입니다".format(now.hour))  #datetime.datetime.now.hour()
# else :
#     print(res)
#
# res=int(input("정수를 입력해주세요:"))
# if res%2==0:
#     print(f"{res}은 2으로 나누어 떨어지는 숫자입니다.")
# else :
#     print(f"{res}은 2으로 나누어 떨어지는 숫자가 아닙니다.")
#
# if res%3==0:
#     print(f"{res}은 3으로 나누어 떨어지는 숫자입니다.")
# else:
#     print(f"{res}은 3으로 나누어 떨어지는 숫자가 아닙니다.")
#
# if res % 4 == 0:
#     print(f"{res}은 4으로 나누어 떨어지는 숫자입니다.")
# else:
#     print(f"{res}은 4으로 나누어 떨어지는 숫자가 아닙니다.")
#
# if res % 5 == 0:
#     print(f"{res}은 5으로 나누어 떨어지는 숫자입니다.")
# else:
#     print(f"{res}은 5으로 나누어 떨어지는 숫자가 아닙니다.")
# --------------------------------------#
#리스트:숫자,문자열,불 처럼 데이터 타입 중 하나 [1,2,3,4,5]표현, 여러가지 자료를 저장
#요소:리스트 데이터 타입 내부 단일 데이터
#인덱스:0번부터 시작하는 요소 번호
#for반복문:특정 실행문을 반복 수행하기 위한 문법
# 리스트는 내부 요소를 인덱싱을 통해 접근(조회),수정 가능

# array = [273,32,103,"문자열",True,False]
# print(array[:-2])
# 2중 인덱스 문자열
# print(array[-3][0])

#리스트 연산자 + * len()
# lista=[1,2,3]
# listb=[4,5,6]
# a="hello"
# print(lista+listb)
# print(a.upper())
# print(a.find("e"))
# lista[0]=100
# print(lista)
# print(a.replace("h","a"))
#

# 리스트 관련 함수

# 1.리스트명.append() 요소 추가           원본변형
# lista.append(4)
# print(lista)

# 2.리스트명.insert(위치,요소) 특정 위치에 요소 추가
# lista=[1,2,3]
# lista.insert(0,10)
# print(lista)

# 3.리스트명.extend() +연산자와 같음        원본변형
# lista.extend([5,6,7])
# print(lista)

# lista=[1,2,3]
# listb=[4,5,6]

# 4.del 리스트명[인덱스]
# del lista[0]    #명령이라 바로 print못함
# print(lista)
# 리스트명.pop(인덱스)
# lista.pop()     #인덱스 안쓰면 -1이 디폴트값
# print(lista)

# 5. 리스트명.remove(값) 리스트 값이 여러개이면 가장 먼저 발견된 것 제거
# lista.remove(3)
# print(lista)
# 6. 리스트명.clear() 리스트 요소 전부 제거
# lista.clear()
# print(lista)

# 7.리스트 정렬  리스트명.sort()
# list_e=[52,34,1,4,6]
# list_e.sort(reverse=True) #내림 정렬
# print(list_e)

# 리스트 내부검사
# in , not in , 값 in 리스트 , 값 not in 리스트
# print(222 in lista)

# 반복문 (문자열,리스트,딕셔너리,range)
"""
for 반복자 in 반복할 수 있는것:
    코드
"""
# for i in range(6):  #0~5까지
#     print("출력",i)

# for i in "HELLO":
#     print(i)

# list_of_list=[[1,2,3],[4,5,6,7],[8,9]]
# for items in list_of_list:
#     for item in items:
#         print(item)
# 전개 연산자 *리스트
# b=[*list_of_list,[5]]
# print(b)
# print(*list_of_list,[5])

# numbers = [273,103,5,32,65,9,72,800,99]
# for number in numbers:
#     print(number,'는',len(str(number)),'자릿수 입니다.')

# numbers = [1,2,3,4,5,6,7,8,9]
# output = [[],[],[]]
#
# for number in numbers:
#     output[(number+2)%3].append(number)
# print(output)

'''
for i in range(0, len(numbers)//2):
    j = (i*2)+1
    print(f"i = {i}, j ={j}")
    numbers[j] = numbers[j]**2
print(numbers)

'''
# ------------------------------------------------------------#
# if number ==1:
#     per={1,0,0,0]
# elif number == 2:
#     per = [0.5, 0.5, 0, 0, 0]
# elif number == 3:
#     per = [0.4, 0.4, 0.2, 0, 0]
# elif number == 4:
#     per = [0.25, 0.25, 0.25, 0.25, 0]
# elif number == 5:
#     per = [0.2, 0.2, 0.2, 0.2, 0.2]

# print(f"총 장학금 {number}명한테 지급 예정")
# for i in range(number):
#     student = students[i]
#     a = int(total_money * per[i])  # 장학금 계산
#     print(f"{student['이름']} 학생이 {a}만 원 받았다.")

