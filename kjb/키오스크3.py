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
        "1.해피밀(맥머핀 종류)": {
            "1.에그맥머핀": 2800,
            "2.소시지에그맥머핀": 3000,
            "3.베이컨에그맥머핀": 3300,
        },
        "2.해피밀(버거 종류)": {
            "1.에그맥머핀": 2800,
            "2.소시지에그맥머핀": 3000,
            "3.베이컨에그맥머핀": 3300,
            "4.치즈버거": 2000,
            "5.햄버거": 2500,
            "6.불고기버거": 3000
        }
    }
}
cart = []  # 장바구니 리스트 전역
number = 1  # 주문번호
# 시간
import datetime
now = datetime.datetime.now()
start_morning = datetime.datetime(now.year, now.month, now.day + 0, 4, 0)
end_morning = datetime.datetime(now.year, now.month, now.day + 0, 10, 30)
start_lunch = datetime.datetime(now.year, now.month, now.day + 0, 10, 30)
end_lunch = datetime.datetime(now.year, now.month, now.day + 0, 14, 0)
next_morning1 = datetime.datetime(now.year, now.month, now.day + 0, 10, 30)
next_morning = datetime.datetime(now.year, now.month, now.day + 1, 4, 0)
#메뉴 리스트 업데이트
def printcategori():
    menu_list = []
    if next_morning1<= now<=next_morning:
        menu_list.append("1.버거")
        menu_list.append("9.해피밀")
    elif start_lunch <= now <= end_lunch:
        menu_list.append("2.맥런치")
    elif start_morning <= now<= end_morning:
        menu_list.append("3.맥모닝")
        menu_list.append("9.해피밀")
    # 공통 메뉴 추가
    menu_list.extend(["4.해피스낵", "5.사이드", "6.디저트", "7.맥카페", "8.음료"])
    # 메뉴 목록 정렬
    menu_list.sort()
    return menu_list
#시간대 메뉴출력 함수
def printmenu_time():
    available_menues = printcategori()
    print("현재 가능한 메뉴 카테고리:")
    for menu in available_menues:
        print(menu, end=" ' ")
# 메뉴 추출 함수
def printmenu(menu):
    for j in menu:
        print(f"{j}")
# 결제 함수
def printfinish():
    global number
    while True:
        x = input("추가 추천메뉴: 1.해피스낵 2.디저트 3.맥카페 등 주문하기로 이동 (4.선택안함) ")
        if x == "1" or x == "2" or x == "3":
            print("주문페이지로 이동합니다.")
            break
        elif x == "4":
            print("\n주문내역")
        total_price = 0
        for item, price in cart:  # cart에서 장바구니에 넣어 놓은 거 꺼냄
            print(f"{item}: {price}원")
            total_price += price
        print(f"총 합계금액: {total_price}원")
        x2 = input("결제 방법 선택 1.카드결제 2.모바일상품권 3.뒤로가기: ")
        if x2 == "3":
            continue
        while x2 == "1":
            x2_2 = input("카드결제) 숫자1을 입력해주세요(뒤로가기:0): ")
            if x2_2 == "1":
                print("주문이 접수 되었습니다.\n영수증을 받으세요")
                print("----------영수증----------")
                print(f"주문 번호:{number}")
                for item, price in cart:
                    print(f"{item}: {price}원")
                print(f"결제금액 {total_price}원")
                print(f"감사합니다.")
                print("-------------------------")
                return 0 #종료
            else:
                break
        while x2 == "2":
            x2_3 = input("모바일상품권결제) 숫자1을 입력해주세요(뒤로가기:0): ")
            if x2_3 == "1":
                print("주문이 접수 되었습니다.\n영수증을 받으세요")
                print("----------영수증----------")
                print(f"주문 번호:{number}")
                for item, price in cart:
                    print(f"{item}: {price}원")
                print(f"결제금액 {total_price}원")
                print(f"감사합니다.")
                print("-------------------------")
                return 0
            else:
                break
# 주문 처리 함수1(단품메뉴)
def printcart(menu1):
    global cart
    while True:
        print("\n상품번호를 입력해주세요.(돌아가기:0)")
        choice = int(input("메뉴 선택: "))
        if choice == 0:
            break
        # elif choice > 0 and choice <= len(menu1):  #메뉴 수만큼
        elif 0 < choice <= len(menu1):  #메뉴 수만큼
            food = list(menu1.keys())[choice - 1]  #-1안하면 메뉴 하나씩 밀림
            price = menu1[food]
            x2=input("장바구니에 1.추가 2.취소")
            if x2=="1":
                print(f"{food} 상품이 주문 목록에 추가되었습니다. 가격:{price}원")
            elif x2=="2":
                continue
            cart.append((food, price))
            break
# 주문 처리 함수2 (버거,맥런치 세트선택메뉴)
def printcart1(menu1):
    global cart
    while True:
        print("\n상품번호를 입력해주세요.(돌아가기:0)")
        choice = int(input("메뉴 선택:"))
        if choice == 0:
            break
        elif 0 < choice <= len(menu1):
            food = list(menu1.keys())[choice - 1]
            price = menu1[food]
            # 세트선택 여부 확인
            x = input("1.단품선택 2.세트선택(+1500원) 3.뒤로가기 4.처음으로: ")
            if x == "1":
                x2 = input("장바구니에 1.추가 2.취소: ")
                if x2 == "1":
                    print(f"{food} 상품이 주문목록에 추가되었습니다. 가격: {price}원")
                elif x2 == "2":
                    continue
            elif x == "2":
                printmenu(s1["5.사이드"])
                x_1 = input("사이드메뉴 선택: ")
                printmenu(s1["8.음료"])
                x_2 = input("음료메뉴 선택: ")
                x2_1 = input("장바구니에 1.추가 2.취소: ")
                if x2_1 == "1":
                    price += 1500
                    print(f"{food} 세트가 주문 목록에 추가되었습니다. 가격: {price}원")
                elif x2_1 == "2":
                    continue
            elif x == "3":
                continue
            elif x == "4":
                break
            cart.append((food, price))
            break
        else:
            print("다시 입력해주세요.")
