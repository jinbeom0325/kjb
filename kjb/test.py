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
    "2.해피스낵": {
        "1.드립커피M": 1000,
        "2.제로콜라M": 1000,
        "3.치즈버거": 2000,
        "4.치즈스틱2조각": 2000,
        "5.후렌치후라이S": 1000},
    "3.사이드": {
        "1.후렌치후라이S": 1000,
        "2.맥윙2조각": 2000,
        "3.후렌치후라이M": 1500,
        "4.치즈스틱2조각": 2000,
        "5.맥윙4조각": 3500,
        "6.맥너겟4조각": 2000,
        "7.치즈스틱4조각": 3800,
        "8.맥너겟6조각": 2800,
        "9.맥윙8조각": 6000,
        "10.후렌치후라이L": 2000},
    "4.디저트": {
        "1.맥플러리": 3000,
        "2.아이스크림콘": 1000},
    "5.맥카페": {
        "1.카페라떼": 2000,
        "2.아이스카페라떼": 2000,
        "3.아이스드립커피": 1000,
        "4.드립커피": 1000},
    "6.음료": {
        "1.콜라M": 1000,
        "2.콜라제로M": 1000,
        "3.사이다M": 1000,
        "4.생수": 1000,
        "5.오렌지주스": 1000,
        "6.콜라L": 1500,
        "7.콜라제로L": 1500,
        "8.사이다L": 1500},
    "7.해피밀": {
        "1.해피밀(맥머핀 종류)": {
            "1.에그맥머핀": 2800,
            "2.소시지에그맥머핀": 3000,
            "3.베이컨에그맥머핀": 3300},
        "2.해피밀(버거 종류)": {
            "1.치즈버거": 2000,
            "2.햄버거": 2500,
            "3.불고기버거": 3000}},
    "8.맥런치": {
        "1.빅맥세트": 5500,
        "2.더블불고기세트": 4500,
        "3.베이컨토마토디럭스세트": 6000},
    "9.맥모닝": {
        "1.에그맥머핀": 2800,
        "2.소시지에그맥머핀": 3000,
        "3.베이컨에그맥머핀": 3300,
        "4.치킨맥머핀": 3000}}
cart = []  # 장바구니 리스트 전역
number = 1  # 주문번호

import datetime
now = datetime.datetime.now() #시간
start_morning = datetime.datetime(now.year, now.month, now.day + 0, 4, 0)
end_morning = datetime.datetime(now.year, now.month, now.day + 0, 10, 30)
start_lunch = datetime.datetime(now.year, now.month, now.day + 0, 10, 30)
end_lunch = datetime.datetime(now.year, now.month, now.day + 0, 14, 0)
next_morning1 = datetime.datetime(now.year, now.month, now.day + 0, 10, 30)
next_morning = datetime.datetime(now.year, now.month, now.day +1,4,0)
print("현재시간", now.strftime("%H:%M:%S"))

#메뉴 리스트 업데이트
def printcategori():
    menu_list = []
    if next_morning1<= now<=next_morning:  # 10:30 ~ 다음날04:00
        menu_list.append("1.버거")
        menu_list.append("7.해피밀")
    elif start_lunch <= now <= end_lunch:  #10:30 ~ 14:00
        menu_list.append("8.맥런치")
    elif start_morning <= now<= end_morning:  #04:00~10:30
        menu_list.append("9.맥모닝")
        menu_list.append("7.해피밀")
    menu_list.extend(["2.해피스낵", "3.사이드", "4.디저트", "5.맥카페", "6.음료"]) # 항시추가
    menu_list.sort() # 메뉴 목록 정렬
    return menu_list
#시간대 카테고리 출력
def printmenu_time():
    available_menue = printcategori()      #사용메뉴=카테고리에서
    print("현재 가능한 메뉴 카테고리")
    for menu in available_menue:
        print(menu, end=" ' ")
