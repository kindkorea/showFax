import tkinter
import os
import glob
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from queue import Queue
import sys


class CustomHandler(FileSystemEventHandler):
    def __init__(self, app):
        FileSystemEventHandler.__init__(self)
        self.app = app
    def on_created(self, event): self.app.notify(event)
    def on_deleted(self, event): self.app.notify(event)
    def on_modified(self, event): self.app.notify(event)
    def on_moved(self, event): self.app.notify(event)

class WatchDirectory(object):
    def __init__(self,src_path):
        path = src_path
        handler = CustomHandler(self)
        self.observer = Observer()
        self.observer.schedule(handler, path, recursive=True)
        self.queue = Queue()
        self.observer.start()
        # self.list_box = list_box

    def handle_watchdog_event(self, event):
        """Called when watchdog posts an event"""
        watchdog_event = self.queue.get()
        print("event type:", type(watchdog_event))

    def shutdown(self, event):
        print("""Perform safe shutdown when GUI has been destroyed""")
        self.observer.stop()
        self.observer.join()

    def notify(self, event):
        """Forward events from watchdog to GUI"""
        self.queue.put(event)
        self.handle_watchdog_event(event)


class MenuFax():

    def __init__(self, parent):
        # tkinter.Tk.__init__(self,parent)

        self.DIRECTOR_PATH = 'f:/OONGCHEON/사무실서류/수신팩스/'
        self.frame = parent
        self.parent = tkinter.Frame(self.frame)
        self.initialize()
        self.src_file =''
        self.src_path = self.DIRECTOR_PATH
        self.parent.pack(side='top')
        watch = WatchDirectory(self.DIRECTOR_PATH)
        # watch.mainloop()

    def initialize(self):
            
        # self.window=tkinter.Tk()
        # 윈도우창 설정
        
        # self.parent.title("웅천목재 프로그램")
        # self.parent.geometry("640x400+100+100")
        # self.parent.resizable(False, False)
        self.txt_value_entry = tkinter.StringVar()
        # 프레임 1
        self.frame=tkinter.Frame(self.parent, 
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

     
        #원클릭 이벤트 설정
        self.listbox.bind('<<ListboxSelect>>', self.items_selected)
        #더블클릭 이벤트 설정
        self.listbox.bind('<Double-Button-1>', self.items_doubleClicked)


        self.listbox.pack(side="left")

        self.scrollbar["command"]=self.listbox.yview
        self.chk_active = tkinter.IntVar()


        # 프레임 2
        self.frame2 =tkinter.Frame(self.parent, 
                            width=300,
                            )

        self.btn_all_files = tkinter.Button(self.frame2, text='모든파일' ,command=self.all_files)
        self.btn_noCheck_files = tkinter.Button(self.frame2, text='미확인파일', command=self.noCheck_files)
        self.btn_Checked_files = tkinter.Button(self.frame2, text='확인파일', command=self.checked_files)


        self.frame3 =tkinter.Frame(self.parent, 
                            width=300,
                            )


        self.chk_button = tkinter.Checkbutton(self.frame3,text='확인' , variable=self.chk_active)
        self.btn_convert = tkinter.Button(self.frame3,text='이름바꾸기', command=self.convert_filename)
        self.company_name = tkinter.Entry(self.frame3,textvariable=self.txt_value_entry)


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

        self.txt_value_entry = 'hello'
        if filename[0] == 'v' :
            self.chk_active.set(True)
            return True
        else :
            self.chk_active.set(False)
            return False

    def items_selected(self,event):
        # print(f'{self.listbox.curselection()=}')
        selected_indices = self.listbox.curselection()
        if selected_indices:
            index = selected_indices[0]
            self.src_file = self.listbox.get(index)
            self.reload_file(os.path.basename(self.src_file))
        else:
            print("No entry") 
    

    def items_doubleClicked(self,event):
        selected_indices = self.listbox.curselection()
        msg = self.listbox.get(selected_indices[0])
        # os.system(f'./img/{msg}')



    def FAX_rename(self, dst_file, is_checked) :
            print(f'{self.src_file=}, {dst_file=}, {is_checked=}')
            try :
                #파일 생성일자를 업체명 뒤에 붙임
                creation_time = time.gmtime(os.path.getctime(self.src_file))
                file_ctime = time.strftime("%Y_%m_%d", creation_time)

                #소스 파일을 파일, 확장자로 쪼갬
                file_path, file_name_ext = os.path.split(self.src_file)
                file_name , file_ext = os.path.splitext(file_name_ext)

                #새로 변경할 파일명을 조립함
                try :
                    dst_file_name = f'{file_path}/{dst_file}_{file_ctime}{file_ext}'
                    os.rename(self.src_file,dst_file_name)
                    self.noCheck_files()
                except FileExistsError :
                    print(f'{dst_file_name} is exited')
            except FileNotFoundError :
                print(f'{self.src_file} is not found')

    def get_file(self):
        
        load_files = glob.glob(self.DIRECTOR_PATH +'/*.*')
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
        self.FAX_rename( self.company_name.get(), self.chk_active.get())
        # print(f'{self.src_file}')
        # print(f'{self.company_name.get()}')
        # print(f'{self.chk_active.get()}')
 
# root = tkinter.Tk()
# app = MenuFax(root) 
# root.mainloop()