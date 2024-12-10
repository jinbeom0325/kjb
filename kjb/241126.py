# numbers = [273,103,5,32,65,9,72,800,99]
# for number in numbers:
#     if number%2==1:
#         print("{}는 홀수입니다.".format(numbers))
#     elif number%2==0:
#         print("짝수")
#     else:
#         print(" ")
# for number in numbers:
#     print(f"{number} 는 {len(str(number))} 자릿수입니다.")
#     print("{} 는 {} 자릿수 입니다.".format(number,len(str(number))))
#
#
# numbers = [1,2,3,4,5,6,7,8,9,10,11,12]
# output = [[],[],[],[]]
#
# for number in numbers:
#     print((number-1)%3)
#     output[(number-1)%3].append(number)
# print(output)
from itertools import count
from os.path import split

# 함수
# def hello(fff):
#     print("hello",fff)
# hello(str(234234))

# 8진수 표현법  0o+8진숫자
# a=0o100
# print(a) 64
# 16진수 표현법 0x+16진수숫자
# a=0xFF
# print(a) 255

# 문자열 자료형 함수
# 1.count 문자열에 찾는 문자갯수
# a="hello"
# print(a.count('l'))

# 2.find rfind 문자를 찾고 인덱스 번호를 리턴

# 3.index 문자를 찾고 인덱스 번호 리턴

# print(a.find("f"))  find는 찾는 문자가 없으면 -1을 리턴
# print(a.index("f")) index는 찾는 문자가 없으면 valueError에러발생

# 4.join()함수 문자열 중간 삽입 함수
# print("_".join("abcd")) 문자열데이터.join
# print(a.join("1234"))   문자열 담긴변수.join
# print(a)

# 문자열&리스트
# 같은함수들: len(),슬라이싱,인덱스,+,*,for문 대상
# 문자열은 문자로만 구성되며 리스트는 어떤 데이터 타입도 담을 수 있다.
# 리스트는 특정 인덱스 위치의 값을 바꿀 수 있고 문자열은 못바꿈(읽기전용)
# 문자열의 일부 문자를 수정하는 방법은 인덱스가 아닌 replace()로 가능
# a="hello"
# print(a.replace("h","f"))
# print(a)

# split() 분리
# aaa="aaa bbb ccc"
# print(aaa.split(" "))   #split()함수는 공백을 기준으로 문자열을 분리,리스트로 반환
# print(aaa)

# 리스트:인덱스 번호 기반 자료 정리,저장    순서에 의존
# 딕셔너리:키를 기반으로 값을 저장
# dict_a = {
#     'name':"어벤저스 엔드게임",
#     "type":123,
#     1:[3,4,5],
#     False:50
# }
# print(dict_a[1]) #리스트에서 인덱싱과 같은 방법으로, 인덱스 번호가 아닌 key이름을 입력

'''
dictionary = {
    "name": "7D 건조 망고",
    "type": "당절임",
    "ingredient": ["망고","설탕","메타중아황산나트륨","치자황색소"],
    "origin":"필리핀"
}
print("name",dictionary["name"])
print("type",dictionary["type"])
print("ingredient",dictionary["ingredient"])
print("origin",dictionary["origin"])

dictionary["name"]="8D 건조 망고" #수정
print("name:",dictionary["name"]) #출력
print(dictionary["name"][1]) #인덱스로 특정 값만 출력
'''

#추가 제거
# dictionary={}
# print("요소 추가 이전:",dictionary)
# dictionary["name"]="새로운 이름"
# dictionary["head"]="새로운 정신"
# dictionary["body"]="새로운 몸"
# print("요소 추가 이후:",dictionary)
# dictionary["name"]="새로운"
# print(dictionary)
# del dictionary["name"]
# print(dictionary)

# 딕셔너리 in키워드
# if "head" in dictionary:
#     print("존재한다")

# 딕셔너리의 키 검색 방법 : get()함수
# get(키)에서 키가 존재 하지 않으면 None이 리턴되고 정상 종료 (에러x)
# value=dictionary.get("존재하지 않는 키")
# print("값:",value)

# for i in dictionary:
#     print(i,dictionary[i]) #키 값불러옴

