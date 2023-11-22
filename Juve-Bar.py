from tkinter import PhotoImage, Tk, Label, CENTER
import random, time


def rand():
    x = random.choice(
        ["c0.png", "c0.png", "c0.png", "c0.png", "c0.png", "c1.png", "c1.png", "c1.png", "c1.png", "c2.png",
         "c2.png", "c2.png", "c3.png", "c3.png", "c4.png"])
    return x


def start(click_mouse):
    global h1, h2
    for i in range(10):
        h1 = PhotoImage(file=rand())
        h2 = PhotoImage(file=rand())
        lab1["image"] = h1
        lab2["image"] = h2
        root.update()
        time.sleep(0.1)


root = Tk()
root.geometry("849x442")
root.title("Предсказатель счета! Нажмите ЛЕВУЮ кнопку мышки!!!", )
root.resizable(height=False, width=False)
root.iconphoto(True, PhotoImage(file='soc.png'))
fon = PhotoImage(file='fon.png')
Label(root, image=fon).pack()
lab1 = Label(root)
lab1.place(relx=0.34, rely=0.8, anchor=CENTER)
default1 = PhotoImage(file='ques.png')
lab1["image"] = default1

lab2 = Label(root)
lab2.place(relx=0.65, rely=0.8, anchor=CENTER)
default2 = PhotoImage(file='ques.png')
lab2["image"] = default2

root.bind("<1>", start)
## start("a")

root.mainloop()
