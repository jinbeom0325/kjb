# import time
# number = 0
# x=[[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
# target_tick= time.time() +5
# while time.time() <target_tick:
#     number+=1
#     for i in x:
#         for j in i:
#              i.count(j)
# print("5초 동안 {}번 반복했습니다.".format(number))
import datetime
import time
from os.path import split

# break
# continue
# 위 두가지 키워드는 반복문의 내부에서만 사용 가능
# 반복문의 내부에 들여쓰기로 들어간 자식
# break는 반복문 탈출, continue키워드는 반복문의 처음으로 돌아가서 실행가능

# i=0
# while True:
#     print("{}번째 반복문입니다.".format(i))
#     i+=1
#     input_text=input(">종료하시겠습니까(y/n):")
#     if input_text in ["Y","y"]:
#         print("반복을 종료합니다.")
#         break

# key_list = ["name","hp","mp","level"]
# value_list = ["기사",200,30,5]
# character={}
# for i in range(0,4):
#     character[key_list[i]]=value_list[i]
# print(character)
# for i in range(len(key_list)):
#     character[key_list[i]]=value_list[i]
# print(character)
#
# limit =10000
# i =1
# sum_value=0
# while sum_value<limit:
#     sum_value+=i
#     i+=1
# print("{}를 더할 때 {}을 넘으며 그때의 값은 {}입니다.".format(i-1,limit,sum_value))
# limit =10000
# i =1
# sum_value=0
# while True:
#     sum_value+=i
#     i += 1
#     if sum_value>=10000:
#         break
# print("{}를 더할 때 {}을 넘으며 그때의 값은 {}입니다.".format(i-1,limit,sum_value))
#
# max_value =0
# a=0
# b=0
# for i in range(1,100):
#     j = 100-i
#     if j*i>max_value:
#         max_value=j*i
#         a=j
#         b=i
#         max_value=a*b
# print("최대가 되는 경우: {} * {} = {}".format(a,b,max_value))





# 반복해서 input을 요청함
# utc기반 초 에서 아래 데이터 기준 초3자리 소수점 1자리를 맞춰야함
# 틀린경우 힌트 출력 소수점은 보여주지 않음
# 문제 시도 횟수 20번
# import time
# time2= float(f"{int(time.time())%1000+(time.time()-int(time.time())):4.1f}")
# time3=  (str(time.time())[7:12])
# time4=  (str(time.time())[:10])
# i=1
# max=20
# while i<max:
#     a = float(input("숫자를 입력하세요(xxx.x)"))
#     i += 1
#     if a == time3:
#         print("정답")
#         break
#     elif i>20:
#          print("실패")
#     else:
#          print(f"힌트는 {time4}입니다.")
# print(f"정답은 {time3}였습니다.")

# --------------또다른 방법-----------------------#
# count =0
# while count!=20:
#     count+=1
#     x=str(time.time())
#     x2=x[7:12]
#     print(x)
#     v=input("xxx.x초 입력")
#     if x2==v:
#         print("정답")
#         break
#     else:
#         print("오답",x.split(".")[0])
#     if count==20:
#         print("실패")

# 딕셔너리에 사용 가능한 함수
# keys() : 키 리스트를 얻을 수 있다
# a={"A":100,"B":200,"C":300}
# print(a.keys()) #키 묶음 개체 리턴
# print(list(a.keys()))  #리스트로 형변환
#
# for i in list(a.keys()):
#     print(i)
# for i in a:
#     print(i)
# for i in a.keys():
#     print(i)

# item():딕셔너리 내부 키 : 밸류 들을 얻는 함수
# print(a.items())

# clear():딕셔너리 비우기
# a.clear()
# print(a)

# get()

# 리스트 적용 함수 min() max() sum()
# 최소, 최대, 합 함수
# reversed() 리스트 뒤집기
# enumerate() 열거함수

# temp = reversed([1,2,3,4,5,6])
# for i in temp:
#     print(i,"1111111111")
# for i in temp:
#     print(i,"2222222222")
# 두번째 for문이 출력되지 않는 이유
# reversed()를 통해 만들어진 객체 <list_reverseitorator object>는
# 한번 for문을 통해 내부 순회가 끝나면
# 객체 내부적으로 더 이상 조회가 되지 않는 객체 형태다
# for문을 통해 첫 번째 순회시 내부 데이터가 소모 됨
# for i in reversed([1,2,3,4,5,6]):
#     print(i,"33333333")
# for i in reversed([1,2,3,4,5,6]):
#     print(i,"44444444")

