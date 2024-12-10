import datetime
s1 = {
    "1.버거": {
        "1.전체": {
            "1.더블쿼터파운더치즈": 6000,
            "2.쿼터파운더치즈": 5000,
            "3.불고기": 3000,
            "4.더블불고기": 3500,
            "5.빅맥": 4500,
            "6.치즈": 3000,
            "7.베이컨토마토디럭스": 5000,
            "8.햄버거": 2500,
            "9.맥스파이시상하이": 5500,
            "10.맥치킨": 4500,
            "11.맥크리스피디럭스": 6000},
        "2.비프": {
            "1.더블쿼터파운더치즈": 6000,
            "2.쿼터파운더치즈": 5000,
            "3.불고기": 3000,
            "4.더블불고기": 3500,
            "5.빅맥": 4500,
            "6.치즈": 3000,
            "7.베이컨토마토디럭스": 5000,
            "8.햄버거": 2500},
        "3.치킨": {
            "1.맥스파이시상하이": 5500,
            "2.맥치킨": 4500,
            "3.맥크리스피디럭스": 6000}},
    "2.맥런치": {
        "1.빅맥세트": 5500,
        "2.더블불고기세트": 4500,
        "3.베이컨토마토디럭스세트": 6000},
    "3.맥모닝": {
        "1.에그맥머핀": 2800,
        "2.소시지에그맥머핀": 3000,
        "3.베이컨에그맥머핀": 3300,
        "4.치킨맥머핀": 3000},
    "4.해피스낵": {
        "1.드립커피M": 1000,
        "2.제로콜라M": 1000,
        "3.치즈버거": 2000,
        "4.치즈스틱2조각": 2000,
        "5.후렌치후라이S": 1000},
    "5.사이드": {
        "1.맥윙2조각": 2000,
        "2.맥윙4조각": 3500,
        "3.맥윙8조각": 6000,
        "4.치즈스틱2조각": 2000,
        "5.치즈스틱4조각": 3800,
        "6.후렌치후라이S": 1000,
        "7.후렌치후라이M": 1500,
        "8.후렌치후라이L": 2000,
        "9.맥너겟4조각": 2000,
        "10.맥너겟6조각": 2800},
    "6.디저트": {
        "1.맥플러리": 3000,
        "2.아이스크림콘": 1000},
    "7.맥카페": {
        "1.카페라떼": 2000,
        "2.아이스카페라떼": 2000,
        "3.아이스드립커피": 1000,
        "4.드립커피": 1000},
    "8.음료": {
        "1.콜라M": 1000,
        "2.콜라L": 1500,
        "3.콜라제로M": 1000,
        "4.콜라제로L": 1500,
        "5.사이다M": 1000,
        "6.사이다L": 1500,
        "7.오렌지주스": 1000,
        "8.생수": 1000},
    "9.해피밀": {
        "1.에그맥머핀": 2800,
        "2.소시지에그맥머핀": 3000,
        "3.베이컨에그맥머핀": 3300,
        "4.치즈버거": 2000,
        "5.햄버거": 2500,
        "6.불고기버거": 3000}
}
# 전체 / 비프 / 치킨 3가지로 나뉜다. 세트선택시 위 금액에 +1500원
#맥런치는 단품은 없고 세트만 주문 가능 , *맥런치는 오전10시30분~오후14:00까지 주문 가능
#맥모닝은 단품 or 세트 주문 가능 *오전04:00~오전10:30까지 주문가능 *세트선택시 위 금액에 +1500원
#해피스낵은 사이즈변경이나 조각 수 변경 불가 위 조건으로만 판매
#해피밀은 어린이용 세트로 사이드메뉴는 파인애플만 제공, 음료는 오렌지주스 혹은 생수 중 선택 가능하다
#오전04:00~오전10:30
#오전10:30~오전04:00
now = datetime.datetime.now()
time1 = now.time()
hour = now.hour #시
minute = now.minute #분
cart= [] #장바구니 리스트 전역
number = 1 #주문번호

