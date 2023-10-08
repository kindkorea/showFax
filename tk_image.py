import tkinter
import os

print (os.path.dirname(os.path.realpath(__file__)) ) #프로젝트 소스코드 파일 경로 출력

root=tkinter.Tk()
root.title("blog")
root.geometry("840x420")
root.resizable(0, 0)
image1=tkinter.PhotoImage(file="icon1.png") #PhotoImage를 통한 이미지 지정
label=tkinter.Label(root, image=image1) #라벨 생성, 라벨에는 앞서 선언한 이미지가 들어감.
label.pack()

root.mainloop()