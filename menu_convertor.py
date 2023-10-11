import tkinter.ttk as ttk
import tkinter.messagebox as msgbox
from tkinter import * # __all__
import lib_modify_file  as modify_file
import datetime


class PDFconvert():

    def __init__(self, parent):
        # tkinter.Tk.__init__(self,parent)
        self.parent = parent
        self.frame = Frame(self.parent)
        self.initialize()
        self.src_file =''
        self.frame.pack(side='top')

    def initialize(self):

        # 로드 경로 프레임
        self.src_path_frame = LabelFrame(self.frame, text="로드경로")
        self.src_path_frame.pack(fill="x", padx=5, pady=5, ipady=5)

        self.txt_src_path = Entry(self.src_path_frame)
        self.txt_src_path.pack(side="left", fill="x", expand=True, padx=5, pady=5, ipady=4) # 높이 변경
        self.txt_src_path.insert(END,"C:/Users/kindk/Downloads")

        self.btn_src_path = Button(self.src_path_frame, text="찾아보기", width=10)
        self.btn_src_path.pack(side="right", padx=5, pady=5)

        # 저장 경로 프레임


        self.path_frame = LabelFrame(self.frame, text="저장경로")
        self.path_frame.pack(fill="x", padx=5, pady=5, ipady=5)

        self.txt_dest_path = Entry(self.path_frame)
        self.txt_dest_path.pack(side="left", fill="x", expand=True, padx=5, pady=5, ipady=4) # 높이 변경
        self.txt_dest_path.insert(END,"C:/Users/kindk/Desktop")

        self.btn_dest_path = Button(self.path_frame, text="찾아보기", width=10 )
        self.btn_dest_path.pack(side="right", padx=5, pady=5)

        
        self.frame_run = Frame(self.frame)
        self.frame_run.pack(fill="x", padx=5, pady=5)

        self.btn_convert_jpg = Button(self.frame_run, padx=5, pady=5, text="JPG변환", width=12, command=self.cmd_pdf_to_jpg)
        self.btn_convert_jpg.pack(side="right", padx=5, pady=5)

        self.btn_rename = Button(self.frame_run, padx=5, pady=5, text="이름변경", width=12, command=self.cmd_rename)
        self.btn_rename.pack(side="right", padx=5, pady=5)


        self.month = datetime.datetime.now().month
        self.make_mid_content = Entry(self.frame_run)
        self.make_mid_content.pack(side="left", fill="x", expand=True, padx=5, pady=5, ipady=4) # 높이 변경
        self.make_mid_content.insert(END,f"{self.month}월 청구서")

        self.make_comp_name = Entry(self.frame_run)
        self.make_comp_name.pack(side="left", fill="x", expand=True, padx=5, pady=5, ipady=4) # 높이 변경
        self.make_comp_name.insert(END,f"업체명")

        # 진행 상황 Progress Bar
        self.frame_progress = LabelFrame(self.frame, text="진행상황")
        self.frame_progress.pack(fill="x", padx=5, pady=5, ipady=5)

        self.p_var = DoubleVar()
        self.progress_bar = ttk.Progressbar(self.frame_progress, maximum=100, variable=self.p_var)
        self.progress_bar.pack(fill="x", padx=5, pady=5)


        # 하단 닫기 버튼

        self.frame_run = Frame(self.frame)
        self.frame_run.pack(fill="x", padx=5, pady=5)

        self.btn_close = Button(self.frame_run, padx=5, pady=5, text="닫기", width=12, command=self.parent.quit)
        self.btn_close.pack(side="right", padx=5, pady=5)

    def cmd_pdf_to_jpg(self):
        if self.make_comp_name.get() == '업체명' :
            msgbox.showwarning('경고','업체명을 입력하세요')
        else :

            pdf_file = modify_file.Modify_file(self.txt_src_path.get())
            f_name = f'웅천목재_{self.make_mid_content.get()}_{self.make_comp_name.get()}'
            
            if not pdf_file.pdf_to_jpg(self.txt_dest_path.get(),f_name) :
                msgbox.showwarning('경고','PDF 파일이 없습니다.')
            
            self.make_comp_name.delete(0,'end')
            self.make_comp_name.insert(END,"업체명")
            # modify_file.convert_jpg(txt_src_path.get(),txt_dest_path.get(),f_name)
            # progress_bar.update()

    def cmd_rename(self):
        if self.make_comp_name.get() != '업체명' :
            pdf_file = modify_file.Modify_file(self.txt_src_path.get())

            f_name = f'웅천목재_{self.make_mid_content.get()}_{self.make_comp_name.get()}'
            # result = pdf_file.pdf_rename(txt_dest_path.get(),f_name)

            if not pdf_file.pdf_rename(self.txt_dest_path.get(),f_name) :
                msgbox.showwarning('경고','PDF 파일이 없습니다.')

            self.make_comp_name.delete(0,'end')
            self.make_comp_name.insert(END,"업체명")

        else :
            # print("업체명을 입력하세요.")
            msgbox.showwarning('경고','업체명을 입력하세요')

        # f_name = f'웅천목재_{make_mid_content.get()}_{make_comp_name.get()}'
        # modify_file.re_name(txt_src_path.get(),txt_dest_path.get(),f_name)
        # progress_bar.update()




# root = Tk()

# app = PDFconvert(root)
# root.title("OC PROGRAMS")
# # root.ttk.call('wm','./icon.png')
# # icon = PhotoImage(file='./icon.png ')
# # root.wm_iconphoto(False, icon)


# root.resizable(False, False)
# root.mainloop()