# 시간별 카테고리 출력 함수
def printcategori():# 미완성
    menu_list = []
    menu_list.append("1.버거")
    if 10 <= hour < (hour == 14 and minute == 0):
        menu_list.append("2.맥런치")
    if 4 <= hour < (hour == 10 and minute == 30):
        menu_list.append("3.맥모닝")
    if 4 <= hour < 10:
        menu_list.append("9.해피밀")
    elif hour == 10 and minute <= 30:
        menu_list.append("9.해피밀")
    menu_list.extend(["4.해피스낵","5.사이드","6.디저트","7.맥카페","8.음료"])
    return menu_list

# 메뉴 출력 함수
def printmenu(menu):
    for j in menu:
        print(f"{j}")

#결제 함수
def printfinish():
    global number
    while True:
        x=input("추가 추천메뉴) 1.해피스낵 2.디저트 3.맥카페 4.뒤로가기")
        if x==("1"or"2"or"3"):
            print("주문페이지로 이동합니다.")
            break
        elif x=="4":
            print("\n주문내역 ")
        total_price = 0
        for item,price in cart: #cart에서 장바구니에 넣어 논거 꺼내옴
            print(f"{item}:{price}원")
            total_price+=price
        print(f"총 합계금액: {total_price}원")
        x2=input("결제 방법 선택 1.카드결제 2.모바일상품권 3.이전단계")
        if x2=="3":
            break
        while x2==("1"):
            x2_2=input("카드결제)숫자1을 입력해주세요(이전단계:0)")
            if x2_2 =="1":
                print("주문이 접수 되었습니다.\n영수증을 받으세요")
                print("----------영수증----------")
                print(f"주문 번호:{number}")
                print(f"{item}{price}원")
                print(f"결제금액{total_price}원")
                print(f"감사합니다.")
                print("-------------------------")
                break
            else:
                break
        while x2==("2"):
            x2_3=input("모바일상품권결제)숫자1을 입력해주세요(뒤로가기:0)")
            if x2_3 == "1":
                print("주문이 접수 되었습니다.\n영수증을 받으세요")
                print("----------영수증----------")
                print(f"주문 번호:{number}")
                print(f"{item}{price}원")
                print(f"결제금액{total_price}원")
                print(f"감사합니다.")
                print("-------------------------")
                break
            else:
                break
        number += 1
        cart.clear()
        break

# 주문 처리 함수1(나머지메뉴 세트x)
def printcart(menu1):
    global cart
    while True:
        print("\n번호를 입력해주세요.(뒤로가기:0)")
        choice = int(input("메뉴 선택: "))
        if choice == 0:
            break
        elif choice > 0 and choice <= len(menu1):  #메뉴 수만큼
            food = list(menu1.keys())[choice - 1]  #-1안하면 메뉴 하나씩 밀림
            price = menu1[food]
            x2=input("(세트주문 불가 상품)장바구니에 1.추가 2.취소")
            if x2=="1":
                print(f"{food} 상품이 주문 목록에 추가되었습니다. 가격:{price}원")
            elif x2=="2":
                break
            cart.append((food, price))  # 상품,가격
            break
        else:
            print("다시 선택해주세요.")
            continue

# 주문 처리 함수2 (버거,해피밀,맥런치 세트메뉴)
def printcart1(menu1):
    global cart
    while True:
        print("\n번호를 입력해주세요.(뒤로가기:0)")
        choice = int(input("메뉴선택: "))
        if choice == 0:
            break
        elif choice > 0 and choice <= len(menu1):
            food = list(menu1.keys())[choice-1]  # -1안하면 메뉴 하나씩 밀려서 나옴 가격도 체크
            price = menu1[food]
            # 세트선택 여부 확인
            x = input("1.단품선택 2.세트선택(+1500원) 3.뒤로가기 4.처음으로")
            if x=="1":
                x2= input("장바구니에 1.추가 2.취소")
                if x2=="1":
                    print(f"{food} 상품이 주문목록에 추가되었습니다. 가격:{price}원")
                elif x2=="2":
                    break
            elif x=="2":
                printmenu(s1["5.사이드"])
                x_1=input("사이드메뉴 선택")
                printmenu(s1["8.음료"])
                x_2=input("음료메뉴 선택")
                # if x_1==type(str) or x_2==type(str):
                x2_1=input("장바구니에 1.추가 2.취소")
                if x2_1=="1":
                    price += 1500
                    print(f"{food} 세트가 주문 목록에 추가되었습니다. 가격:{price}원")
                elif x2_1=="2":
                    break
            cart.append((food, price))  #상품,가격
            break
        else:
            print("다시 선택해주세요.")
            continue

