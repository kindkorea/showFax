import tkinter
import os
import glob
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class Target:
    DIRECTORY_WATCH = 'c:/Users/kindk/VsCode/showFax/img/'
    #watchDir에 감시하려는 디렉토리를 명시한다.

    def __init__(self):
        self.observer = Observer()   #observer객체를 만듦

    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.DIRECTORY_WATCH, 
                                                       recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(1)
        except:
            self.observer.stop()
            print("Error")
            self.observer.join()

class Handler(FileSystemEventHandler):
#FileSystemEventHandler 클래스를 상속받음.
#아래 핸들러들을 오버라이드 함

    #파일, 디렉터리가 move 되거나 rename 되면 실행
    def on_moved(self, event):
        print(event)

    def on_created(self, event): #파일, 디렉터리가 생성되면 실행
        print(event)

    def on_deleted(self, event): #파일, 디렉터리가 삭제되면 실행
        print(event)

    def on_modified(self, event): #파일, 디렉터리가 수정되면 실행
        print(event)

# if __name__ == ‘__main__’: #본 파일에서 실행될 때만 실행되도록 함





# w = Target()

# window.mainloop()
# w.run()



class MenuFax(tkinter.Tk):

    def __init__(self, parent):
        tkinter.Tk.__init__(self,parent)
        self.parent = parent
        self.initialize()
        self.src_file =''

    def initialize(self):
            
        # self.window=tkinter.Tk()
        # 윈도우창 설정
        self.title("YUN DAE HEE")
        self.geometry("640x400+100+100")
        self.resizable(False, False)

        # 프레임 1
        self.frame=tkinter.Frame(self, 
                            width=300,
                            )
        # 파일 리스트 박스 
        self.scrollbar=tkinter.Scrollbar(self.frame)
        self.scrollbar.pack(side="right", fill="y")


        self.listbox=tkinter.Listbox(self.frame, 
                                yscrollcommand = self.scrollbar.set,
                                # listvariable=var,
                                width=100,
                                )

        self.listbox.pack(side="left")

        #원클릭 이벤트 설정
        self.listbox.bind('<<ListboxSelect>>', self.items_selected)
        #더블클릭 이벤트 설정
        self.listbox.bind('<Double-Button-1>', self.items_doubleClicked)

        self.scrollbar["command"]=self.listbox.yview
        self.chk_active = tkinter.IntVar()


        # 프레임 2
        self.frame2 =tkinter.Frame(self, 
                            width=300,
                            )

        self.btn_all_files = tkinter.Button(self.frame2, text='모든파일' ,command=self.all_files)
        self.btn_noCheck_files = tkinter.Button(self.frame2, text='미확인파일', command=self.noCheck_files)
        self.btn_Checked_files = tkinter.Button(self.frame2, text='확인파일', command=self.checked_files)


        self.frame3 =tkinter.Frame(self, 
                            width=300,
                            )


        self.chk_button = tkinter.Checkbutton(self.frame3,text='확인' , variable=self.chk_active)
        self.btn_convert = tkinter.Button(self.frame3,text='이름바꾸기', command=self.convert_filename)
        self.company_name = tkinter.Entry(self.frame3)


        self.company_name.grid(row=0, column=0)
        self.chk_button.grid(row=0, column=1)
        self.btn_convert.grid(row=0, column=2)

        self.btn_all_files.grid(row=0, column=0)
        self.btn_noCheck_files.grid(row=0, column=1)
        self.btn_Checked_files.grid(row=0, column=2)
        # chk_button.select()

        self.frame.pack()
        self.frame2.pack()
        self.frame3.pack()
        self.noCheck_files()

    # print(f'{chk_active.get()}')
        
    def reload_file(self,filename):
        self.company_name.delete(0,'end')
        self.company_name.insert(0,filename.split('_')[0])  
        if filename[0] == 'v' :
            self.chk_active.set(True)
            # return True
        else :
            self.chk_active.set(False)
            # return False

    def items_selected(self,event):
        selected_indices = self.listbox.curselection()
        self.src_file = self.listbox.get(selected_indices[0])
        self.reload_file(os.path.basename(self.src_file))

    def items_doubleClicked(self,event):
        selected_indices = self.listbox.curselection()
        msg = self.listbox.get(selected_indices[0])
        os.system(f'./img/{msg}')



    def FAX_rename(self, src_file ,dst_file, is_checked) :
            try :
                #파일 생성일자를 업체명 뒤에 붙임
                creation_time = time.gmtime(os.path.getctime(src_file))
                file_ctime = time.strftime("%Y_%m_%d", creation_time)

                #소스 파일을 파일, 확장자로 쪼갬
                file_path, file_name_ext = os.path.split(src_file)
                file_name , file_ext = os.path.splitext(file_name_ext)

                #새로 변경할 파일명을 조립함
                try :
                    dst_file_name = f'{file_path}/{dst_file}_{file_ctime}{file_ext}'
                    os.rename(src_file,dst_file_name)
                except FileExistsError :
                    print(f'{dst_file_name} is exited')
            except FileNotFoundError :
                print(f'{src_file} is not found')

    def get_file(self):
        src_path = './img'
        load_files = glob.glob(src_path+'/*.*')
        return  [file for file in load_files if file.endswith('.jpg')]

    def all_files(self):
        self.listbox['listvariable'] = tkinter.Variable(value=self.get_file())

    def noCheck_files(self):
        noChk_file_list = [file for file in self.get_file() if os.path.basename(file)[0] != 'v']
        self.listbox['listvariable'] = tkinter.Variable(value=noChk_file_list)

    def checked_files(self):
        noChk_file_list = [file for file in self.get_file() if os.path.basename(file)[0] == 'v']
        self.listbox['listvariable'] = tkinter.Variable(value=noChk_file_list)

    def convert_filename(self):
        self.FAX_rename(self.src_file, self.company_name.get(), self.chk_active.get())
        # print(f'{self.src_file}')
        # print(f'{self.company_name.get()}')
        # print(f'{self.chk_active.get()}')
 

app = MenuFax(None) 
app.mainloop()