import tkinter as tk
import tkinter.ttk as ttk
from tkinter import Button, Entry, Label, messagebox


## 기본설정
win = tk.Tk()
win.rowconfigure(0, weight = 1)
win.columnconfigure(0, weight = 1)
balance = 100000
print_message = "       " + "잔액: " + str(balance) + " 원" + "       "

background_image = tk.PhotoImage(file="background.png")
logo_image = tk.PhotoImage(file="logo.png")
small_logo = tk.PhotoImage(file="small_logo.png")
card_image = tk.PhotoImage(file="card.png")

id_list = []
pw_list = []

T = False

# 프레임 전환
def change_frame(frame):
    frame.tkraise()

#로그인
def login():
    my_id = L_id_entry.get()
    my_pw = L_pw_entry.get()
    if my_id in id_list:
        id_list_num = id_list.index(my_id)
    else:
        messagebox.showinfo("알림", "등록된 아이디가 없습니다!")    
    if my_pw in pw_list:
        pw_list_num = pw_list.index(my_pw)
        if id_list_num == pw_list_num:
            change_frame(bank_frame)
    else:
        messagebox.showinfo("알림", "비밀번호가 다릅니다!")

# 아이디 확인
def check_id():
    join_id = J_id_entry.get()
    if join_id in id_list:
        messagebox.showinfo("알림", "중복된 아이디가 이미 존재합니다!")
    else:
        global T
        T = True
        messagebox.showinfo("알림", "아이디 사용이 가능합니다!")
   
# 라벨 삭제
def del_lab():
    H_balance_lab.destroy()
    S_balance_lab.destroy()

# 라벨 다시 만들기
def redraw():
    n_print_message = "       " + "잔액: " + str(balance) + " 원" + "       "
    n_balance_lab = Label(bank_frame, text = n_print_message, font = ("맑은고딕", 30), bg = "#FFFFCC")
    n_balance_lab.place(x = 20,  y = 80)
    n_send_balance_lab = Label(send_frame, text = n_print_message, font = ("맑은고딕", 30), bg = "#FFFFCC")
    n_send_balance_lab.place(x = 20,  y = 120)

# 회원가입
def join():
    if T == True:
        join_id = J_id_entry.get()
        join_pw = J_pw_entry.get()
        check_pw = J_check_pw_entry.get()
        if join_pw == check_pw:
            id_list.append(join_id)
            pw_list.append(join_pw)
            change_frame(start_frame)
            messagebox.showinfo("알림", "완료! 로그인을 해주세요.")
        else:
            messagebox.showinfo("알림", "비밀번호가 다릅니다!")
    elif T == False:
        messagebox.showinfo("알림", "ID 중복체크를 해주세요!")
# 송금
def send():
    send_number = send_entry.get()
    account_number = account_entry.get()
    bank_number = combobox.get()
    if bank_number == "--은행을 선택하세요--":
        messagebox.showinfo("알림", "은행을 선택하세요.")
    if account_number == "":
        messagebox.showinfo("알림", "계좌번호를 입력하세요.")
    if send_number == "" or int(send_number) <= 0:
        messagebox.showinfo("알림", "송금할 금액을 정확히 입력하세요.")

    if bank_number != "--은행을 선택하세요--" and account_number != "" and send_number != "":
        global balance
        if balance >= int(send_number) >0:
            balance = balance - int(send_number)
            del_lab()
            redraw()
            change_frame(bank_frame)
            messagebox.showinfo("알림", "송금완료했습니다.")    
            
        elif balance <= int(send_number):
            messagebox.showinfo("알림", "잔액이 부족합니다.")
            change_frame(send_frame)


# 프레임 설정
start_frame = tk.Frame(win)
join_frame = tk.Frame(win)
bank_frame = tk.Frame(win)
send_frame = tk.Frame(win)
for frame in (start_frame, join_frame, bank_frame, send_frame):
    frame.grid(row = 0, column = 0, sticky = "nsew")