# -메인 키오스크 실행 함수
def kiosk():
    while True:
        x = input("\n1.주문하기(1번입력): ")
        if x == "1":
            x2 = input("1.매장 2.테이크아웃 3.처음으로")
            if x2 == "1" or x2 == "2":
                print("메뉴 카테고리")
                print("1.버거 2.맥런치 3.맥모닝 4.해피스낵 5.사이드 6.디저트 7.맥카페 8.음료 9.해피밀")
                printcategori()
                x3 = input("원하시는 메뉴를 선택해주세요:")
                if x3 == "1":
                    print("--버거 카테고리 선택---")
                    x3_1 = input("1.전체 2.비프 3.치킨")
                    if x3_1 == "1":
                        print("전체 버거 메뉴:")
                        printmenu(s1["1.버거"]["1.전체"])
                        printcart1(s1["1.버거"]["1.전체"])
                    elif x3_1 == "2":
                        print("비프 버거 메뉴:")
                        printmenu(s1["1.버거"]["2.비프"])
                        printcart1(s1["1.버거"]["2.비프"])
                    elif x3_1 == "3":
                        print("치킨 버거 메뉴:")
                        printmenu(s1["1.버거"]["3.치킨"])
                        printcart1(s1["1.버거"]["3.치킨"])
                elif x3 == "2":
                    print("맥런치 메뉴:")
                    printmenu(s1["2.맥런치"])
                    printcart1(s1["2.맥런치"])
                elif x3 == "3":
                    print("맥모닝 메뉴:")
                    printmenu(s1["3.맥모닝"])
                    printcart1(s1["3.맥모닝"])
                elif x3 == "4":
                    print("해피스낵 메뉴:")
                    printmenu(s1["4.해피스낵"])
                    printcart(s1["4.해피스낵"])
                elif x3 == "5":
                    print("사이드 메뉴:")
                    printmenu(s1["5.사이드"])
                    printcart(s1["5.사이드"])
                elif x3 == "6":
                    print("디저트 메뉴:")
                    printmenu(s1["6.디저트"])
                    printcart(s1["6.디저트"])
                elif x3 == "7":
                    print("맥카페 메뉴:")
                    printmenu(s1["7.맥카페"])
                    printcart(s1["7.맥카페"])
                elif x3 == "8":
                    print("음료 메뉴:")
                    printmenu(s1["8.음료"])
                    printcart(s1["8.음료"])
                elif x3 == "9":
                    print("해피밀 메뉴:")
                    printmenu(s1["9.해피밀"])
                    printcart1(s1["9.해피밀"])
                else:
                    print("잘못된 입력하셨습니다.")
                    continue
                x4 = input("1.주문완료 2.주문하기 3.처음으로")
                if x4 == "1":
                    if len(cart)==0:        #상품 리스트가 없으면
                        print("결제하실 상품이 없습니다.")
                        continue    #추후엔 처음말고 카테고리 선택으로
                    else:
                        printfinish()
                elif x4 == "2":
                    continue  #추후엔 처음말고 카테고리 선택으로
            else:
                continue
        else:
            print("다시 선택해주세요")
kiosk()# 메인함수
##개선사항
#맥런치부분
#해피밀부분
#시간별 메뉴카테고리출력