# 메뉴 추출 함수
def printmenu(menu):
    for j in menu:
        print(f"{j}")
# 결제 함수
def printfinish():
    global number
    while True:
        x = input("(추천메뉴- 1.해피스낵 2.사이드 3.디저트 4.맥카페 주문하기로 이동 (5.선택안함)")
        if x == "1":
            print("해피스낵 주문페이지로 이동합니다.")
            printmenu(s1["2.해피스낵"])
            printcart(s1["2.해피스낵"])
        elif x=="2":
            print("사이드 주문페이지로 이동합니다.")
            printmenu(s1["3.사이드"])
            printcart(s1["3.사이드"])
        elif x == "3":
            print("디저트 주문페이지로 이동합니다.")
            printmenu(s1["4.디저트"])
            printcart(s1["4.디저트"])
        elif x == "4":
            print("맥카페 주문페이지로 이동합니다.")
            printmenu(s1["5.맥카페"])
            printcart(s1["5.맥카페"])
        elif x == "5":
            print("\n---주문내역---")
        total_price = 0
        for item, price in cart:  # cart에서 장바구니에 넣어 놓은 거 꺼냄
            print(f"{item[2:]}: {price}원")
            total_price += price
        print(f"총 합계금액: {total_price}원")
        x2 = input("결제방법 선택- 1.카드결제 2.모바일상품권 3.간편결제 0.처음으로(초기화)")
        if x2 == "0":
            print("취소되었습니다.")
            cart.clear()
            break
        while x2 == "1":
            x2_2 = input("카드결제 숫자1을 입력해주세요. 0.처음으로(초기화) ")
            if x2_2 == "1":
                print("주문이 접수 되었습니다.\n영수증을 받으세요.")
                print("----------영수증----------")
                print(f"주문 번호:{number}")
                for item, price in cart:
                    print(f"{item[2:]}: {price}원")
                print(f"결제금액 {total_price}원")
                print(f"감사합니다.")
                print("-------------------------")
                cart.clear()
                print("처음 화면으로 돌아갑니다.")
                kiosk()
            elif x2_2=="0":
                print("결제가 취소되었습니다.")
                cart.clear()
                kiosk()
            else:
                print("잘못입력되었습니다. 다시 입력해주세요.")
                continue
        while x2 == "2":
            x2_3 = input("모바일상품권결제 숫자1을 입력해주세요. 0.처음으로(초기화) ")
            if x2_3 == "1":
                print("주문이 접수 되었습니다.\n영수증을 받으세요.")
                print("----------영수증----------")
                print(f"주문 번호:{number}")
                for item, price in cart:
                    print(f"{item}: {price}원")
                print(f"결제금액 {total_price}원")
                print(f"감사합니다.")
                print("-------------------------")
                cart.clear()
                print("처음 화면으로 돌아갑니다.")
                kiosk()
            elif x2_3=="0":
                print("결제가 취소되었습니다.")
                cart.clear()
                kiosk()
            else:
                print("잘못입력되었습니다. 다시 입력해주세요.")
                continue
        while x2 == "3":
            x2_3 = input("간편결제 숫자1을 입력해주세요. 0.처음으로(초기화) ")
            if x2_3 == "1":
                print("주문이 접수 되었습니다.\n영수증을 받으세요.")
                print("----------영수증----------")
                print(f"주문 번호:{number}")
                for item, price in cart:
                    print(f"{item}: {price}원")
                print(f"결제금액 {total_price}원")
                print(f"감사합니다.")
                print("-------------------------")
                cart.clear()
                print("처음 화면으로 돌아갑니다.")
                kiosk()
            elif x2_3=="0":
                print("결제가 취소되었습니다.")
                cart.clear()
                kiosk()
            else:
                print("잘못입력되었습니다. 다시 입력해주세요.")
                continue

