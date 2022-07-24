from tkinter import *

def setwindow(root): # window setting
    root.title("Окно программы")
    root.resizable(False, False)
    x = 800
    y = 600
    sw = root.winfo_screenwidth()
    sh = root.winfo_screenheight()
    a = int(sw / 2 - x / 2)
    b = int(sh / 2 - y / 2)
    root.geometry("{0}x{1}+{2}+{3}".format(x, y, a, b))

def hendlerbutton():
    global en1
    global en2
    global result
    try:
        r = str(float(en1.get()) + float(en2.get()))
        result.config(text = "Сумма числе равна:" + r)
    except ValueError:
        result.config(text = "Некорректный ввод")

root = Tk()
setwindow(root)

header = Label(root, text = "Введите числа", font = "Tahoma 15")
en1 = Entry(root, font = "Tahoma 15")
en2 = Entry(root, font = "Tahoma 15")
button = Button(root, text = "Сумма", font = "Tahoma 15", command = hendlerbutton)
result = Label(root, font = "Tahoma 15")

header.place(relx = 0.5, rely = 0.01, anchor="n")
en1.place(relx = 0.5, rely = 0.1, anchor="n")
en2.place(relx = 0.5, rely = 0.2, anchor="n")
button.place(relx = 0.5, rely = 0.3, anchor="n")
result.place(relx = 0.5, rely = 0.4, anchor="n")

root.mainloop()