#주문처리함수3(해피밀)
def printcart2(menu1):
    global cart
    while True:
        print("\n상품번호를 입력해주세요.(돌아가기:0)")
        choice = int(input("메뉴 선택: "))
        if choice == 0:
            break
        elif 0 < choice <= len(menu1):
            food = list(menu1.keys())[choice - 1]
            price = menu1[food]
            # 세트선택 여부 확인
            x = input("1.해피밀은 어린이용 세트메뉴로 사이드는 파인애플만 제공됩니다.\n"
                      "음료를 선택해주세요 1.오렌지주스 2.생수 3.뒤로가기 4.처음으로")
            if x=="1"or x=="2":
                x2=input(("장바구니에 1.추가 2.취소"))
                if x2 == "1":
                    print(f"{food} 상품이 주문 목록에 추가되었습니다. 가격:{price}원")
                    break
                elif x2=="2":
                    continue
            elif x=="3":
                continue
            elif x=="4":
                break
            cart.append((food, price))  # 상품,가격
            break

# 메인
def kiosk():
    while True:
        x = input("\n1.주문하기(1번입력): ")
        if x == "1":
            while x == "1":
                x2 = input("1.매장 2.테이크아웃 3.처음으로")
                if x2 == "1" or x2 == "2":
                    available_menues = printcategori()
                    printmenu_time()
                    print("\n---------------------------------")
                    x3 = input("원하시는 메뉴를 선택해주세요:")
                    if x3 == "1" and "1.버거" in available_menues:
                        print("--버거 카테고리 선택---")
                        x3_1 = input("1.전체 2.비프 3.치킨")
                        if x3_1 == "1":
                            print("전체 버거 메뉴:")
                            printmenu(s1["1.버거"]["1.전체"])
                            printcart1(s1["1.버거"]["1.전체"])
                            break
                        elif x3_1 == "2":
                            print("비프 버거 메뉴:")
                            printmenu(s1["1.버거"]["2.비프"])
                            printcart1(s1["1.버거"]["2.비프"])
                            break
                        elif x3_1 == "3":
                            print("치킨 버거 메뉴:")
                            printmenu(s1["1.버거"]["3.치킨"])
                            printcart1(s1["1.버거"]["3.치킨"])
                            break
                    elif x3 == "2" and "2.맥런치" in available_menues:
                        print("맥런치 메뉴:")
                        printmenu(s1["2.맥런치"])
                        printcart(s1["2.맥런치"])
                        break
                    elif x3 == "3" and "3.맥모닝" in available_menues:
                        print("맥모닝 메뉴:")
                        printmenu(s1["3.맥모닝"])
                        printcart1(s1["3.맥모닝"])
                        break
                    elif x3 == "3" and "3.맥모닝" in available_menues:
                        print("해피스낵 메뉴:")
                        printmenu(s1["4.해피스낵"])
                        printcart(s1["4.해피스낵"])
                        break
                    elif x3 == "3" and "3.맥모닝" in available_menues:
                        print("사이드 메뉴:")
                        printmenu(s1["5.사이드"])
                        printcart(s1["5.사이드"])
                        break
                    elif x3 == "3" and "3.맥모닝" in available_menues:
                        print("디저트 메뉴:")
                        printmenu(s1["6.디저트"])
                        printcart(s1["6.디저트"])
                        break
                    elif x3 == "3" and "3.맥모닝" in available_menues:
                        print("맥카페 메뉴:")
                        printmenu(s1["7.맥카페"])
                        printcart(s1["7.맥카페"])
                        break
                    elif x3 == "3" and "3.맥모닝" in available_menues:
                        print("음료 메뉴:")
                        printmenu(s1["8.음료"])
                        printcart(s1["8.음료"])
                        break
                    elif x3 == "9" and "9.해피밀" in available_menues:
                        print("해피밀 메뉴:")

                        if start_morning <= now<= end_morning:
                            printmenu(s1["9.해피밀"]["1.해피밀(맥머핀 종류)"])
                            printcart2(s1["9.해피밀"]["1.해피밀(맥머핀 종류)"])
                            break
                        elif next_morning1<= now<=next_morning:
                            printmenu(s1["9.해피밀"]["2.해피밀(버거 종류)"])
                            printcart2(s1["9.해피밀"]["2.해피밀(버거 종류)"])
                            break
                    else:
                        print("현재 시간에는 선택할 수 없는 메뉴입니다.")
                        kiosk()
                elif x2=="3":
                    kiosk()
            if len(cart) ==0:
                kiosk()
            else:
                while len(cart) != 0:
                    x4 = input("1.주문완료 2.추가주문 3.장바구니비우기")
                    if x4 == "1":
                        printfinish()
                        break
                    elif x4 == "2":
                        kiosk()  #
                    elif x4 == "3":
                        cart.clear()  # 초기화하고 재실행 return 0 해도
                        kiosk()
        else:
            print("다시 입력해주세요.")
#kiosk()
#해피밀 메뉴업데이트 개선필요
#뒤로가기 처음으로 버튼 정확도