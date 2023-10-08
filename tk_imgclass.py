from tkinter import *
 
class MyFrame(Frame):
    def __init__(self, master):
        img = PhotoImage(file='user.png')
        lbl = Label(image=img)
        lbl.image = img  # 레퍼런스 추가
        lbl.pack()
 
def main():
    root = Tk()
    root.title('이미지 보기')
    root.geometry('500x400+10+10')
    myframe = MyFrame(root)
    root.mainloop()
 
if __name__ == '__main__':
    main()