### 로그인 페이지
class Login:
    def __init__(self, name, type, frame, text, image, font, bg, config_btn, width, height, x, y):
        self.name = name
        self.type = type
        self.frame = frame
        self.text = text
        self.image = image
        self.font = font
        self.bg = bg
        self.config_btn = config_btn
        self.width = width
        self.height = height
        self.x = x
        self.y = y
    
    def show_up(self):
        self.name = self.type(self.frame, text = self.text, image = self.image, font = self.font, bg = self.bg, width = self.width, height = self.height)
        self.name.place(x = self.x, y = self.y)
        self.name.config(command = self.config_btn)

main_image = Login("main_image", Label, start_frame, None, background_image, None, None, None, None, None, 0, 0)
head_logo_image = Login("head_logo_image", Label, start_frame, None, logo_image, None, None, None, None, None, 160, 0)
id_label = Login("id_label", Label, start_frame, "ID", None, ("굴림", 20), "#cef4e6", None, None, None, 90, 120)
pw_label = Login("pw_label", Label, start_frame, "password", None, ("굴림", 20), "#cef4e6", None, None, None, 0, 150)
login_btn = Login("login_btn", Button, start_frame, "로그인", None, None, "#CCCCFF", login, 10, 4, 270, 200)
join_btn = Login("join_btn", Button, start_frame, "회원가입", None, None, "#CCCCFF", lambda: change_frame(join_frame), 10, 4, 180, 200)

main_image.show_up()
head_logo_image.show_up()
head_logo_image.show_up()
id_label.show_up()
pw_label.show_up()
login_btn.show_up()
join_btn.show_up()

L_id_entry = tk.Entry(start_frame, width = 30)
L_pw_entry = tk.Entry(start_frame, width = 30)
L_id_entry.place(x = 150, y = 130)
L_pw_entry.place(x = 150, y = 160)


### 회원가입 페이지
class Join:
    def __init__(self, name, type, frame, text, image, font, bg, config_btn, width, height, x, y):
        self.name = name
        self.type = type
        self.frame = frame
        self.text = text
        self.image = image
        self.font = font
        self.bg = bg
        self.config_btn = config_btn
        self.width = width
        self.height = height
        self.x = x
        self.y = y
    
    def show_up(self):
        self.name = self.type(self.frame, text = self.text, image = self.image, font = self.font, bg = self.bg, width = self.width, height = self.height)
        self.name.place(x = self.x, y = self.y)
        self.name.config(command = self.config_btn)

main_image = Join("main_image", Label, join_frame, None, background_image, None, None, None, None, None, 0, 0)
join_message = Join("join_message", Label, join_frame, "회원가입할 아이디와 비밀번호를 입력해주세요!", None, ("굴림", 15), "#FFFFCC", None, None, None, 30, 50)
join_label = Join("join_label", Label, join_frame, "ID", None, ("굴림", 20), "#cef4e6", None, None, None, 90, 100)
pw_label = Join("pw_label", Label, join_frame, "password", None, ("굴림", 20), "#c9f3e9", None, None, None, 0, 150)
check_id_btn = Join("check_id_btn", Button, join_frame, "ID중복 확인", None, ("굴림 12"), "#CCCCFF", check_id, None, None, 390, 110)
finish_join_btn = Join("finish_join_btn", Button, join_frame, "회원가입", None, ("굴림 10"), "#CCCCFF", join, 10, 3, 280, 230)
come_back_btn = Join("come_back_btn", Button, join_frame, "로그인화면으로 돌아가기", None, ("굴림 10"), "#CCCCFF", lambda: change_frame(start_frame), 20, 3, 100, 230)

main_image.show_up()
join_message.show_up()
join_label.show_up()
pw_label.show_up()
come_back_btn.show_up()
check_id_btn.show_up()
finish_join_btn.show_up()

J_id_entry = Entry(join_frame, width = 30)
J_pw_entry = Entry(join_frame, width = 30)
J_check_pw_entry = Entry(join_frame, width = 30)
J_id_entry.place(x = 150, y = 110)
J_pw_entry.place(x = 150, y = 160)
J_check_pw_entry.place(x = 150, y = 190)