# 주문 처리 함수1(사이드 및 단품메뉴)
def printcart(menu1):
    global cart
    while True:
        print("\n상품번호를 입력해주세요. 0.처음으로(초기화)")
        choice = int(input("메뉴 선택: "))
        if choice == 0:
            cart.clear()
            break
        # elif choice > 0 and choice <= len(menu1):  #메뉴 수만큼
        elif 0 < choice <= len(menu1):  #메뉴 수만큼
            food = list(menu1.keys())[choice - 1]  #-1안하면 메뉴 하나씩 밀림
            price = menu1[food]
            x2=input("장바구니에 1.추가 2.취소")
            if x2=="1":
                print(f"{food[2:]} 상품이 주문목록에 추가되었습니다. 가격:{price}원\n")
            elif x2=="2":
                print("취소되었습니다. 다시입력해주세요.\n")
                printmenu(menu1)
                continue
            else:
                print("잘못입력되었습니다.다시입력해주세요.\n")
                printmenu(menu1)
                continue
            cart.append((food, price))
            break
# 주문 처리 함수2 (맥런치,맥모닝,버거)
def printcart1(menu1):
    global cart
    while menu1 == s1["8.맥런치"]:
        print("\n상품번호를 입력해주세요. 0.처음으로(초기화)")
        choice = int(input("메뉴 선택:"))
        if choice == 0:
            cart.clear()
            break
        elif 0 < choice <= len(menu1):
            food = list(menu1.keys())[choice - 1]
            price = menu1[food]
        x3 = input("1.라지세트로 변경(+800원) 2.변경안함 (뒤로가기:0)")
        if x3 =="1":
            print(list(s1["3.사이드"].keys())[6:])
            x_3 = int(input("사이드메뉴 선택: "))
            side_selected = list(s1["3.사이드"].keys())[x_3 - 1]
            print(list(s1["6.음료"].keys())[3:])
            x_4 = int(input("음료메뉴 선택: "))
            drink_selected = list(s1["6.음료"].keys())[x_4 - 1]
            print("----고르신 메뉴----")
            print(f"메뉴: {food[2:]}")
            print(f"사이드:{side_selected[2:]}")
            print(f"음료: {drink_selected[2:]}")
            x3_1 = input("장바구니에 1.추가 2.취소")
            if x3_1 =="1":
                price += 800
                print(f"{food[2:]}라지 세트가 주문목록에 추가되었습니다. 가격: {price}원\n")
            elif x3_1=="2":
                print("취소되었습니다. 다시입력해주세요.\n")
                printmenu(menu1)
                continue
            else:
                print("잘못입력되었습니다.다시입력해주세요.\n")
                printmenu(menu1)
                continue
        elif x3 =="2":
            print(list(s1["3.사이드"].keys())[:6])  # 크기에 맞는 사이드
            x_1 = int(input("사이드메뉴 선택: "))
            side_selected = list(s1["3.사이드"].keys())[x_1 - 1]
            print(list(s1["6.음료"].keys())[:5])
            x_2 = int(input("음료메뉴 선택: "))
            drink_selected = list(s1["6.음료"].keys())[x_2 - 1]
            print("----고르신 메뉴----")
            print(f"메뉴: {food[2:]}")
            print(f"사이드:{side_selected[2:]}")       #숫자슬라이싱
            print(f"음료: {drink_selected[2:]}")
            x3_2 = input("장바구니에 1.추가 2.취소 ")
            if x3_2=="1":
                print(f"{food[2:]} 상품이 주문목록에 추가되었습니다. 가격: {price}원\n")
            elif x3_2=="2":
                print("취소되었습니다. 다시입력해주세요.\n")
                printmenu(menu1)
                continue
            else:
                print("잘못입력되었습니다.다시입력해주세요.\n")
                printmenu(menu1)
                continue
        elif x3 =="0":
            continue
        else:
            continue
        cart.append((food, price))
        break
    while menu1 == s1["9.맥모닝"]:
        print("\n상품번호를 입력해주세요. 0.처음으로(초기화)")
        choice = int(input("메뉴 선택:"))
        if choice == 0:
            cart.clear()
            break
        elif 0 < choice <= len(menu1):
            food = list(menu1.keys())[choice - 1]
            price = menu1[food]
            x3 = input("1.세트로 변경(+1500원) 2.변경안함 (뒤로가기:0)")
            if x3 == "1":
                print(list(s1["3.사이드"].keys())[:6])  # 크기에 맞는 사이드
                x_1 = int(input("사이드메뉴 선택: "))
                side_selected = list(s1["3.사이드"].keys())[x_1 - 1]
                print(list(s1["6.음료"].keys())[:5])
                x_2 = int(input("음료메뉴 선택: "))
                drink_selected = list(s1["6.음료"].keys())[x_2 - 1]
                print("----고르신 메뉴----")
                print(f"메뉴: {food[2:]}")
                print(f"사이드:{side_selected[2:]}")
                print(f"음료: {drink_selected[2:]}")
                x3_1 = input("장바구니에 1.추가 2.취소 ")
                if x3_1 == "1":
                    price += 1500
                    print(f"{food[2:]} 세트가 주문목록에 추가되었습니다. 가격: {price}원\n")
                elif x3_1 == "2":
                    print("취소되었습니다. 다시입력해주세요.\n")
                    printmenu(menu1)
                    continue
                else:
                    print("잘못입력되었습니다.다시입력해주세요.\n")
                    printmenu(menu1)
                    continue
            elif x3 =="2":
                x3_2 = input("장바구니에 1.추가 2.취소 ")
                if x3_2 == "1":
                    print(f"{food[2:]} 상품이 주문목록에 추가되었습니다. 가격: {price}원\n")
                elif x3_2 == "2":
                    print("취소되었습니다. 다시입력해주세요.\n")
                    printmenu(menu1)
                    continue
                else:
                    print("잘못입력되었습니다.다시입력해주세요.\n")
                    printmenu(menu1)
                    continue
            elif x3 == "0":
                printmenu(menu1)
                continue
            else:
                print("잘못입력되었습니다. 다시입력해주세요.")
                printmenu(menu1)
                continue
            cart.append((food, price))
            break
    while menu1==s1["1.버거"]["1.전체"] or menu1==s1["1.버거"]["2.비프"] or menu1==s1["1.버거"]["3.치킨"]:
        print("\n상품번호를 입력해주세요. 0.처음으로(초기화)")
        choice = int(input("메뉴 선택:"))
        if choice == 0:
            cart.clear()
            break
        elif 0 < choice <= len(menu1):
            food = list(menu1.keys())[choice - 1]
            price = menu1[food]
            # 세트선택 여부 확인
            x = input("1.단품선택 2.세트선택(+1500원) 3.라지세트선택(+2300원) 4.뒤로가기  0.처음으로(초기화) ")
            if x == "1":
                x2 = input("장바구니에 1.추가 2.취소 ")
                if x2 == "1":
                    print(f"{food[2:]} 상품이 주문목록에 추가되었습니다. 가격: {price}원\n")
                elif x2 == "2":
                    print("취소되었습니다. 다시입력해주세요.\n")
                    printmenu(menu1)
                    continue
                else:
                    print("잘못입력되었습니다.다시입력해주세요.\n")
                    printmenu(menu1)
                    continue
            elif x == "2":
                print(list(s1["3.사이드"].keys())[:6])      #크기에 맞는 사이드
                x_1 = int(input("사이드메뉴 선택: "))
                side_selected = list(s1["3.사이드"].keys())[x_1 - 1]
                print(list(s1["6.음료"].keys())[:5])
                x_2 = int(input("음료메뉴 선택: "))
                drink_selected = list(s1["6.음료"].keys())[x_2 - 1]
                print("----고르신 메뉴----")
                print(f"메뉴:{food[2:]}")
                print(f"사이드:{side_selected[2:]}")
                print(f"음료:{drink_selected[2:]}")
                x2_1 = input("장바구니에 1.추가 2.취소 ")
                if x2_1 == "1":
                    price += 1500
                    print(f"{food[2:]}세트가 주문목록에 추가되었습니다. 가격: {price}원\n")
                elif x2_1 == "2":
                    print("취소되었습니다. 다시입력해주세요.\n")
                    printmenu(menu1)
                    continue
                else:
                    print("잘못입력되었습니다.다시입력해주세요.\n")
                    printmenu(menu1)
                    continue
            elif x == "3":
                print(list(s1["3.사이드"].keys())[6:])
                x_3 = int(input("사이드메뉴 선택: "))
                side_selected = list(s1["3.사이드"].keys())[x_3 - 1]
                print(list(s1["6.음료"].keys())[3:])
                x_4 = int(input("음료메뉴 선택: "))
                drink_selected = list(s1["6.음료"].keys())[x_4 - 1]
                print("----고르신 메뉴----")
                print(f"메뉴: {food[2:]}")
                print(f"사이드:{side_selected[2:]}")
                print(f"음료: {drink_selected[2:]}")
                x2_2 = input("장바구니에 1.추가 2.취소 ")
                if x2_2 =="1":
                    price += 2300
                    print(f"{food[2:]}라지 세트가 주문목록에 추가되었습니다. 가격: {price}원\n")
                elif x2_2 =="2":
                    print("취소되었습니다. 다시입력해주세요.\n")
                    printmenu(menu1)
                    continue
                else:
                    print("잘못입력되었습니다.다시입력해주세요.\n")
                    printmenu(menu1)
                    continue
            elif x == "0":
                cart.clear()
                break
            elif x == "4":
                printmenu(menu1)
                continue
            cart.append((food, price))
            break
        else:
            print("다시 입력해주세요.")
