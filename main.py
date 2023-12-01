import menu_convertor
import menu_FAX
import tkinter


FAX_DIR = './fax_receive'
PDF_SRC_DIR_PATH = 'C:/Users/kindk/Downloads'
PDF_TO_JPG_DEST_DIR_PATH = 'C:/Users/kindk/dst'

root = tkinter.Tk()


root.title("OC PROGRAMS")
app1 = menu_convertor.PDFconvert(root, PDF_SRC_DIR_PATH, PDF_TO_JPG_DEST_DIR_PATH)
app1.pack()

app2 = menu_FAX.MenuFax(root,FAX_DIR )

btn_close = tkinter.Button(root, padx=5, pady=5, text="Close", width=12, command=root.quit)
btn_close.pack(side="bottom", padx=5, pady=5)



root.resizable(True, True)
root.geometry("500x700+100+10")
root.mainloop()