### 은행 홈화면
class Home:
    def __init__(self, name, type, frame, text, image, font, bg, config_btn, width, height, x, y):
        self.name = name
        self.type = type
        self.frame = frame
        self.text = text
        self.image = image
        self.font = font
        self.bg = bg
        self.config_btn = config_btn
        self.width = width
        self.height = height
        self.x = x
        self.y = y
    
    def show_up(self):
        self.name = self.type(self.frame, text = self.text, image = self.image, font = self.font, bg = self.bg, width = self.width, height = self.height)
        self.name.place(x = self.x, y = self.y)
        self.name.config(command = self.config_btn)

main_image = Home("main_image",Label, bank_frame, None, background_image, None, None, None, None, None, 0, 0)
s_logo = Home("s_logo", Label, bank_frame, None, small_logo, None, None,  None, None, None, 200, 0)
bank_account = Home("bank_account", Label, bank_frame, "MY 계좌번호: 123456789", None, ("굴림", 10), "#FFCCCC", None, None, None, 20, 60)
card = Home("card", Label, bank_frame, None, card_image, None, None, None, None, None, 80, 140)
send_btn = Home("send_btn", Button, bank_frame, "송금하기", None, ("굴림"), "#CCCCFF", lambda: change_frame(send_frame), 8, 2, 280, 380)
log_out_btn = Home("send_btn", Button, bank_frame, "로그아웃", None, ("굴림"), "#CCCCFF", lambda: change_frame(start_frame), 8, 2, 130, 380)

main_image.show_up()
s_logo.show_up()
bank_account.show_up()
card.show_up()
send_btn.show_up()
log_out_btn.show_up()

H_balance_lab = Label(bank_frame, text = print_message, font = ("굴림", 30), bg = "#FFFFCC")
H_balance_lab.place(x = 10,  y = 80)

### 송금화면
class Send:
    def __init__(self, name, type, frame, text, image, font, bg, config_btn, width, height, x, y):
        self.name = name
        self.type = type
        self.frame = frame
        self.text = text
        self.image = image
        self.font = font
        self.bg = bg
        self.config_btn = config_btn
        self.width = width
        self.height = height
        self.x = x
        self.y = y
    
    def show_up(self):
        self.name = self.type(self.frame, text = self.text, image = self.image, font = self.font, bg = self.bg, width = self.width, height = self.height)
        self.name.place(x = self.x, y = self.y)
        self.name.config(command = self.config_btn)

banks = ["--은행을 선택하세요--","농협", "국민은행", "신한은행", "우리은행", "하나은행", "기업은행"]

main_image = Send("main_image", Label, send_frame, None, background_image, None, None,  None, None, None, 0, 0)
head_logo_image = Send("head_logo_image", Label, send_frame, None, logo_image, None, None, None, None, None, 160, 0)
bank = Send("bank", Label, send_frame, "송금할 은행을 선택하세요.", None, ("굴림", 10), "#c8f2ea", None, None, None, 0, 180)
account = Send("account", Label, send_frame, "계좌번호를 입력하세요.", None, ("굴림", 10), "#c4f1eb", None, None, None, 0, 210)
send_blank = Send("send_blank", Label, send_frame, "송금할 금액을 입력해주세요.", None, ("굴림", 10), "#c2f1ed", None, None, None, 0, 240)
money_send_btn = Send("money_send_btn", Button, send_frame, "송금하기", None, ("굴림"), "#CCCCFF", send, 8, 3, 210, 290)
come_home_btn = Send("come_home_btn", Button, send_frame, "<--", None, None, "#CCCCFF", lambda: change_frame(bank_frame), 4, 2, 10, 10)

main_image.show_up()
head_logo_image.show_up()
bank.show_up()
account.show_up()
send_blank.show_up()
money_send_btn.show_up()
come_home_btn.show_up()

S_balance_lab = Label(send_frame, text = print_message, font = ("굴림", 30), bg = "#FFFFCC")
combobox = ttk.Combobox(send_frame, height = 5, values = banks, state = "readonly")
combobox.current(0)
account_entry = Entry(send_frame, width = 23)
send_entry = Entry(send_frame, width = 23)
combobox.place(x = 180,  y = 180)
account_entry.place(x = 180, y = 210)
send_entry.place(x = 180, y = 240)
S_balance_lab.place(x = 10,  y = 120)

change_frame(start_frame)

win.title("MS BANk")
win.geometry("500x550")
win.resizable(False, False)
win.mainloop()