import tkinter.ttk as ttk
import tkinter.messagebox as msgbox
from tkinter import * # __all__
import modify_file
import datetime

root = Tk()
root.title("OC PROGRAMS")
# root.ttk.call('wm','./icon.png')
# icon = PhotoImage(file='./icon.png ')
# root.wm_iconphoto(False, icon)

# 로드 경로 프레임
src_path_frame = LabelFrame(root, text="로드경로")
src_path_frame.pack(fill="x", padx=5, pady=5, ipady=5)

txt_src_path = Entry(src_path_frame)
txt_src_path.pack(side="left", fill="x", expand=True, padx=5, pady=5, ipady=4) # 높이 변경
txt_src_path.insert(END,"C:/Users/kindk/Downloads")

btn_src_path = Button(src_path_frame, text="찾아보기", width=10)
btn_src_path.pack(side="right", padx=5, pady=5)

# 저장 경로 프레임


path_frame = LabelFrame(root, text="저장경로")
path_frame.pack(fill="x", padx=5, pady=5, ipady=5)

txt_dest_path = Entry(path_frame)
txt_dest_path.pack(side="left", fill="x", expand=True, padx=5, pady=5, ipady=4) # 높이 변경
txt_dest_path.insert(END,"C:/Users/kindk/Desktop")

btn_dest_path = Button(path_frame, text="찾아보기", width=10 )
btn_dest_path.pack(side="right", padx=5, pady=5)

def cmd_pdf_to_jpg():
    if make_comp_name.get() == '업체명' :
        msgbox.showwarning('경고','업체명을 입력하세요')
    else :

        pdf_file = modify_file.Modify_file(txt_src_path.get())
        f_name = f'웅천목재_{make_mid_content.get()}_{make_comp_name.get()}'
        
        if not pdf_file.pdf_to_jpg(txt_dest_path.get(),f_name) :
            msgbox.showwarning('경고','PDF 파일이 없습니다.')
        
        make_comp_name.delete(0,'end')
        make_comp_name.insert(END,"업체명")
        # modify_file.convert_jpg(txt_src_path.get(),txt_dest_path.get(),f_name)
        # progress_bar.update()

def cmd_rename():
    if make_comp_name.get() != '업체명' :
        pdf_file = modify_file.Modify_file(txt_src_path.get())

        f_name = f'웅천목재_{make_mid_content.get()}_{make_comp_name.get()}'
        # result = pdf_file.pdf_rename(txt_dest_path.get(),f_name)

        if not pdf_file.pdf_rename(txt_dest_path.get(),f_name) :
            msgbox.showwarning('경고','PDF 파일이 없습니다.')

        make_comp_name.delete(0,'end')
        make_comp_name.insert(END,"업체명")

    else :
        # print("업체명을 입력하세요.")
        msgbox.showwarning('경고','업체명을 입력하세요')

    # f_name = f'웅천목재_{make_mid_content.get()}_{make_comp_name.get()}'
    # modify_file.re_name(txt_src_path.get(),txt_dest_path.get(),f_name)
    # progress_bar.update()



frame_run = Frame(root)
frame_run.pack(fill="x", padx=5, pady=5)

btn_convert_jpg = Button(frame_run, padx=5, pady=5, text="JPG변환", width=12, command=cmd_pdf_to_jpg)
btn_convert_jpg.pack(side="right", padx=5, pady=5)

btn_rename = Button(frame_run, padx=5, pady=5, text="이름변경", width=12, command=cmd_rename)
btn_rename.pack(side="right", padx=5, pady=5)


month = datetime.datetime.now().month
make_mid_content = Entry(frame_run)
make_mid_content.pack(side="left", fill="x", expand=True, padx=5, pady=5, ipady=4) # 높이 변경
make_mid_content.insert(END,f"{month}월 청구서")

make_comp_name = Entry(frame_run)
make_comp_name.pack(side="left", fill="x", expand=True, padx=5, pady=5, ipady=4) # 높이 변경
make_comp_name.insert(END,f"업체명")

# 진행 상황 Progress Bar
frame_progress = LabelFrame(root, text="진행상황")
frame_progress.pack(fill="x", padx=5, pady=5, ipady=5)

p_var = DoubleVar()
progress_bar = ttk.Progressbar(frame_progress, maximum=100, variable=p_var)
progress_bar.pack(fill="x", padx=5, pady=5)


# 하단 닫기 버튼

frame_run = Frame(root)
frame_run.pack(fill="x", padx=5, pady=5)

btn_close = Button(frame_run, padx=5, pady=5, text="닫기", width=12, command=root.quit)
btn_close.pack(side="right", padx=5, pady=5)


root.resizable(False, False)
root.mainloop()



