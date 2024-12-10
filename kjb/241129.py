# {:b} 2진수 {:o} 8진수 {:x} 16진수
# {:b}.format(22)
# print(int("1010",2))
# print(int("ff",16))
# print("{:x}".format(255))
# print("{:b}".format(0).count("0")==1)


# 1
# output = [j for j in range(1,101)
#          if "{:b}".format(j).count("0")==1]
# for i in output:
#     print("{} : {}".format(i, "{:b}".format(i)))
# print("합계:",sum(output))

# output=[]
# for i in range(1,101):
#     if "{:b}".format(i).count("0")==1:
#         output.append(i)
# for i in output:
#     print("{}: {}".format(i,"{:b}".format(i)))
# print("합계:",sum(output))



# a=[1,2,3,4,1,2,3,1,4,1,2,3]
# counter={}
# for i in a:
#     if i not in counter:
#         counter[i]=0
#     counter[i]+=1
# print(len(list(counter.keys())))


# atgc=input("암기서열입력:")
# l=[]
# counter={}
# # l=[atgc[i:i+3] for i in range(0,len(atgc),3) if len(atgc[i:i+3])==3]
# for i in range(0,len(atgc),3):
#     if len(atgc[i:i+3])==3:
#         l.append(atgc[i:i+3])
# for i in l:
#     if i not in counter:
#         counter[i]=0
#     counter[i]+=1
# print(counter)

# a=[1,2,[3,4],5,[6,7],[8,9]]
# output=[]
# for i in a:
#     if type(i)==list:
#         for j in i:
#             output.append(j)
#     else:
#         output.append(i)
# print(output)


# 튜플
# 튜플은 리스트와 비슷 여러 요소를 담는 데이터 타입
# 리스트는 요소의 삭제 수정 추가가 가능하지만 튜플은 안됨
# 튜플은 보통 생성보다는 함수의 결과로 나오는 경우가 많음

# 생성방법
# tuple1=(1,) #요소가 1개인 튜플은 값 뒤에 쉼표를 작성
# tuple2=1,2,3 #괄호 없이 변수에 여러값을 쉼표로 동시에 주면 튜플로 묶에서 변수에 할당
# tuple3=("a","b",("aaa","bbb"))#중첩
# print(tuple2[0])  인덱스를 통한 조회가능:읽기
# tuple2[0]=100     인덱스를 통한 재할당(쓰기)안됨
# del tuple2[0]     del키워드로 요소 삭제 안됨
# print(tuple3[:])    슬라이싱가능
# print(tuple1+tuple3)  +연산은 리스트와 마찬가지로 연결가능
# print(tuple3*10)      *연산도 리스트와 마찬가지로 반복가능
# print(len(tuple3))      len사용가능

# 내장(빌트인)함수:파이썬에 기본적으로 구현되어 있는 함수들
# 사용자 정의 함수:직접 만드는 함수
# 함수 생성방법
'''
def 함수이름():
    함수내에서 실행하려는 문장
'''
import time

# def print_3_times(asd):
#     print(asd)
#     print("안녕하세요")
#     print("안녕하세요")
# print_3_times("gd")
# 함수의 정의 기준은 반복사용성이 있는지 여부

# 매개변수와 인자개수를 맞춰줌
# def print_n_times(value,n):
#     for i in range(n):
#         print(value)
# print_n_times("안녕하세요",5)

#  매개변수 순서:일반> 가변> 기본

# # 일반,가변 매개변수
# def print_n_times(n,*values):
#     for i in range(n):
#         for value in values:
#             print(value)
#         print()
# print_n_times(3,"안녕하세요","즐거운","파이썬")
#
# # 일반,기본 매개변수
# def print_n_times(value,n=2):
#     for i in range(n):
#             print(value)
# print_n_times("안녕하세요")

# 기본이 가변앞에 올수없음 ,가변이 먼저오는경우 우선으로 실행 같이 쓰려면 n=2처럼 키워드로 써야함

# return이 없는 함수의 반환 결과는 None
# def test(a,b=10,c=100):
#     print(a+b+c)
# print(test(100,200,300))
'''
def 함수(매개변수):
    변수=초깃값
    실행문
    실행문
    return 변수
'''
# x=100   #선언,할당
# x=200   #재할당
# x=200+x #조회 재할당
# print(x)

# def x(ad):
#     print(ad)
# x("1")

# def x(x,y):
#     x=5
#     x=x+100
#     print(x)
# x(100,x)
# print(x)  #x(x,y)
# abc=x
# aaa=[abc,abc,abc]
# for i in aaa:
#     i(1000,2000)   #x함수 호출

#def로 만드는 사용자 정의 함수의 이름도 식별자이다
#def x() 함수를 정의 후 a=x라는 코드를 작성하면 a()형태로 x함수 호출가능


# print("###########")
# a=100
# print(a)
# print(id(a))
# import time
# t=str(time.time()).split(".")[0][-1]
# def func1():
#     print("5보다크다")
# def func2():
#     print("5보다작다")
#
# def xx(l):
#     hello="xx함수 내 지역변수"
#     print(hello)
#     print(id(hello),"hello의 실제 위치")
#     if int(t)>5:
#         return l[0]
#     else:
#         return l[3]
# s=func1
# lists=[s,s,s,func2,s]
# xx(lists)()