#
# temp = list(reversed([1,2,3,4,5,6]))
# for i in temp:
#     print(i,"55555555")
# for i in temp:
#     print(i,"66666666")

# enumerate() 열거함수 리스트형태
# example_list=["요소a","요소b","요소c"]
# print("#단순 출력")
# print(example_list)
# print()
#
# print("# enumerate() 함수 적용 출력")
# print(enumerate(example_list))
# print()
#
# print("# list() 함수로 강제 변환 출력")
# print(list(enumerate(example_list)))
# print()
#
# print("# 반복문과 조합하기")
# for i, value in enumerate(example_list):
#     print("{}번째 요소는 {}입니다.".format(i,value))


#딕셔너리 items()함수와 반복문
# example_dictionary = {
#     "키A": "값A",
#     "키B": "값B",
#     "키C": "값C",
# }
# print("#딕셔너리의 items() 함수")
# print("item():",example_dictionary.items())
# print()
# print("#딕셔너리의 items() 함수와 반복문 조합하기")
# for key, element in example_dictionary.items():
#     print("dictionary[{}] = {}".format(key,element))
#
# array=[]
# for i in range(0,20,2):
#     array.append(i*i)
# print(array)
# # 리스트변수명=[결과식 for 반복변수 in 반복가능한객체]
# # 리스트변수명=[결과식 for 반복변수 in 반복가능한객체 if 반복문]
# array2=[i*i for i in range(0,20,2)]
# print(array2)

#조건문을 활용한 리스트 내포
# array = ["사과","자두","초콜릿","바나나","체리"]
# output = [fruit for fruit in array if fruit != "초콜릿"]
# print(output)
#
# numbers =[1,2,3,4,5,6]
# r_n=list(reversed(numbers))
# print(r_n)
# for i in range(len(r_n)-1):
#     print(r_n[i])

# print("{:d}".format(10))




# p267
# 1
# output = [j for j in range(1,101)
#          if "{:b}".format(j).count("0")==1]
# for i in output:
#     print("{} : {}".format(i, "{:b}".format(i)))
# print("합계:",sum(output))


# 2
# a=[1,2,3,4,1,2,3,1,4,1,2,3]
# cnt={}
# total=0
# for i in a:
#     if i in cnt:
#         cnt[i]=cnt[i]+1
#     else:
#         cnt[i]=cnt[i]=1
#
# print("{}에서\n사용된 숫자의 종류는 {}개 입니다.\n참고:{}".format(a,(len(cnt)),cnt))




# 3
# a=input("암기 서열을 입력해주세요:")
# dna={
#     "a":0,
#     "t":0,
#     "g":0,
#     "c":0
# }
# for i in a:
#     if i in dna:
#         dna[i]+=1
#     else:
#         dna[i]+=0
#
# for j in dna:
#     print("{}의 개수:{}".format(j,dna[j]))



# 4.
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


# 5
# a=[1,2,[3,4],5,[6,7],[8,9]]
# b=[]
# for i in a:
#     if type(i)==list:
#         for j in i:
#             b.append(j)
#     else:
#         b.append(i)
# print("{}를 평탄화 하면{}입니다.".format(a,b))






#이터레이터&이터러블 둘다 for문 가능
# 이터러블 :반복할 수 있는 것
# 순차적인 값을 반환할 수 있는 구조 (리스트,문자열,딕셔너리)
#
# 이터레이터:반복을 실제 수행하는 객체
# 이터레이터는 이터러블 객체에서 값을 순차적으로 하니씩 꺼내는 역할을 한다
# 사용법:(reversed()의 반환 값,iter() 반환값,리스트반복:enumerate()반환 값) 딕셔너리반복:items()
# 이터레이터는 print()해보면 at 메모리 주소 형태로 출력
# next()함수를 통해 순차적으로 다음 값을 반환
# next()사용시 stopIteration 더 이상 반환 할 값 없다
# 한번 순회를 마치면 다시 조회 불가

# testlist=["500","600","700"] #이터러블 객체
# testiter=iter(testlist) #이터러블 객체에서 이터레이터로 변환 iter()
# print(testiter)
# print(next(testiter))
