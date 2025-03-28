import tkinter as tk
import tkinter.messagebox as msgbox
import naviframe  # 양승준님 코드
from color import Color
# tkcalendar 달력 선택 패키지 설치 필수
from tkcalendar import DateEntry  # 날짜 선택을 위한 모듈 추가
# from tablewidget import TableWidget
# from datetime import datetime
import json
from tablewidget import TableWidget
from tkinter import ttk
dbm = None


class order(tk.Frame):

  def __init__(self, root):
    super().__init__(root, width=1300, height=700)
    self.root = root
    self.frameX = 300
    self.frameY = 130

    # frame 생성
    self.topleft_Frame = tk.Frame(self, width=950, height=350)  # 왼쪽 위 구역
    self.topright_Frame = tk.Frame(self, width=350, height=350)  # 오른쪽 위 구역
    self.bottom_Frame = tk.Frame(self, width=1300, height=350)  # 아래 구역

    # frame 크기 자동 축소 방지
    self.topleft_Frame.grid_propagate(False)
    self.topleft_Frame.pack_propagate(False)
    self.topright_Frame.grid_propagate(False)
    self.topright_Frame.pack_propagate(False)
    self.bottom_Frame.grid_propagate(False)
    self.bottom_Frame.pack_propagate(False)

    # frame 배치
    self.topleft_Frame.grid(row=0, column=0)
    self.topright_Frame.grid(row=0, column=1)
    self.bottom_Frame.grid(row=1, column=0, columnspan=2)

    # 발주서 입력 필드 생성
    self.create_order_form()

  # 기본 화면
  def create_order_form(self):  # 등록
    w = 14
    e = 15
    self.topleft_Frame.grid_columnconfigure(0, weight=1)  # 라벨 컬럼
    self.topleft_Frame.grid_columnconfigure(1, weight=2)  # 입력 필드 컬럼
    self.topleft_Frame.grid_columnconfigure(2, weight=1)  # 라벨 컬럼
    self.topleft_Frame.grid_columnconfigure(3, weight=2)  # 입력 필드 컬럼
    self.topleft_Frame.grid_columnconfigure(4, weight=1)  # 라벨 컬럼
    self.topleft_Frame.grid_columnconfigure(5, weight=2)  # 입력 필드 컬럼

    # 작성일자 > 발주서 코드 > 내/외> 작성자에 대한 > 완제품 코드 >
    self.order_label = ttk.Label(self.topleft_Frame, width=w,text="작성 일자", anchor="w")
    self.order_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
    self.order_date = DateEntry(self.topleft_Frame,width=w, foreground="white",
                                date_pattern="yyyy.mm.dd", state="disabled")
    self.order_date.grid(row=0, column=1, padx=5, pady=5,sticky="ew")

    self.ordercode_label = ttk.Label(self.topleft_Frame,width=w, text="발주서 코드" , anchor="w")
    self.ordercode_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
    self.order_entry = ttk.Entry(self.topleft_Frame, width=e, state="disabled")
    self.order_entry.grid(row=1, column=1, padx=5, pady=5,sticky="ew")

    self.inout_label = ttk.Label(self.topleft_Frame, width=w, text="내/외부", anchor="w")
    self.inout_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")
    self.inout_entry = ttk.Entry(self.topleft_Frame, width=e, state="disabled")
    self.inout_entry.grid(row=2, column=1, padx=5, pady=5,sticky="ew")

    self.order_author = ttk.Label(self.topleft_Frame,width=w, text="작성자 명", anchor="w")
    self.order_author.grid(row=3, column=0, padx=10, pady=5, sticky="w")
    self.author_entry = ttk.Entry(self.topleft_Frame, width=e, state="disabled")
    self.author_entry.grid(row=3, column=1, padx=5, pady=5,sticky="ew")

    self.author_position_label = ttk.Label(self.topleft_Frame,width=w, text="작성자 직책", anchor="w")
    self.author_position_label.grid(row=4, column=0, padx=10, pady=5, sticky="w")
    self.author_position_antry = ttk.Entry(self.topleft_Frame, width=e, state="disabled")
    self.author_position_antry.grid(row=4, column=1, padx=5, pady=5,sticky="ew")

    self.author_phone_label = ttk.Label(self.topleft_Frame,width=w, text="작성자 연락처", anchor="w")
    self.author_phone_label.grid(row=5, column=0, padx=10, pady=5, sticky="w")
    self.author_phone_entry = ttk.Entry(self.topleft_Frame, width=e, state="disabled")
    self.author_phone_entry.grid(row=5, column=1, padx=5, pady=5,sticky="ew")

    self.author_email_label = ttk.Label(self.topleft_Frame,width=w, text="작성자 이메일", anchor="w")
    self.author_email_label.grid(row=6, column=0, padx=10, pady=5, sticky="w")
    self.author_email_entry = ttk.Entry(self.topleft_Frame, width=e, state="disabled")
    self.author_email_entry.grid(row=6, column=1, padx=5, pady=5,sticky="ew")

    self.manager_label = ttk.Label(self.topleft_Frame,width=w, text="관리자 명", anchor="w")
    self.manager_label.grid(row=7, column=0, padx=10, pady=5, sticky="w")
    self.manager_entry = ttk.Entry(self.topleft_Frame, width=e, state="disabled")
    self.manager_entry.grid(row=7, column=1, padx=5, pady=5,sticky="ew")

    self.manager_position_label = ttk.Label(self.topleft_Frame,width=w, text="관리자 직책", anchor="w")
    self.manager_position_label.grid(row=8, column=0, padx=10, pady=5, sticky="w")
    self.manager_position_entry = ttk.Entry(self.topleft_Frame, width=e, state="disabled")
    self.manager_position_entry.grid(row=8, column=1, padx=5, pady=5,sticky="ew")

    self.manager_phone_label = ttk.Label(self.topleft_Frame,width=w, text="관리자 연락처", anchor="w")
    self.manager_phone_label.grid(row=9, column=0, padx=10, pady=5, sticky="w")
    self.manager_phone_entry = ttk.Entry(self.topleft_Frame, width=e, state="disabled")
    self.manager_phone_entry.grid(row=9, column=1, padx=5, pady=5,sticky="ew")

    self.manager_email_label = ttk.Label(self.topleft_Frame,width=w, text="관리자 이메일", anchor="w")
    self.manager_email_label.grid(row=10, column=0, padx=10, pady=5, sticky="w")
    self.manager_email_entry = ttk.Entry(self.topleft_Frame, width=e, state="disabled")
    self.manager_email_entry.grid(row=10, column=1, padx=5, pady=5,sticky="ew")

    self.productcode_label = ttk.Label(self.topleft_Frame, width=w, text="완제품 코드", anchor="w")
    self.productcode_label.grid(row=0, column=2, padx=10, pady=5, sticky="w")
    self.productcode_entry = ttk.Entry(self.topleft_Frame, width=e, state="disabled")
    self.productcode_entry.grid(row=0, column=3, padx=5, pady=5, sticky="ew")

    self.product_label = ttk.Label(self.topleft_Frame,width=w, text="완제품 명", anchor="w")
    self.product_label.grid(row=1, column=2, padx=10, pady=5, sticky="w")
    self.product_entry = ttk.Entry(self.topleft_Frame, width=e, state="disabled")
    self.product_entry.grid(row=1, column=3, padx=5, pady=5,sticky="ew")

    self.unitprice_label = ttk.Label(self.topleft_Frame,width=w, text="단가", anchor="w")
    self.unitprice_label.grid(row=2, column=2, padx=10, pady=5, sticky="w")
    self.unitprice_entry = ttk.Entry(self.topleft_Frame,width=e, state="disabled")
    self.unitprice_entry.grid(row=2, column=3, padx=5, pady=5,sticky="ew")
    #
    # self.inventory_label = ttk.Label(self.topleft_Frame,width=w, text="창고", anchor="w")
    # self.inventory_label.grid(row=3, column=2, padx=10, pady=5, sticky="w")
    # self.inventory_entry = ttk.Entry(self.topleft_Frame,width=e, state="disabled")
    # self.inventory_entry.grid(row=3, column=3, padx=5, pady=5,sticky="ew")

    self.quantity_label = ttk.Label(self.topleft_Frame,width=w, text="거래 수량", anchor="w")
    self.quantity_label.grid(row=3, column=2, padx=10, pady=5, sticky="w")
    self.quantity_entry = ttk.Entry(self.topleft_Frame,width=e, state="disabled")
    self.quantity_entry.grid(row=3, column=3, padx=5, pady=5,sticky="ew")

    self.total_label = ttk.Label(self.topleft_Frame,width=w, text="총 가격", anchor="w")
    self.total_label.grid(row=4, column=2, padx=10, pady=5, sticky="w")
    self.total_entry = ttk.Entry(self.topleft_Frame,width=e, state="disabled")
    self.total_entry.grid(row=4, column=3, padx=5, pady=5,sticky="ew")

    self.VAT_label = ttk.Label(self.topleft_Frame,width=w, text="부가세", anchor="w")
    self.VAT_label.grid(row=5, column=2, padx=10, pady=5, sticky="w")
    self.VAT_antry = ttk.Entry(self.topleft_Frame,width=e, state="disabled")
    self.VAT_antry.grid(row=5, column=3, padx=5, pady=5,sticky="ew")

    self.correspondent_label = ttk.Label(self.topleft_Frame,width=w, text="거래처 코드", anchor="w")
    self.correspondent_label.grid(row=0, column=4, padx=10, pady=5, sticky="w")
    self.correspondent_combobox = ttk.Entry(self.topleft_Frame,width=e, state="disabled")
    self.correspondent_combobox.grid(row=0, column=5, padx=5, pady=5,sticky="ew")
    #
    # self.correspondent_name_label = ttk.Label(self.topleft_Frame,width=w, text="거래처 명", anchor="w")
    # self.correspondent_name_label.grid(row=1, column=4, padx=10, pady=5, sticky="w")
    # self.correspondent_name_entry = ttk.Entry(self.topleft_Frame,width=e, state="disabled")
    # self.correspondent_name_entry.grid(row=1, column=5, padx=5, pady=5,sticky="ew")
    #
    # self.type_label = ttk.Label(self.topleft_Frame,width=w, text="거래처 종류", anchor="w")
    # self.type_label.grid(row=2, column=4, padx=10, pady=5, sticky="w")
    # self.type_entry = ttk.Entry(self.topleft_Frame,width=e, state="disabled")
    # self.type_entry.grid(row=2, column=5, padx=5, pady=5,sticky="ew")
    #
    # self.address_label = ttk.Label(self.topleft_Frame,width=w, text="거래처 주소(국가)", anchor="w")
    # self.address_label.grid(row=3, column=4, padx=10, pady=5, sticky="w")
    # self.address_entry = ttk.Entry(self.topleft_Frame,width=e, state="disabled")
    # self.address_entry.grid(row=3, column=5, padx=5, pady=5,sticky="ew")
    #
    # self.account_manager_label = ttk.Label(self.topleft_Frame,width=w, text="거래처 담당자명", anchor="w")
    # self.account_manager_label.grid(row=4, column=4, padx=10, pady=5, sticky="w")
    # self.account_manager_entry = ttk.Entry(self.topleft_Frame,width=e, state="disabled")
    # self.account_manager_entry.grid(row=4, column=5, padx=5, pady=5,sticky="ew")
    #
    # self.account_phone_labe = ttk.Label(self.topleft_Frame,width=w, text="담당자 연락처", anchor="w")
    # self.account_phone_labe.grid(row=5, column=4, padx=10, pady=5, sticky="w")
    # self.account_phone_entry = ttk.Entry(self.topleft_Frame,width=e, state="disabled")
    # self.account_phone_entry.grid(row=5, column=5, padx=5, pady=5,sticky="ew")
    #
    # self.account_email_label = ttk.Label(self.topleft_Frame, width=w,text="담당자 이메일", anchor="w")
    # self.account_email_label.grid(row=6, column=4, padx=10, pady=5, sticky="w")
    # self.account_email_entry = ttk.Entry(self.topleft_Frame,width=e, state="disabled")
    # self.account_email_entry.grid(row=6, column=5, padx=5, pady=5,sticky="ew")

    self.sledding_label = ttk.Label(self.topleft_Frame,width=w, text="진행 상태", anchor="w")
    self.sledding_label.grid(row=1, column=4, padx=10, pady=5, sticky="w")
    self.sledding_entry = ttk.Entry(self.topleft_Frame,width=e, state="disabled")
    self.sledding_entry.grid(row=1, column=5, padx=5, pady=5,sticky="ew")

    self.deadline_label = ttk.Label(self.topleft_Frame,width=w, text="납기일", anchor="w")
    self.deadline_label.grid(row=2, column=4, padx=10, pady=5, sticky="w")
    self.deadline_entry = DateEntry(self.topleft_Frame, foreground="white",
                                    date_pattern="yyyy.mm.dd", state="disabled")
    self.deadline_entry.grid(row=2, column=5, padx=5, pady=5,sticky="ew")

    self.modification_label = ttk.Label(self.topleft_Frame,width=w, text="수정 일자", anchor="w")
    self.modification_label.grid(row=3, column=4, padx=10, pady=5, sticky="w")
    self.modification_entry = DateEntry(self.topleft_Frame, foreground="white",
                                        date_pattern="yyyy.mm.dd", state="disabled")
    self.modification_entry.grid(row=3, column=5, padx=5, pady=5,sticky="ew")

    # 오른쪽 위
    # 조회
    self.topright_Frame.columnconfigure(0, weight=1, uniform="equal")  # column 1에 비례적으로 공간 분배
    self.topright_Frame.columnconfigure(1, weight=1, uniform="equal")  # column 2에도 동일하게 적용
    self.topright_Frame.columnconfigure(2, weight=1, uniform="equal")

    self.labela = ttk.Label(self.topright_Frame,width=w, text="발주서 코드", anchor="w")
    self.labela.grid(row=0, column=0, padx=10, pady=5, sticky="w")
    self.allOrdering_entry = ttk.Entry(self.topright_Frame,width=15)
    self.allOrdering_entry.grid(row=0, column=1, padx=5, pady=5,sticky="ew")

    self.labelc = ttk.Label(self.topright_Frame,width=w, text="완제품 명", anchor="w")
    self.labelc.grid(row=1, column=0, padx=10, pady=5, sticky="w")
    self.allproduction_entry = ttk.Entry(self.topright_Frame,width=15)
    self.allproduction_entry.grid(row=1, column=1, padx=5, pady=5,sticky="ew")

    self.labeld = ttk.Label(self.topright_Frame,width=w, text="거래처 코드", anchor="w")
    self.labeld.grid(row=2, column=0, padx=10, pady=5, sticky="w")
    self.allCorrespondent_entry = ttk.Entry(self.topright_Frame,width=15)
    self.allCorrespondent_entry.grid(row=2, column=1, padx=5, pady=5,sticky="ew")

    self.labele = ttk.Label(self.topright_Frame,width=w, text="관리자", anchor="w")
    self.labele.grid(row=3, column=0, padx=10, pady=5, sticky="w")
    self.entryd = ttk.Entry(self.topright_Frame,width=15)
    self.entryd.grid(row=3, column=1, padx=5, pady=5,sticky="ew")

    self.labelz = ttk.Label(self.topright_Frame,width=w, text="납기일", anchor="w")
    self.labelz.grid(row=5, column=0, padx=10, pady=5, sticky="w")
    self.date_entry4 = DateEntry(self.topright_Frame,width=e, foreground="white", date_pattern="yy.mm.dd")
    self.date_entry4.grid(row=5, column=1, padx=5, pady=6, sticky="ew")  # sticky="nsew"로 모든 방향에 맞게 채우기

    self.date_entry5 = DateEntry(self.topright_Frame,width=e, foreground="white", date_pattern="yy.mm.dd")
    self.date_entry5.grid(row=5, column=2, padx=5, pady=6, sticky="ew")  # sticky="nsew"로 모든 방향에 맞게 채우기

    self.labelf = ttk.Label(self.topright_Frame, text="작성일자",width=w, anchor="w")
    self.labelf.grid(row=6, column=0, padx=10, pady=5, sticky="w")

    self.creation_date_start = DateEntry(self.topright_Frame, width=e, foreground="white",
                                         date_pattern="yy.mm.dd")
    self.creation_date_start.grid(row=6, column=1, padx=5, pady=5, sticky="ew")

    self.creation_date_end = DateEntry(self.topright_Frame, width=e, foreground="white",
                                       date_pattern="yy.mm.dd")
    self.creation_date_end.grid(row=6, column=2, padx=5, pady=5, sticky="ew")

    self.labelg = ttk.Label(self.topright_Frame, text="수정 일자",width=w, anchor="w")
    self.labelg.grid(row=7, column=0, padx=10, pady=5, sticky="w")

    self.modified_date_start = DateEntry(self.topright_Frame, width=e, foreground="white",date_pattern="yy.mm.dd")
    self.modified_date_start.grid(row=7, column=1, padx=5, pady=5, sticky="ew")

    self.modified_date_end = DateEntry(self.topright_Frame, width=e, foreground="white",date_pattern="yy.mm.dd")
    self.modified_date_end.grid(row=7, column=2, padx=5, pady=5, sticky="ew")

    self.btn_search = ttk.Button(self.topright_Frame, text="조회", command=self.select_point)
    self.btn_search.grid(row=0, column=2, columnspan=2, padx=10, pady=5, sticky="e")

    # 눌러야 활성화 되면서 작성 가능하게
    self.btn_create = ttk.Button(self.topright_Frame, text="생성", command=self.create_new_entry)
    self.btn_create.grid(row=1, column=2, columnspan=2, padx=10, pady=5, sticky="e")

    # 눌러야 활성화 되면서 작성 가능하게
    self.btn_update = ttk.Button(self.topright_Frame, text="수정", command=self.edit_existing_entry)
    self.btn_update.grid(row=2, column=2, columnspan=2, padx=10, pady=5, sticky="e")

    # 생성과 등록 모두가 사용
    self.btn_save = ttk.Button(self.topright_Frame, text="저장", command=self.create_point)
    self.btn_save.grid(row=3, column=2, columnspan=2, padx=10, pady=5, sticky="e")

    self.btn_delete = ttk.Button(self.topright_Frame, text='삭제', command=self.enable_order_entry)
    self.btn_delete.grid(row=4, column=2, columnspan=2, padx=10, pady=5, sticky="e")

    # 상태 추적을 위한 변수
    self.mode = None  # 현재 모드를 추적 (None, 'create', 'update')

  #     여기부터 생성,수정,조회
  def activate_fields(self):
    # 입력 필드 활성화
    self.order_date.config(state="normal")
    self.order_entry.config(state="normal")
    self.inout_entry.config(state="normal")
    self.author_entry.config(state="normal")
    self.author_position_antry.config(state="normal")
    self.author_phone_entry.config(state="normal")
    self.author_email_entry.config(state="normal")
    self.manager_entry.config(state="normal")
    self.manager_position_entry.config(state="normal")
    self.manager_phone_entry.config(state="normal")
    self.manager_email_entry.config(state="normal")
    self.productcode_entry.config(state="normal")
    self.product_entry.config(state="normal")
    self.unitprice_entry.config(state="normal")
    # self.inventory_entry.config(state="normal")
    self.quantity_entry.config(state="normal")
    self.total_entry.config(state="normal")
    self.VAT_antry.config(state="normal")
    self.correspondent_combobox.config(state="normal")
    # self.correspondent_name_entry.config(state="normal")
    # self.type_entry.config(state="normal")
    # self.address_entry.config(state="normal")
    # self.account_manager_entry.config(state="normal")
    # self.account_phone_entry.config(state="normal")
    # self.account_email_entry.config(state="normal")
    self.sledding_entry.config(state="normal")
    self.deadline_entry.config(state="normal")

  def deactivate_fields(self):
    # 입력 필드 비활성화
    self.order_date.config(state="disabled")
    self.order_entry.config(state="disabled")  # 발주 코드 필드를 비활성화
    self.inout_entry.config(state="disabled")
    self.author_entry.config(state="disabled")
    self.author_position_antry.config(state="disabled")
    self.author_phone_entry.config(state="disabled")
    self.author_email_entry.config(state="disabled")
    self.manager_entry.config(state="disabled")
    self.manager_position_entry.config(state="disabled")
    self.manager_phone_entry.config(state="disabled")
    self.manager_email_entry.config(state="disabled")
    self.productcode_entry.config(state="disabled")
    self.product_entry.config(state="disabled")
    self.unitprice_entry.config(state="disabled")
    # self.inventory_entry.config(state="disabled")
    self.quantity_entry.config(state="disabled")
    self.total_entry.config(state="disabled")
    self.VAT_antry.config(state="disabled")
    self.correspondent_combobox.config(state="disabled")
    # self.correspondent_name_entry.config(state="disabled")
    # self.type_entry.config(state="disabled")
    # self.address_entry.config(state="disabled")
    # self.account_manager_entry.config(state="disabled")
    # self.account_phone_entry.config(state="disabled")
    # self.account_email_entry.config(state="disabled")
    self.sledding_entry.config(state="disabled")
    self.deadline_entry.config(state="disabled")

  def clear_fields(self):
    self.order_date.delete(0, tk.END)
    self.order_entry.delete(0, tk.END)
    self.inout_entry.delete(0, tk.END)
    self.author_entry.delete(0, tk.END)
    self.author_position_antry.delete(0, tk.END)
    self.author_phone_entry.delete(0, tk.END)
    self.author_email_entry.delete(0, tk.END)
    self.manager_entry.delete(0, tk.END)
    self.manager_position_entry.delete(0, tk.END)
    self.manager_phone_entry.delete(0, tk.END)
    self.manager_email_entry.delete(0, tk.END)
    self.productcode_entry.delete(0,tk.END)
    self.product_entry.delete(0, tk.END)
    self.unitprice_entry.delete(0, tk.END)
    # self.inventory_entry.delete(0, tk.END)
    self.quantity_entry.delete(0, tk.END)
    self.total_entry.delete(0, tk.END)
    self.VAT_antry.delete(0, tk.END)
    self.correspondent_combobox.delete(0, tk.END)
    # self.correspondent_name_entry.delete(0, tk.END)
    # self.type_entry.delete(0, tk.END)
    # self.address_entry.delete(0, tk.END)
    # self.account_manager_entry.delete(0, tk.END)
    # self.account_phone_entry.delete(0, tk.END)
    # self.account_email_entry.delete(0, tk.END)
    self.sledding_entry.delete(0, tk.END)
    self.deadline_entry.delete(0, tk.END)

  def create_new_entry(self):
    # 생성
    self.activate_fields()  # 필드 활성화
    self.mode = 'create'

  def edit_existing_entry(self):
    # 수정
    self.activate_fields()
    self.modification_entry.config(state="normal")
    self.mode = 'update'

  def enable_order_entry(self):
    self.order_entry.config(state='normal')  # 입력 가능하게 변경
    self.mode = 'delete'
    self.delete_point()

  def delete_point(self):
    order_code = self.order_entry.get()  # 발주 코드
    if not order_code:  # 발주 코드가 없으면 실행 안 함
      return

    send = {
      "code": 30304,
      "args": {
        "order_code": order_code  # 발주 코드
      }
    }
    self.send_(send)  # 서버에 삭제 요청

  def create_point(self):
    # 필드 값들
    print("전송 준비 중")
    order_code = self.order_entry.get()  # 발주 코드
    product_code = self.productcode_entry.get() # 완제품 코드
    product_name = self.product_entry.get()  # 완제품 명
    internal_external = self.inout_entry.get()  # 내/외부
    creator_name = self.author_entry.get()  # 작성자 명
    creator_position = self.author_position_antry.get()  # 작성자 직책
    creator_phone = self.author_phone_entry.get()  # 작성자 연락처
    creator_email = self.author_email_entry.get()  # 작성자 이메일
    administrator_name = self.manager_entry.get()  # 관리자
    administrator_position = self.manager_position_entry.get()  # 관리자 직책
    administrator_phone = self.manager_phone_entry.get()  # 관리자 연락처
    administrator_email = self.manager_email_entry.get()  # 관리자 이메일
    unit_price = self.unitprice_entry.get()  # 단가
    # stock = self.inventory_entry.get()  # 창고,재고

    transaction_quantity = self.quantity_entry.get()  # 거래 수량
    total_price = self.total_entry.get()  # 총 가격
    order_vat = self.VAT_antry.get()  # 부가세

    # 거래처 관련 항목들
    Customer_code = self.correspondent_combobox.get()  # 거래처 코드
    # correspondent_name = self.correspondent_name_entry.get()  # 거래처 명
    # correspondent_type = self.type_entry.get()  # 거래처 종류
    # account_address = self.address_entry.get()  # 거래처 주소(국가)
    # account_manager = self.account_manager_entry.get()  # 거래처 담당자
    # manager_phone = self.account_phone_entry.get()  # 거래처 담당자 연락처
    # manager_email = self.account_email_entry.get()  # 거래처 담당자 이메일

    sledding = self.sledding_entry.get()  # 운반
    delivery_date = self.deadline_entry.get_date()  # 납기일
    delivery_date = delivery_date.strftime('%Y-%m-%d')
    creation_date = self.order_date.get_date()  # 작성일자
    creation_date = creation_date.strftime('%Y-%m-%d')
    if self.mode == 'update':
      modified_date = self.modification_entry.get_date()  # 수정일자
      modified_date = modified_date.strftime('%Y-%m-%d')
    else:
      modified_date = None

    # 데이터 전송 구조
    if self.mode == 'update':
      code = 30303
    else:
      code = 30302

    send = {
      "code": code,
      "args": {
        "order_code": order_code,  # 발주 코드
        "product_code":product_code,
        "product_name": product_name,  # 완제품 명
        "internal_external": internal_external,  # 내/외부
        "creator_name": creator_name,  # 작성자 명
        "creator_position": creator_position,  # 작성자 직책
        "creator_phone": creator_phone,  # 작성자 연락처
        "creator_email": creator_email,  # 작성자 이메일
        "administrator_name": administrator_name,  # 관리자 이름
        "administrator_position": administrator_position,  # 관리자 직책
        "administrator_phone": administrator_phone,  # 관리자 연락처
        "administrator_email": administrator_email,  # 관리자 이메일
        "unit_price": unit_price,  # 단가
        # "stock": stock,  # 현 재고
        "transaction_quantity": transaction_quantity,  # 거래 수량
        "total_price": total_price,  # 총 가격
        "order_vat": order_vat,  # 부가세
        "Customer_code": Customer_code,  # 거래처 코드
        # "account_name": correspondent_name,  # 거래처 명
        # "account_type": correspondent_type,  # 거래처 종류
        # "account_address": account_address,  # 거래처 주소(국가)
        # "account_manager": account_manager,  # 거래처 담당자
        # "manager_phone": manager_phone,  # 거래처 담당자 연락처
        # "manager_email": manager_email,  # 거래처 담당자 이메일
        "sledding": sledding,  # 창고
        "delivery_date": delivery_date,  # 납기일
        "creation_date": creation_date,  # 작성일자
        "modified_date": modified_date  # 수정일자
      }
    }

    if self.mode == 'update':
      print(send)
      self.send_(send)
    elif self.mode == 'create':
      print(send)
      self.send_(send)

  def select_point(self):
    # 조건값 가져오기
    order_code = self.allOrdering_entry.get().strip() or None
    product_name = self.allproduction_entry.get().strip() or None
    correspondent_code = self.allCorrespondent_entry.get().strip() or None
    administrator = self.entryd.get().strip() or None

    delivery_date_start = self.date_entry4.get_date()
    delivery_date_start = delivery_date_start.strftime('%Y-%m-%d') if delivery_date_start else None

    delivery_date_end = self.date_entry5.get_date()
    delivery_date_end = delivery_date_end.strftime('%Y-%m-%d') if delivery_date_end else None

    creation_date_start = self.creation_date_start.get_date()
    creation_date_start = creation_date_start.strftime('%Y-%m-%d') if creation_date_start else None

    creation_date_end = self.creation_date_end.get_date()
    creation_date_end = creation_date_end.strftime('%Y-%m-%d') if creation_date_end else None

    modified_date_start = self.modified_date_start.get_date()
    modified_date_start = modified_date_start.strftime('%Y-%m-%d') if modified_date_start else None

    modified_date_end = self.modified_date_end.get_date()
    modified_date_end = modified_date_end.strftime('%Y-%m-%d') if modified_date_end else None

    send = {
      "code": 30301,
      "args": {
        "order_code": order_code,
        "product_name": product_name,
        "correspondent_code": correspondent_code,
        "administrator": administrator,
        "delivery_date_start": delivery_date_start,
        "delivery_date_end": delivery_date_end,
        "creation_date_start": creation_date_start,
        "creation_date_end": creation_date_end,
        "modified_date_start": modified_date_start,
        "modified_date_end": modified_date_end,
      }
    }
    try:
      json_data = json.dumps(send)  # JSON 변환 시도
      print("json_data:", json_data)  # 정상 변환되었는지 출력
      self.send_(send)  # 최종 전송
    except TypeError as e:
      print("JSON 변환 오류 발생:", e)

  # # 발주서 조회
  # @staticmethod
  # def f30301(**kwargs):
  #   # DB 연결
  #   # 조회할 컬럼
  #   columns = [
  #     'o.creation_date', 'o.order_code', 'o.internal_external', 'o.creator_name', 'o.administrator_name',
  #     'o.product_code',
  #     'o.product_name', 'o.unit_price', 'o.transaction_quantity', 'o.total_price', 'o.order_vat',
  #     'o.Customer_code', 'c.Customer_name', 'c.Type_business', 'c.ContactPerson_name', 'c.Type_business',
  #     'c.business_adress', 'c.ContactPerson_name',
  #     'c.e_mail', 'c.ContactPerson_phone', 'o.delivery_date', 'o.modified_date'
  #   ]
  #
  #   # 기본 쿼리
  #   sql_query = f'''
  #         SELECT {", ".join(columns)}
  #         FROM erp_db.order_form o
  #         INNER JOIN erp_db.customer_management c
  #         ON o.Customer_code = c.Customer_code
  #     '''
  #
  #   conditions = []  # 조건 리스트 초기화
  #   start_value, end_value = None, None  # 날짜 변수 초기화
  #
  #   for key, value in kwargs.items():
  #     print("select:", key, value)
  #     if value is not None:
  #       column_name = key  # 기본적으로 key를 column_name으로 설정
  #
  #       # 시작 날짜 처리 (start와 관련된 처리)
  #       if "start" in key:
  #         start_value = value
  #         column_name = key.replace('_start', '')  # '_start'를 제거하여 실제 컬럼명 추출
  #         if start_value:
  #           current_date = datetime.datetime.now().strftime('%Y-%m-%d')
  #           if start_value != current_date:  # 오늘 날짜가 아니면 조건 추가
  #             conditions.append(f"o.{column_name} >= '{start_value} 00:00:00'")
  #
  #       # 종료 날짜 처리 (end와 관련된 처리)
  #       elif "end" in key:
  #         end_value = value
  #         column_name = key.replace('_end', '')  # '_end'를 제거하여 실제 컬럼명 추출
  #         if end_value:
  #           if start_value == end_value:
  #             # start와 end 값이 같으면 조건을 추가하지 않음
  #             continue
  #           conditions.append(f"o.{column_name} <= '{end_value} 23:59:59'")
  #
  #       # 일반적인 값 비교 처리
  #       elif isinstance(value, str):  # 문자열일 때 LIKE 조건
  #         conditions.append(f"o.{column_name} LIKE '%{value}%'")
  #       else:  # 문자열이 아닐 때 (정확한 값 비교)
  #         conditions.append(f"o.{column_name} = '{value}'")
  #
  #   # WHERE 절이 존재할 경우 조건
  #   if conditions:
  #     sql_query += " WHERE " + " AND ".join(conditions)
  #
  #   # 최종 SQL 쿼리
  #   print("쿼리:", sql_query)
  #   result = dbm.query(sql_query)
  #   print(result)
  #
  #   if result is not None:
  #     # datetime 문자열
  #     result = [
  #       tuple(item.strftime('%Y.%m.%d') if isinstance(item, datetime.datetime) else item for item in row)
  #       for row in result  # row에 값 넣고 item의 값을 하나씩 빼서 처리
  #     ]
  #     sign = 1
  #   else:
  #     print("오류:", result)
  #     sign = 0
  #
  #   # 결과 반환
  #   recv = {
  #     "sign": sign,
  #     "data": result if result else []  # 결과가 없으면 빈 리스트 반환
  #   }
  #   print(recv)
  #
  #   return recv

  #
  # # 발주서 생성
  # @staticmethod
  # def f30302(**kwargs):
  #   # DB 연결
  #   # 컬럼 목록
  #   columns = [
  #     'order_code', 'product_code', 'product_name', 'internal_external', 'creator_name', 'creator_position',
  #     'creator_phone', 'creator_email', 'administrator_name', 'administrator_position',
  #     'administrator_phone', 'administrator_email', 'unit_price', 'stock', 'transaction_quantity', 'total_price',
  #     'order_vat', 'Customer_code', 'sledding', 'delivery_date', 'creation_date'
  #   ]
  #
  #   values = []
  #   columns_to_insert = []
  #   print("kwargs :", kwargs.get('args'))
  #
  #   Customer_code = kwargs.get("Customer_code")
  #   print(Customer_code)
  #
  #   # Customer_code 유효성 검사
  #   if Customer_code:
  #     check_query = f"SELECT COUNT(*) FROM erp_db.customer_management WHERE Customer_code = '{Customer_code}'"
  #     check_result = dbm.query(check_query)
  #
  #     if check_result and check_result[0][0] == 0:
  #       print(f"Customer_code '{Customer_code}'가 존재하지 않습니다.")
  #       return {"sign": 0, "data": {}}
  #
  #   # kwargs에서 컬럼 값들을 처리
  #   for key, value in kwargs.items():
  #     if key in columns and value is not None:
  #       columns_to_insert.append(key)
  #       if value is None:
  #         values.append("NULL")
  #       elif isinstance(value, (int, float)):
  #         values.append(str(value))
  #       elif isinstance(value, str):
  #         values.append(f"'{value}'")
  #       else:
  #         print(f"예상치 못한 값: {key} = {value}")
  #         values.append("NULL")
  #
  #   sql_query = f"""
  #         INSERT INTO erp_db.order_form ({', '.join(columns_to_insert)})
  #         VALUES ({', '.join(values)})
  #     """
  #
  #   print("쿼리:", sql_query)
  #   result = dbm.query(sql_query)
  #   print(result)
  #
  #   sign = 1 if result is not None else 0
  #
  #   recv = {
  #     "sign": sign,
  #     "data": {}
  #   }
  #
  #   print(recv)
  #   return recv

  # 발주서 수정
  # @staticmethod
  # def f30303(**kwargs):
  #   # 초기화
  #   values = []
  #   Customer_code = kwargs.get("Customer_code")
  #   print(Customer_code)
  #
  #   # Customer_code 유효성 검사
  #   if Customer_code:
  #     check_query = f"SELECT COUNT(*) FROM erp_db.customer_management WHERE Customer_code = '{Customer_code}'"
  #     check_result = dbm.query(check_query)
  #
  #     if check_result and check_result[0][0] == 0:
  #       print(f"Customer_code '{Customer_code}'가 존재하지 않습니다.")
  #       return {"sign": 0, "data": {}}
  #
  #   for key, value in kwargs.items():
  #     if value not in [None, '']:  # 값이 None이 아니고 빈 문자열이 아닐 때만 처리
  #       values.append(f"{key} = '{value}'")
  #   sql_query = f"UPDATE erp_db.order_form SET "
  #   sql_query += ", ".join(values)
  #   sql_query += f" WHERE order_code = '{kwargs['order_code']}'"
  #   result = dbm.query(sql_query)
  #   # 쿼리 실행
  #   if result is not None:
  #     sign = 1
  #   else:
  #     print("오류:", result)
  #     sign = 0
  #   # 결과 반환
  #   recv = {"sign": sign, "data": []}
  #   return recv

  def send_(self, some_dict):
    self.root.send_(json.dumps(some_dict, ensure_ascii=False))

  def recv(self, **kwargs):
    code, sign, data = kwargs.get("code"), kwargs.get("sign"), kwargs.get("data")
    print("code:", code)
    print("sign:", sign)
    print("data:", data)

    if code == 30301:
      if sign == 1:
          if isinstance(data, list) and len(data) > 0:
              if any(data[0]):
                  self.table = TableWidget(self.bottom_Frame,
                                           data=data,
                                           col_name=["작성일자", "발주서 코드", "내/외부", "작성자명", "관리자명","완제품 코드", "완제품명", "단가", "거래수량",
                                                     "총 가격", "부가세", "거래처 코드", "거래처 이름", "거래처 종류", "담당자명", "납기일", "수정 일자"],
                                           has_checkbox=False,  # 체크박스 여부
                                           cols=17,
                                           new_row=False,  # 새로운 칸 가능 여부
                                           col_width=[100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
                                                      100, 100, 100],
                                           width=1300,  # 넓이
                                           height=350,  # 높이
                                           padding=10)
                  self.table.place(x=0, y=0)
                  # self.activate_fields()
                  # self.correspondent_name_entry.config(state="normal")
                  # self.type_entry.config(state="normal")
                  # self.address_entry.config(state="normal")
                  # self.account_manager_entry.config(state="normal")
                  # self.account_phone_entry.config(state="normal")
                  # self.account_email_entry.config(state="normal")
          else:
              msgbox.showerror("조회 오류","조회된 데이터가 없습니다.")

    elif code == 30302:
      if sign == 1:
        msgbox.showinfo("저장 성공", "저장 완료 되었습니다.")
        self.clear_fields()  # 내용 초기화
        self.deactivate_fields()  # 비활성화
      else:
        msgbox.showerror("저장 실패", "저장에 실패했습니다.")
    elif code == 30303:
      if sign == 1:
        msgbox.showinfo("수정 성공", "수정 완료 되었습니다.")
        self.clear_fields()  # 내용 초기화
        self.deactivate_fields()  # 비활성화
      else:
        msgbox.showerror("수정 실패", "발주서 코드 혹은 거래처 코드를 확인해 주시길 바랍니다.")
    elif code == 30304:
      if sign == 1:
        msgbox.showinfo("삭제 성공", "삭제 완료 되었습니다.")
        self.order_entry.delete(0, tk.END)
        self.order_entry.config(state='disabled')
      else:
        msgbox.showerror("삭제 실패", "삭제에 실패했습니다.")

  def after_init(self):
    pass


if __name__ == "__main__":
  r = tk.Tk()
  r.geometry("1600x900")
  r.config(background="white")
  fr = order(r)
  fr.place(x=300, y=130)
  r.mainloop()