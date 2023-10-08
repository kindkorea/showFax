# tkinter 패키지 import
import tkinter
from time import sleep

# Tk Class 선언으로 window 창 생성


image=tkinter.PhotoImage(file="user.png") #PhotoImage를 통한 이미지 지정





window = tkinter.Tk()

# 생성할 window 창의 크기 및 초기 위치 설정 매서드: geometry()
window_width = 1000
window_height = 800
window_pos_x = 700
window_pos_y = 100

window.geometry("{}x{}+{}+{}".format(window_width, window_height, window_pos_x, window_pos_y))

# 생성한 Window 창의 크기 조절 가능 여부 설정: resizable()
window.resizable(False, False)   # True, False 대신 1, 0을 사용할 수 있음

# 생성한 Window 창의 Title 설정: title()
window.title("Tkinter: Frame Test by Rosmary")

# 생성한 Window 창의 Icon 설정: iconphoto()
window.iconphoto(False, tkinter.PhotoImage(file="icon1.png"))

# tkinter.Frame 클래스 선언 및 Frame 위젯 생성
frame1 = tkinter.Frame(window, width = 800, height = 780, relief="solid", bd=2, bg="red")
frame2 = tkinter.Frame(window, width = 200, height = 80, relief="solid", bd=2, bg="blue")

# frame1의 label 위젯 생성, frame2의 entry 위젯 생성
label_id = tkinter.Label(frame1, text="아이디")
label_pw = tkinter.Label(frame1, text="비밀번호")
entry_id = tkinter.Entry(frame2, width=20)
entry_pw = tkinter.Entry(frame2, width=20)

# frame1.pack()
# frame2.pack(side="left")
# Frame 위젯 배치
frame1.place(x=10, y=10)
frame2.place(x=820, y=10)
label_id = label_id.place(x=0, y=0)
label_id = label_pw.place(x=0, y=40)
entry_id = entry_id.place(x=0, y=0)
entry_id = entry_pw.place(x=0, y=40)

# 생성한 window 창이 닫히지 않도록 유지
window.mainloop()