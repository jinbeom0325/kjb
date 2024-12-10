# while True:
#     # 첫 번째 숫자 입력
#     num1_a = input("첫 번째 숫자를 입력하세요: ")
#     num1 = float(num1_a)
#     while True:
#         # 연산 기호 입력
#         op = input("연산 기호를 입력하세요 (+, -, *, /): ")
#         if op not in ['+', '-', '*', '/']:
#             continue
#         # 두 번째 숫자 입력
#         num2_b = input("다음 숫자를 입력하세요: ")
#         num2 = float(num2_b)
#
#         if op == '/' and num2 == 0:
#             continue  #다시 입력
#         # 계산 수행
#         if op == '+':
#             result = num1 + num2
#         if op == '+':
#             result = num1 - num2
#         elif op == '*':
#             result = num1 * num2
#         elif op == '/':
#             result = num1 / num2
#         # 현재 연산식과 결과 출력
#         print(f"현재 연산: {num1} {op} {num2} = {result}")
#         num1 = result


# def add(a, b):
#     return a + b
# def sub(a, b):
#     return a - b
# def mul(a, b):
#     return a * b
# def div(a, b):
#     return a / b
#
# while True:
#     # 첫 번째 숫자 입력
#     num1_a = input("첫 번째 숫자를 입력하세요: ")
#     num1 = float(num1_a)
#     while True:
#         op = input("연산 기호를 입력하세요 (+, -, *, /): ")
#         if op not in ['+', '-', '*', '/']:
#             continue
#         # 두 번째 숫자 입력
#         num2_b = input("다음 숫자를 입력하세요: ")
#         num2 = float(num2_b)
#         if op == '/' and num2 == 0:
#             continue
#         if op == '+':
#             result = add(num1, num2)
#             print(f"{num1} + {num2} = {result}")
#         elif op == '-':
#             result = sub(num1, num2)
#             print(f"{num1} - {num2} = {result}")
#         elif op == '*':
#             result = mul(num1, num2)
#             print(f"{num1} * {num2} = {result}")
#         elif op == '/':
#             result = div(num1, num2)
#             if result ==0:
#                 continue  # 0으로 나누는 경우 다시 입력
#         print(f"현재 연산: {num1} {op} {num2} = {result}")
#         num1 = result
#-----------------------------------------------------------------------
# 시작하기 1버튼 input
# 1매장 포장
# 2음식의 종류 1런치 2해피스낵
# 3메뉴카테고리에 해당하는 세부메뉴
#   4 메뉴선택 카테고리8 분류5  햄버거선택5
#   5  세트 단품 취소
#     6 옵션 음료 사이즈 이전화면
#     최종 구성 가격 갯수설정 옵션수정버튼 장바구니ㅣ처음화면
# 장바구니에 담겼고 2번 메뉴선택화면
# 결제전 추천메뉴
# 장바구니 리스트와 주문완료,이전버튼
# 결제방법 메뉴
# 주문번호 영수증
# while True:
#     x=input("1.주문하기")
#     if x=="1":
#         x2=input("1.포장 2.매장")
#         if x2=="2":
#             print("모든 카테고리 출력1~8")
#             print("버거의 소분류 모두 출력(기본값 전체)9~14")
#             print("모든 버거의 종류15~22")
#             print("처음으로 23")
#             y=input("1~23번 중 어떤거?")
#             if y=="23":
#                 continue
#
# x=input("버튼 1.버거 2.사이드")
# if x=="2":
#     print("맥런치1,맥런치2")
# menu={"에그맥머핀":[3000,0],"치즈스틱2조각":[2000,0]} #메뉴인덱싱
# key=[0,0,0,0,0]
# while key[0]==0:
#     key[0]=1
#     print("d1")
#     while True:
#         print("d2")
#         while key[2]==0:
#             print("d3")
#             while True:
#                 print("d4")
#--------------------------------------------------------------------