'''
# 4번문제
# character ={
#     "name": "기사",
#     "level": 12,
#     "items": {
#         "sword": "불꽃의 검",
#         "armor": "풀플레이트"
#     },
#     "skill":["베기","세게 베기","아주 세게 베기"]
# }

# for key in character:
#     if (type(character[key]) is list):   #키값이 리스트 인가
#         for list_1 in character[key]:    #값을 list_1에
#             print(key,":",list_1)        #키와 키값
##        
    #
    # elif type(character[key]) is dict:      #딕트인경우
    #     for dict_1 in character[key]:       #키값을 dict_1에 sword,armor
    #         print(dict_1,":",character[key][dict_1])  #키값과, 키값sword,armor의 값
    #
    # else:
    #     print(key,":",character[key])  #그외
'''

'''
# 3번문제 p227
# numbers = [1,2,3,6,2,7,8,2,8,3,1,2,4]
# counter = {}
# for number in numbers:
#     if number in counter:
#         counter[number]= counter[number]+1
#     else:
#         counter[number]=1
# print(counter)
'''

'''
# 2번문제
pets=[
    {"name": "구름","age":5},
    {"name": "구름","age":5},
    {"name": "구름","age":5},
    {"name": "구름","age":5},
]
for pet in pets:
    print(pet["name"],str(pet["age"])+"살")
'''


# numbers = [1,2,3,6,2,7,8,2,8,3,1,2,4]
# counter = {}
# for number in numbers:
#
#     if counter.get(number)==None:
#         counter[number]=1
#     else:
#         counter[number]+=1
# counter[9]=1
# counter[9]=counter[9]+1
# print(counter[9])

# character ={
#     "name": "기사",
#     "level": 12,
#     "items": {
#         "sword": "불꽃의 검",
#         "armor": "풀플레이트"
#     },
#     "skill":["베기","세게 베기","아주 세게 베기"]
# }
# for key in character:
#     if (type(character[key]) is list):
#         for i in character[key]:
#             print("{} : {}".format(key,i))
#     elif type(character[key]) is dict:
#         for i in character[key]:
#             print("{} : {}".format(i,character[key][i]  ))
#     else:
#         print(key,character[key])
# for key in character:
#     print(key)



'''
# 딕셔너리 학생에는 5명의 학생 정보
# 정보종류로는 1이름,2학년,3전공(국어,영어,수학,컴공),4성적은 학생 각각 (국어,영어,수학,컴공)(성적범위 1~100점)
# 사용자 입력a을 통해 장학금 액수 입력
# 사용자 입력b을 통해 장학금 지급 인원 설정
#   case1 1명으로 설정하는 경우 장학금 100%지원
#   2명일 경우 50:50
#   3명일 경우 40:40:20
#   4명일 경우 25:25:25:25
#   5명일 경우 20:20:20:20:20
# 비전공자는 과목에+10%가산, 최대점수는 100점
# 장학금은 성적의 평균으로 지급
# 출력: 총 장학금 ~ x명한테 지급 x학생이 x를 받았다.

students = [
    {"이름": "학생1", "학년": 1, "전공": "국어", "성적": {"국어": 80, "영어": 70, "수학": 80, "컴공": 70}},
    {"이름": "학생2", "학년": 2, "전공": "영어", "성적": {"국어": 70, "영어": 30, "수학": 90, "컴공": 50}},
    {"이름": "학생3", "학년": 3, "전공": "수학", "성적": {"국어": 60, "영어": 60, "수학": 20, "컴공": 30}},
    {"이름": "학생4", "학년": 4, "전공": "컴공", "성적": {"국어": 20, "영어": 60, "수학": 30, "컴공": 50}},
    {"이름": "학생5", "학년": 1, "전공": "국어", "성적": {"국어": 90, "영어": 30, "수학": 70, "컴공": 80}},
]
# 평균 성적 계산
total = 0
count = 4
for student in students:

    for subject in ["국어", "영어", "수학", "컴공"]:
        score = student["성적"][subject]  # 점수
        if subject == student["전공"]:  # 전공 과목은 그대로
            total = total + score
        else:  # 다른 과목은 10%
            score1 = score * 1.1
            if score1 > 100:  # 100점 안넘게
                score1 = 100
                total = total + score1
            student["평균"] = total / count  # 평균저장
# print(student["성적"]["국어"])        정상출력
total_money= int(input("장학금 총액을 입력하세요: "))
number = int(input("장학금 지급 인원 수를 입력하세요:(1~5입력)"))

# 1명으로 입력하는 경우 장학금 100%지원,2명은 각각50%씩 3명은 40%,40%,20%, 4명은 각각 25%씩, 5명은 각각20%씩
p = 0
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
'''












