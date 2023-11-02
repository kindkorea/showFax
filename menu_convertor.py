import tkinter.ttk as ttk
import tkinter.messagebox as msgbox
from tkinter import * # __all__
import lib_modify_file  as modify_file
import datetime
from io import BytesIO
from PIL import Image
import win32clipboard
import time 
import os

class CB_button:
    def __init__(self, frame, cb_label, number):
        self.__dst_file = ''
        self.number = number+1
        self.frame = frame
        self.cb_label = cb_label
      
        self.btn = Button(self.frame, padx=10, text=f'CB_{self.number}', command = self.send_to_clipboard)
        # self.label = Label(self.cb_label, textvariable=self.cb_copied, fg='red')
        self.btn.grid(row=1 , column=self.number)
        # self.label.grid(row=2,column=0)
       


    def change_bg_color(self, color):
        self.btn.configure(bg=color)
        
    @property
    def filename(self):
        return self.__dst_file
    
    @filename.setter
    def filename(self,filename):
        self.__dst_file = filename

    

    def send_to_clipboard(self):
        if not self.__dst_file:
            self.cb_label.set(f"There is no file")
        else : 
            file_name = os.path.basename(self.__dst_file)
            image = Image.open(self.__dst_file)
            output = BytesIO()
            image.convert("RGB").save(output, "BMP")
            data = output.getvalue()[14:]
            output.close()
            win32clipboard.OpenClipboard()
            win32clipboard.EmptyClipboard()
            win32clipboard.SetClipboardData(win32clipboard.CF_DIB, data)
            win32clipboard.CloseClipboard()    
            self.cb_label.set(f"{file_name} copied!!")
            



class PDFconvert():

    def __init__(self, parent):
        # tkinter.Tk.__init__(self,parent)
        self.NUMBER_OF_CB = 8
     
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
        self.btn_convert_jpg = Button(self.frame_run, padx=5, pady=5, text="JPG변환", width=12, command=self.cmd_pdf_to_jpg)
        self.btn_convert_jpg.pack(side="right", padx=5, pady=5)

        self.btn_rename = Button(self.frame_run, padx=5, pady=5, text="이름변경", width=12, command=self.cmd_rename)
        self.btn_rename.pack(side="right", padx=5, pady=5)


        # self.frame_run = Frame(self.frame)
        # self.frame_run.pack(fill="x", padx=5, pady=5)

        self.month = datetime.datetime.now().month
        self.make_mid_content = Entry(self.frame_run)
        self.make_mid_content.pack(side="left", fill="x", expand=True, padx=5, pady=5, ipady=4) # 높이 변경
        self.make_mid_content.insert(END,f"{self.month}월 청구서")

        self.make_comp_name = Entry(self.frame_run)
        self.make_comp_name.pack(side="left", fill="x", expand=True, padx=5, pady=5, ipady=4) # 높이 변경
        self.make_comp_name.insert(END,f"업체명")
        self.frame_run.pack(fill="x", padx=5, pady=5)

        
        # 진행 상황 Progress Bar
        self.frame_cb = LabelFrame(self.frame, text="Copy to Clipboard")
        self.cb_label_frame = Frame(self.frame)
        self.cb_label_text = StringVar()
        self.cb_label = Label(self.cb_label_frame, textvariable=self.cb_label_text, fg='red')
        self.btn_list = []

        for i in  range(self.NUMBER_OF_CB):
            btn = CB_button(self.frame_cb,self.cb_label_text,i)
            self.btn_list.append(btn)
            
        # self.cb_label.grid(row=2,column=0)
        self.frame_cb.pack(fill="x", padx=5, pady=5, ipady=5)
        self.cb_label.pack()
        self.cb_label_frame.pack()



    

    def cmd_pdf_to_jpg(self):
        if self.make_comp_name.get() == '업체명' :
            msgbox.showwarning('경고','업체명을 입력하세요')
        else :
            pdf_file = modify_file.Modify_file(self.txt_src_path.get())
            f_name = f'웅천목재_{self.make_mid_content.get()}_{self.make_comp_name.get()}'
            
            filename_jpg = pdf_file.pdf_to_jpg(self.txt_dest_path.get(),f_name)
            # time.sleep(1)
            
            # self.send_to_clipboard(filename_jpg[0])
            # print(f'{filename_jpg=}')
            for i in range(self.NUMBER_OF_CB):
                if len(filename_jpg) <= i :
                    self.btn_list[i].change_bg_color("#f0f0f0")
                    self.btn_list[i].filename = ''
                else : 
                    self.btn_list[i].change_bg_color("red")
                    self.btn_list[i].filename = filename_jpg[i]
                    


            if not  filename_jpg:
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

    

    