#주문처리함수3(해피밀메뉴)
def printcart2(menu1):
    global cart
    while True:
        print("\n상품번호를 입력해주세요. 0.처음으로(초기화)")
        choice = int(input("메뉴 선택: "))
        if choice == 0:
            cart.clear()
            break
        elif 0 < choice <= len(menu1):
            food = list(menu1.keys())[choice - 1]
            price = menu1[food]
            # 세트선택 여부 확인
            x = input("해피밀은 어린이용 세트메뉴로 사이드는 파인애플만 제공됩니다.\n"
                      "음료를 선택해주세요 1.오렌지주스 2.생수 3.뒤로가기 0.처음으로(초기화)")
            if x=="1":
                print("----고르신 메뉴----")
                print(f"메뉴: {food[2:]}")
                print(f"사이드: 파인애플")
                print(f"음료: 오렌지주즈")
                x2 = input(("장바구니에 1.추가 2.취소"))
                if x2 == "1":
                    print(f"해피밀{food[2:]} 세트상품이 주문 목록에 추가되었습니다. 가격:{price}원\n")
                elif x2=="2":
                    print("취소되었습니다. 다시입력해주세요.\n")
                    printmenu(menu1)
                    continue
                else:
                    print("잘못입력되었습니다.다시입력해주세요.\n")
                    printmenu(menu1)
                    continue
            elif x=="2":
                print("----고르신 메뉴----")
                print(f"메뉴: {food[2:]}")
                print(f"사이드: 파인애플")
                print(f"음료: 생수")
                x2=input(("장바구니에 1.추가 2.취소"))
                if x2 == "1":
                    print(f"해피밀{food[2:]} 세트상품이 주문 목록에 추가되었습니다. 가격:{price}원\n")
                elif x2=="2":
                    print("취소되었습니다. 다시입력해주세요.\n")
                    printmenu(menu1)
                    continue
                else:
                    print("잘못입력되었습니다.다시입력해주세요.\n")
                    printmenu(menu1)
                    continue
            elif x=="0":
                cart.clear()
                break
            elif x=="3":
                printmenu(menu1)
                continue
            else:
                print("잘못입력되었습니다.다시입력해주세요.\n")
                printmenu(menu1)
                continue
            cart.append((food, price))  # 상품,가격
            break