# -------------------------------------------------------
# print("###########")
# a=["111","123123",1,2,"400"]
# print(a)
# print(id(a))
# import time
# t=str(time.time()).split(".")[0][-1]
# def func1():
#     print("5보다크다")
# def func2():
#     print("5보다작다")
#
# def xx(l):
#     hello="xx함수 내 지역변수"
#     print(hello)
#     print(id(hello),"hello의 실제 위치")
#     if int(t)>5:
#         return l[0]
#     else:
#         return l[3]
# s=func1
# lists=[]
# for i in range(10):
#     lists.append(s)
# xx(lists)()
# xx(lists)()
# print(id(a))
# for i in range(500):
#     print(id(i),"주소 실제 데이터",i)
# y나 변수들 :스택
# int숫자의 실제데이터11 21:힙

# 파이썬의 메모리 영역은 크게 힙과 스택으로 분류가능
# 그 외에 고정메모리영역 등 존재 각 영역마다 메모리 할당 및 객체 관리 방법이 다르다
# 256까지 정수 형태 데이터가 일정한 주소로 나타난 이유는
# 메모리 효율성을 위해 고정된메모리영역에 256까지 미리 생성해놓기때문
# 따라서 해당 범위 내 숫자는 이미 생성되어 있는 것을 참조하는 것

# 힙영역은 파이썬에서 동적으로 할당되는 객체 저장하는 공간
# 숫자,문자열,리스트,튜플 등 객체들이 이 힙 영역에 실제로 저장됨
# 동적으로 할당된다는 것은 실행 중 할당이 된다/해제가 된다의 의미

# def mul(*values):
#     a=1
#     for i in values:
#         a*=i
#     return a
# print(mul(5,7,9,10))

# # 데이터 타입 집합set
# s1=set([1,2,3])
# print(s1)
# s2=set("hello")
# print(s2)
# # set 데이터타입은 중복이 안되며 순서 상관이 없다. unordered
# # 중복제거 용도로 한번 set변환했다가 다시 다른데이터 타입으로 변환
# # 인덱스 사용x
# # 딕셔너리도 순서x
# # set집합 데이터를 만드는 이유 =교집합,합집합,차집합을 구하기 위해

# s1=set([1,2,3,4,5,6])
# s2=set([1,2,3,4,5,6,7,8,9])
# print(s1&s2)  #교집합
# print(s1.intersection(s2)) #교집합
#
# print(s1|s2)  #합집합
# print(s1.union(s2)) #합집합
#
# print(s2-s1) #차집합
# print(s2.difference(s1))#차집합
#
# s1.add(100) #집합에서 한개의 값 추가
# print(s1)
#
# s1.update([500,700,600]) #여러개의 값 추가
# print(s1)
#
# s1.remove(500)  #값 하나 지우기
# print(s1)
#
# s1.clear()
# print(s1)
# # 숫자 문자 불 리스트 딕트 셋 튜플



# a=int(input("숫자1입력"))
# b=int(input("숫자2입력"))
#
# def add(a,b):
#     c = a + b
#     print("{}+{}는 {}입니다.".format(a,b,c))
#
# def mul(a,b):
#     c=a*b
#     print("{}*{}는 {}입니다.".format(a, b, c))
#
# def sub(a,b):
#     c=a-b
#     print("{}-{}는 {}입니다.".format(a, b, c))
#
# def div(a,b):
#     c=a//b
#     print("{}/{}는 {}입니다.".format(a, b, c))
# add(a,b)
# mul(a,b)
# sub(a,b)
# div(a,b)

# if inp==l[0]
    # while true받아서
    # input

# while True:
#     num1=float(input("숫자1입력:"))
#     a = input("연산기호 입력:")
#     if a not in ['+', '-', '*', '/']:
#         continue
#     num2=float(input("숫자2입력:"))
#     def add(num1,a,num2):
#         if a == '+':
#             result = num1 + num2
#             print("{}+{}={}".format(num1,num2,result))                      #이전계산문
#     def sub(num1,a,num2):
#         if a == '-':
#             result = num1 - num2
#             print("{}-{}={}".format(num1,num2,result))
#     def mul(num1,a,num2):
#         if a == '*':
#             result = num1 * num2
#             print("{}*{}={}".format(num1,num2,result))
#     def div(num1,a,num2):
#         if a == '/':
#             result = num1 / num2
#             print("{}/{}={}".format(num1,num2,result))
# add(num1,a,num2)
# mul(num1,a,num2)
# sub(num1,a,num2)
# div(num1,a,num2)

# atgc=input("암기서열입력:")
# l=[]
# counter={}
# # l=[atgc[i:i+3] for i in range(0,len(atgc),3) if len(atgc[i:i+3])==3]
# for i in range(0,len(atgc),3):
#     if len(atgc[i:i+3])==3:
#         l.append(atgc[i:i+3])
# for i in l:
#     if i not in counter:
#         counter[i]=0
#     counter[i]+=1
# print(counter)
