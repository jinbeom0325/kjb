import tablewidget
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from tkcalendar import DateEntry
from datetime import datetime
import tkinter.messagebox as msb
import pymysql
# import dbManager
import json


# import mysql


# 초과근무 관리
class OvertimeManagement(tk.Frame):
    def __init__(self, root):
        super().__init__(root, width=1300, height=700)
        self.root = root

        # entry
        self.info_dict = {
            "사원명": [],
            "사원코드": [],
            "소속부서": [],
            "초과근무날짜": [],
            "시작시간": [],
            "종료시간": [],
            "총 초과 근무 시간": []
        }

        # 입력 프레임 (950x350, 왼쪽 위)
        self.input_frame = tk.LabelFrame(self)
        self.input_frame.place(x=0, y=30, width=950, height=350)

        self.create_input_fields()

        # 제어 프레임 (350x350, 오른쪽 위)
        self.control_frame = tk.LabelFrame(self)
        self.control_frame.place(x=950, y=30, width=350, height=350)

        self.create_control_fields()

        # 출력 프레임 (1300x350, 아래)
        self.output_frame = tk.LabelFrame(self)
        self.output_frame.place(x=0, y=380, width=1300, height=350)

        # self.create_output_fields()

    # 초과근무 시간 계산 함수
    def work_overtime(self):

        try:
            start_time = datetime.strptime(self.time_combobox1.get(), "%H:%M")
            end_time = datetime.strptime(self.time_combobox2.get(), "%H:%M")
            work_time = (end_time - start_time).total_seconds() / 3600
            overtime_hours = max(0, work_time - 8)  # 8시간 초과 근무 계산
            self.var4.set(str(overtime_hours))
        except ValueError:
            msb.showerror("오류", "올바른 시간을 선택하세요.")

    # 시작, 종료 콤보 버튼을 선택했는지 확인하는 함수.
    def on_two_combobox(self, event):
        self.event = event = None

        if self.time_combobox1.get() and self.time_combobox2.get():
            self.work_overtime()

    def create_input_fields(self):
        # 왼쪽  프레임

        self.input_left_frame = tk.LabelFrame(self)
        self.input_left_frame.place(x=0, y=30, width=237, height=350)

        # 오른쪽 프레임
        self.input_right_frame = tk.LabelFrame(self)
        self.input_right_frame.place(x=235, y=30, width=237, height=350)

        # 사원명
        self.var1 = tk.StringVar()
        self.label1 = tk.Label(self.input_left_frame, text='사원명')
        self.label1.grid(row=0, column=0, padx=5, pady=5, sticky='w')
        self.entry1 = tk.Entry(self.input_left_frame, textvariable=self.var1, width=20)
        self.entry1.grid(row=0, column=1, padx=5, pady=5)

        # 사원코드
        self.var2 = tk.StringVar()
        self.label2 = tk.Label(self.input_left_frame, text='사원코드').grid(row=1, column=0, padx=5, pady=5, sticky='w')
        self.entry2 = tk.Entry(self.input_left_frame, textvariable=self.var2, width=20)
        self.entry2.grid(row=1, column=1, padx=5, pady=5)

        # 소속부서
        self.var3 = tk.StringVar()
        self.label3 = tk.Label(self.input_left_frame, text='소속부서').grid(row=2, column=0, padx=5, pady=5, sticky='w')
        self.entry3 = tk.Entry(self.input_left_frame, textvariable=self.var3, width=20)
        self.entry3.grid(row=2, column=1, padx=5, pady=5)

        # ---------------------------------------------------------------------------------------------------------------#
        # 초과근무날짜

        self.label4 = tk.Label(self.input_right_frame, text="초과근무날짜").grid(row=0, column=0, padx=5, pady=5, sticky='w')
        self.cal_overtime = DateEntry(self.input_right_frame, selectmode='day', width=13)
        self.cal_overtime.grid(row=0, column=1, padx=5, pady=5)

        # 시간 선택
        time_options = [f"{h:02d}:{m:02d}" for h in range(25) for m in range(0, 60, 30)]

        # 시작 시간
        self.label5 = tk.Label(self.input_right_frame, text='시작 시간').grid(row=1, column=0, padx=5, pady=5, sticky='w')
        self.time_combobox1 = ttk.Combobox(self.input_right_frame, values=time_options, width=13)
        self.time_combobox1.grid(row=1, column=1, padx=5, pady=5)
        self.time_combobox1.bind("<<ComboboxSelected>>", self.on_two_combobox)

        # 종료 시간
        self.label6 = tk.Label(self.input_right_frame, text='종료 시간').grid(row=2, column=0, padx=5, pady=5, sticky='w')
        self.time_combobox2 = ttk.Combobox(self.input_right_frame, values=time_options, width=13)
        self.time_combobox2.grid(row=2, column=1, padx=5, pady=5)
        self.time_combobox2.bind("<<ComboboxSelected>>", self.on_two_combobox)

        # 총 초과 근무 시간
        self.var4 = tk.StringVar()
        self.label7 = tk.Label(self.input_right_frame, text='총 초과 근무 시간').grid(row=3, column=0, padx=5, pady=5)
        self.entry5 = tk.Entry(self.input_right_frame, textvariable=self.var4, width=15)
        self.entry5.grid(row=3, column=1, padx=5, pady=5)

        # 결재 신청 버튼
        self.fin_btn = tk.Button(self.input_right_frame, text='결재 신청', command=self.payment_btn)
        self.fin_btn.grid(row=4, column=1, padx=5, pady=5, sticky='E')

    def create_control_fields(self):
        # 왼쪽 입력 필드 (사원코드, 이름)
        tk.Label(self.control_frame, text="사원코드").grid(row=0, column=0, sticky="w", padx=5, pady=5)
        self.entry_code = tk.Entry(self.control_frame, width=20)
        self.entry_code.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(self.control_frame, text="이름").grid(row=1, column=0, sticky="w", padx=5, pady=5)
        self.entry_name = tk.Entry(self.control_frame, width=20)
        self.entry_name.grid(row=1, column=1, padx=5, pady=5)

        # 콤보박스 (부서, 직급)
        tk.Label(self.control_frame, text="부서").grid(row=2, column=0, sticky="w", padx=5, pady=5)
        self.combo_department = ttk.Combobox(self.control_frame, values=["인사부", "영업부", "기술부", "회계부"], state="readonly",
                                             width=18)
        self.combo_department.grid(row=2, column=1, padx=5, pady=5)
        self.combo_department.current(0)  # 기본값 설정

        tk.Label(self.control_frame, text="직급").grid(row=3, column=0, sticky="w", padx=5, pady=5)
        self.combo_position = ttk.Combobox(self.control_frame, values=["사원", "대리", "과장", "부장"], state="readonly",
                                           width=18)
        self.combo_position.grid(row=3, column=1, padx=5, pady=5)
        self.combo_position.current(0)  # 기본값 설정

        # 버튼
        button_frame = tk.Frame(self.control_frame)
        button_frame.grid(row=0, column=2, rowspan=4, padx=5, pady=5, sticky="e")

        tk.Button(button_frame, text="조회", width=10, command=self.search_attendance).pack(pady=3)
        tk.Button(button_frame, text="수정", width=10).pack(pady=3)
        tk.Button(button_frame, text="저장", width=10).pack(pady=3)

    # def create_output_fields(self):
    #     columns = ["사원코드", "사원명", "부서", "출근시간", "퇴근시간", "지각", "조퇴", "연장근무", "연차사용", "근태상태"]

    #     # 더미 데이터 (나중에 DB에서 불러오는 함수 `load_employee_data()`에서 업데이트 예정)
    #     dummy_data = [
    #         ["SCP-772", "박징징징", "인사부", "09:00", "17:50", "지각함 ㅋ", "조퇴마려움", "절대안하지", "연차쓰고감 ㅂㅂ", "자르죠?"]
    #     ]
    #     # TableWidget을 출력 화면에 배치
    #     self.table = tablewidget.TableWidget(
    #         self.output_frame,
    #         data=dummy_data,
    #         col_name=columns,
    #         width=1300,
    #         height=350
    #     )

    #     self.table.pack(x=0, y=0)

    # 조회 함수(클라이언트용)

    def search_attendance(self):
        search = {
            "employee_code": self.entry_code.get().strip(),
            "name": self.entry_name.get().strip(),
            "department": self.combo_department.get().strip()
        }

        self.var1.set(self.entry_code.get())  # 사원코드
        self.var2.set(self.entry_name.get())  # 이 름
        self.var3.set(self.combo_department.get())  # 부서
        print(search)

        data = {

            "code": 10601,

            "args": search

        }
        print(data)
        # data = self.f10601(**search)
        self.send_(data)  # 최종 전송
        self.recv(**data)

    # @staticmethod
    # # 서버용 조회 함수
    # def f10601(**kwargs):
    #     # dbm = dbManager.DBManager(host="192.168.0.29", user="root", password="0000", port=3306)
    #     base_query = "SELECT employee_code,name,department,'date',work_start_time,work_end_time,overtime,Approval_status,pay FROM overtime"
    #     valid_columns = {"employee_code", "name", "department", "'date'", "start_time", "end_time"}
    #
    #     valid_conditions = [
    #         f"COALESCE({key}, '') LIKE '%{value}%'"
    #         for key, value in kwargs.items()
    #         if key in valid_columns and value
    #     ]
    #
    #     query = base_query if not valid_conditions else f"{base_query} WHERE {' AND '.join(valid_conditions)}"
    #
    #     data = dbm.query(query) or []
    #
    #     # 전체 출력 조건 추가
    #     if not data:
    #         data = dbm.query(base_query) or []
    #
    #     formatted_data = [
    #         [str(item) if isinstance(item, datetime.date) else item for item in row]
    #         for row in data
    #     ]
    #
    #     return {"sign": 1, "data": formatted_data} if formatted_data else {"sign": 0, "data": "쿼리 실패"}

    def send_(self, some_dict):
        self.root.send_(json.dumps(some_dict, ensure_ascii=False))

    def after_init(self):
        pass

    # 조회
    def recv(self, **kwargs):
        code, sign, data = kwargs.get("code"), kwargs.get("sign"), kwargs.get("data")
        print("code:", kwargs.get("code"))
        print("sign:", kwargs.get("sign"))
        print("data:", kwargs.get("data"))

        if kwargs.get("code") == 10601:
            if kwargs.get("sign") == 1:
                self.table = tablewidget.TableWidget(
                    self.output_frame,
                    data=data,
                    col_name=["사원코드", "이름", "부서", "초과근무날짜", "시작일시", "종료일시", "초과시간", "승인여부", "수당지급"],
                    col_width=[150, 150, 150, 150, 150, 150, 150, 150, 150],
                    width=1300,
                    height=350
                )
                self.table.grid(row=0, column=0)
            else:
                msb.showerror("오류", "사원코드를 바르게 입력해주세요.")
        elif kwargs.get("code") == 10601 and kwargs.get("sign") == 1:
            self.table.refresh(kwargs.get("data"))

    # 결재 신청 관한 함수
    def payment_btn(self):

        employee_entry_data = {

            "사원명": self.var1.get(),
            "사원코드": self.var2.get(),
            "소속부서": self.var3.get(),
            "초과근무날짜": self.cal_overtime.get_date(),
            "시작시간": self.time_combobox1.get(),
            "종료시간": self.time_combobox2.get(),
            "총 초과 근무 시간": self.var4.get()  # 총 초과 근무 시간
        }

        if any(value == "" for value in employee_entry_data.values()):
            msb.showwarning("경고", "모든 칸을 입력해주세요.")
            return

        # data = {"code": 10602, "args": employee_entry_data}
        # self.root.send_(json.dumps(data, ensure_ascii=False))

        master = self.root.root
        if master.get_user_grade() in ["사장", "부장", "과장"]:
            msb.showinfo("알림", "대리 이하 직급에서 신청 가능합니다")
            return

        # 기존 딕셔너리에 데이터를 리스트 형태로 추가
        for key, value in employee_entry_data.items():
            self.info_dict[key].append(value)
            print(self.info_dict)

        msb.showinfo("성공", "초과 근무 신청이 정상적으로 저장되었습니다.")

        # data = {"code": 10601, "arges": self.info_dict}

        # # self.f10602(**data)
        # self.root.send_(json.dumps(data, ensure_ascii=False))

    # 수정할 코드드
    # @staticmethod
    # def f10602(**kwargs):
    #     dbm = dbManager.DBManager(host="192.168.0.13", user="root", password="0000", port=3306)
    #
    #     # 만약에 결재 신청을 누르면 사원코드 , 사원명, 부서 ,초과근무날짜 , 시작식나, 종료 시간에 대한 entry 값이
    #


if __name__ == "__main__":
    r = tk.Tk()
    r.geometry("1600x900")
    r.config(bg="white")
    app = OvertimeManagement(r)
    app.place(x=300, y=130)
    app.mainloop()