# 메인
def kiosk():
    while True:
        x = input("\n1.주문하기(1번입력): ")
        if x == "1":
            while x == "1":
                x2 = input("1.매장 2.테이크아웃 3.처음으로(초기화)")
                if x2 == "1" or x2 == "2":
                    available_menue = printcategori()
                    printmenu_time()
                    print("\n---------------------------------")
                    x3 = input("원하시는 메뉴의 번호를 입력해주세요:")
                    if x3 =="1" and "1.버거" in available_menue:
                        print("---버거 카테고리 선택---")
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
                    elif x3 == "2" and "2.해피스낵" in available_menue:
                        print("해피스낵 메뉴:")
                        printmenu(s1["2.해피스낵"])
                        printcart(s1["2.해피스낵"])
                        break
                    elif x3 == "3" and "3.사이드" in available_menue:
                        print("사이드 메뉴:")
                        printmenu(s1["3.사이드"])
                        printcart(s1["3.사이드"])
                        break
                    elif x3 == "4" and "4.디저트" in available_menue:
                        print("디저트 메뉴:")
                        printmenu(s1["4.디저트"])
                        printcart(s1["4.디저트"])
                        break
                    elif x3 == "5" and "5.맥카페" in available_menue:
                        print("맥카페 메뉴:")
                        printmenu(s1["5.맥카페"])
                        printcart(s1["5.맥카페"])
                        break
                    elif x3 == "6" and "6.음료" in available_menue:
                        print("음료 메뉴:")
                        printmenu(s1["6.음료"])
                        printcart(s1["6.음료"])
                        break
                    elif x3 == "7" and "7.해피밀" in available_menue:
                        print("해피밀 메뉴:")
                        if start_morning <= now <= end_morning:
                            printmenu(s1["7.해피밀"]["1.해피밀(맥머핀 종류)"])
                            printcart2(s1["7.해피밀"]["1.해피밀(맥머핀 종류)"])
                            break
                        elif next_morning1 <= now <= next_morning:
                            printmenu(s1["7.해피밀"]["2.해피밀(버거 종류)"])
                            printcart2(s1["7.해피밀"]["2.해피밀(버거 종류)"])
                            break
                    elif x3 == "8" and "8.맥런치" in available_menue:
                        print("맥런치 메뉴:")
                        printmenu(s1["8.맥런치"])
                        printcart1(s1["8.맥런치"])
                        break
                    elif x3 == "9" and "9.맥모닝" in available_menue:
                        print("맥모닝 메뉴:")
                        printmenu(s1["9.맥모닝"])
                        printcart1(s1["9.맥모닝"])
                        break
                    else:
                        print("잘못 입력되었습니다. \n가능한 메뉴의 번호를 다시 입력해주세요.")
                        cart.clear()
                        kiosk()
                elif x2=="3":
                    cart.clear()
                    kiosk()
                else:
                    print("잘못입력되었습니다.\n다시입력해주세요.")
            if len(cart) ==0:
                print("장바구니에 담긴 상품이 없습니다. 처음으로 돌아갑니다.")
                kiosk()
            else:
                while len(cart) != 0:
                    x4 = input("1.주문완료 2.추가주문 3.장바구니비우기")
                    if x4 == "1":
                        printfinish()
                        break
                    elif x4 == "2":
                        break
                    elif x4 == "3":
                        print("장바구니를 비웠습니다. 처음 화면으로 돌아갑니다.")
                        cart.clear()  # 초기화하고 재실행
                        break
                    else:
                        print("잘못입력되었습니다.\n다시입력해주세요.")
        else:
            print("잘못입력되었습니다.\n주문하시려면 숫자1을 다시 입력해주세요.")
kiosk()