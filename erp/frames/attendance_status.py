import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar
import locale
import tablewidget
from tkinter import *
import tkinter.messagebox as msb
from PIL import Image, ImageTk
from tkcalendar import DateEntry
# import mysql.connector
# import dbManager
import json
from datetime import datetime


class AttendanceStatus(tk.Frame):
    def __init__(self, root):
        super().__init__(root, width=1300, height=700)
        locale.setlocale(locale.LC_TIME, 'ko_KR')

        self.root = root

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

    def create_input_fields(self):
        # 캘린더 프레임
        self.Calendar_frame = tk.LabelFrame(self)
        self.Calendar_frame.place(x=0, y=30, width=950, height=350)
        self.cal = Calendar(self.Calendar_frame,
                            selectmode='day',
                            background='white',
                            foreground='black',
                            headersbackground='#ADD8E6',
                            normalforeground='black',
                            weekendbackground='#BDCDD6',
                            weekendforground='black',
                            othermonthforeground='gray50',
                            othermonthbackground='white',
                            othermonthweforeground='gray50',
                            othermonthwebackground='#EEE9DA')

        self.cal.pack(fill="both", expand=True, pady=20)

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
        self.combo_department = ttk.Combobox(self.control_frame, values=["인사부", "영업부", "기술부"], state="readonly",
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
    #         ["SCP-772", "박o환", "인사부", "09:00", "17:50", "응 맨날 지각ㅋㅋ", "조퇴마려움", "절대안하지", "연차쓰고감 ㅂㅂ", "이미 권고사직 처리 할까 생각중임"]
    #     ]

    #     # TableWidget을 출력 화면에 배치
    #     self.table = tablewidget.TableWidget(
    #         self.output_frame,
    #         data=dummy_data,
    #         col_name=columns,
    #         width=1300,
    #         height=350
    #     )

    # self.table.pack()

    # 조회 함수(클라이언트용)
    def search_attendance(self):
        self.search = {
            "사원 코드": self.entry_code.get(),  # 사원 코드
            "이 름": self.entry_name.get(),  # 이 름
            "부  서": self.combo_department.get(),  # 부 서
            "직 급": self.combo_position.get()  # 직 급
        }

        data = {"code": 10501, "args": self.search}

        # self.f10501(**data)

        self.root.send_(json.dumps(data, ensure_ascii=False))

    # @staticmethod
    # # 서버용 조회 함수
    # def f10501(**kwargs):
    #     # dbm = dbManager.DBManager(host="192.168.0.29", user="root", password="0000", port=3306)
    #
    #     base_query = """
    #     SELECT e.employee_code, e.name, e.department, a.work_start_time, a.work_end_time, a.late,
    #            a.early_leave, a.overtime, a.leave_used, a.attendance_status
    #            FROM erp_db.employee e
    #           LEFT JOIN erp_db.attendance a ON e.employee_code = a.employee_code
    #       """
    #
    #     # 조건으로 사용할 유효한 컬럼 목록
    #     valid_columns = {"employee_code", "name", "department"}
    #
    #     # 조건이 있는 경우 WHERE 절 추가
    #     valid_conditions = [f"{key} LIKE '%%{value}%%'" for key, value in kwargs.items()
    #                         if key in valid_columns and value]
    #
    #     # 조건이 없으면 전체 조회, 조건이 있으면 필터링 조회
    #     query = base_query if not valid_conditions else f"{base_query} WHERE {' AND '.join(valid_conditions)}"
    #
    #     data = dbm.query(query) or []
    #
    #     if not data:
    #         return {"sign": 0, "data": "조회 결과 없음"}
    #
    #     # 날짜 데이터를 문자열로 변환
    #     formatted_data = [
    #         [str(item) if isinstance(item, (datetime.date, datetime.time, datetime.timedelta)) else item for item in
    #          row]
    #         for row in data
    #     ]
    #
    #     if not formatted_data:
    #         return {"sign": 0, "data": "포맷팅된 데이터 없음"}
    #
    #     else:
    #         return {"sign": 1, "data": formatted_data}

    def recv(self, **kwargs):
        code, sign, data = kwargs.get("code"), kwargs.get("sign"), kwargs.get("data")
        print("code:", kwargs.get("code"))
        print("sign:", kwargs.get("sign"))
        print("data:", kwargs.get("data"))

        if kwargs.get("code") == 10501:
            if kwargs.get("sign") == 1:
                self.table = tablewidget.TableWidget(
                    self.output_frame,
                    data=data,
                    col_name=["사원코드", "사원명", "부서", "출근시간", "퇴근시간", "지각", "조퇴", "연장근무", "연차사용", "근태상태태"],
                    col_width=[150, 150, 150, 150, 150, 150, 150, 150, 150],
                    width=1300,
                    height=350
                )
                self.table.grid(row=0, column=0)
            else:
                msb.showerror("오류", "사원코드를 바르게 입력해주세요.")
        elif kwargs.get("code") == 10501 and kwargs.get("sign") == 1:
            self.table.refresh(kwargs.get("data"))


if __name__ == "__main__":
    r = tk.Tk()
    r.geometry("1600x900")
    r.config(bg="white")
    app = AttendanceStatus(r)
    app.place(x=300, y=130)
    app.mainloop()