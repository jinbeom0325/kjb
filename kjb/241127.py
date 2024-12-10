'''
# 장학금은 성적의 평균으로 지급
s1={"이름": "학생1", "학년": 1, "전공": "국어", "성적": {"국어": 80, "영어": 70, "수학": 80, "컴공": 70}}
s2={"이름": "학생2", "학년": 2, "전공": "영어", "성적": {"국어": 70, "영어": 30, "수학": 90, "컴공": 50}}
s3={"이름": "학생3", "학년": 3, "전공": "수학", "성적": {"국어": 60, "영어": 60, "수학": 20, "컴공": 30}}
s4={"이름": "학생4", "학년": 4, "전공": "컴공", "성적": {"국어": 20, "영어": 60, "수학": 30, "컴공": 50}}
s5={"이름": "학생5", "학년": 1, "전공": "국어", "성적": {"국어": 90, "영어": 30, "수학": 70, "컴공": 80}}
stu_list=[s1,s2,s3,s4,s5]
ratio=[[100],[50,50],[40,40,20],[25,25,25,25],[20,20,20,20,20]] #비율
sum = 0  # 학생의 과목 점수를 누적 합산 임시 변수
score=0 #최대 점수를 기억하기 위한 임시 변수
who=0 #최대 점수의 주인 변수
rank_list=[] #점수가 높은 순 나열하기 위한 리스트



# 비전공자는 과목에+10%가산, 최대점수는 100점
listx=[]
for i in stu_list:  #i=s1,s2,s3,s4
    for j in i["성적"]: #j=국영수컴
        if i["전공"]!=j: # j는 i학생딕트의 과목명
            if i["성적"][j]*1.1>100: #i학새의 j과목 성적에 10%가산 결과가 100점초과면
                sum+=100            #100으로 처리해서 더해줌
            else:       #비전공 우대로 가산을 해도 100보다 작을경우
                sum+=i["성적"][j]*1.1 #가산 1.1곱한 결과를 누적 합산
        else: #전공 과목
            sum+= i["성적"][j] #전공과목 경우 가산없이 누적
    i["총점"]=int(sum)  # i학생의 모든 과목 가산 적용 완료 후 총점을 i학생의 "총점" key값의 value로 할당
    sum=0 # i를 통해 지목된 학생 한명에 대한 성적 합산이 끝나고 변수를 초기화(ex계산기)

# 사용자 입력a을 통해 장학금 액수 입력
# 사용자 입력b을 통해 장학금 지급 인원 설정
A=int(input("장학금 얼마"))
B=int(input("몇명"))

for j in range(B):
    for i in stu_list:
        if i["총점"]>score: #처음 0과비교
            score=i["총점"]
            who=stu_list.index(i) #최고점수 인덱스번호
    rank_list.append(stu_list.pop(who))
    score=0
    who=0

for i in range(len(ratio[B-1])):
    print("{}등 이름{},총점{}으로 장학금{}%지급 =>{}원"
          .format(i+1,rank_list[i]["이름"],rank_list[i]["총점"],ratio[B-1],int(ratio[B-1][i]*A)/100))
                                                                                #퍼센트*장학액수/100
'''

# 범위
# while반복문:특정 횟수/특정시간/특정 조건 도달시 등등 ,#for는 보통 꺼내쓸때
# break키워드
# continue키워드

# range(시작,종료,스텝),  list로 형변환 가능
# print(type(range(0,100)))
# print(list(range(100)))
# print(list(range(10,20+1,2)))

# for i in range(4,0-1,-1):
#     print("현재 반복 변수: {}".format(i))
# for i in reversed(range(5)):  #4,-1,-1
#     print(i)

# output=""
# for i in range(1,10):
#     for j in range(0,i):
#         output+= "*"
#     output +="\n"
# print(output)


# output=""
# for i in range(1,15):
#      for j in range(14,i,-1):       #공백13번
#         output +=" "
#      for k in range(0,2*i-1):
#         output +="*"
#      output += "\n"
# print(output)

# 역피라미드
# output=""
# r=int(input("몇행"))
# for i in range(1,r+1):
#      for j in range(0,i-1):
#         output +=" "
#      for k in range(2*(r-i),-1,-1):
#         if k==0 or k==2*(r-i):
#             output +="*"
#         else:
#             output +="#"
#      output += "\n"
# print(output)

# while 반복문
# for 반복문은 반복가능한객체 대상 ,,,,반복가능한객체 내부 요소를 하나씩 활용
# 특정 횟수 반복 or 범용적 사용=> while반복

# import datetime
# now=datetime.datetime.now()
# x=0
# while x<10:

#     정지방법1
    # print("{}번째 while반복".format(x))
    # now=datetime.datetime.now()
    # if now.second==30: #특정 시간 값에 정지시키기
    #     x=20

# list_test = [1,2,1,2]
# value = 2
# while value in list_test:
#     list_test.remove(value)
# print(list_test)

