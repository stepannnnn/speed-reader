# Import Module
from tkinter import *
import time
# create root window
root = Tk()
root.attributes('-fullscreen',True)
txt = ""
v = DoubleVar() 
cas = 0.8
pause = BooleanVar()
pause = False
restart = False
x = 1
# root window title and dimension
root.title("Rychloctecka")
# Set geometry (widthxheight)
 
# all widgets will be here

leftframe = Frame(root)
leftframe.pack(side = LEFT, padx=10, pady=10)



slider = Scale(leftframe, from_=0.01, to=1, orient=HORIZONTAL, label = "Rychlost čtení (s)", resolution=0.01, variable=v, length=300)
slider.set(0.3)
slider.grid(column=0, row=5)

def start():
    global txt
    global pause
    global vlozeni
    global btn
    global txt_vlozte
    global x
    global leftframe
    vlozeni = Text(root, width=10)
    vlozeni.pack(side = RIGHT, fill = X, expand = True, padx=10, pady=10, ipadx=10, ipady=10)
    txt_vlozte = Label(leftframe, text="Vlozte text, který bude chtít číst: ")
    txt_vlozte.grid(column=0, row=0)
    btn = Button(leftframe, text = "START čtení" ,fg = "red", command=clicked)
    btn.grid(column=0, row=1)
    pause = False
    x = 1

def clicked_end():
    root.destroy()
    exit()
end = Button(leftframe, text = "KONEC PROGRAMU" ,fg = "red", command=clicked_end)
end.grid(column=0, row=6)

#var = Tk.IntVar(leftframe, 255)
def clicked_pause():
    global pause
    global btn_pause
    pause = True
    btn_pause.destroy()
    btn_pause = Button(leftframe, text = "Pokračovat v čtení" ,fg = "red", command=clicked_continue)
    btn_pause.grid(column=0, row=0)
    root.update()
    #btn_pause = Button(leftframe, text = "Pozastavit čtení" ,fg = "red", command=clicked_pause)
    #root.update
    
def clicked_continue():
    global cteni
    global txt
    global pause
    pause = False
    global btn_pause
    btn_pause.destroy()
    btn_pause = Button(leftframe, text = "Pozastavit čtení" ,fg = "red", command=clicked_pause)
    btn_pause.grid(column=0, row=0)
    cteni.destroy()
    tab_text(txt)
    root.update()
    
def clicked_stop():
    global cteni
    global pause
    global x
    global btn_pause
    global btn_konec
    x = 1
    try:
        cteni.destroy()
        btn_konec.destroy()
        btn_pause.destroy()
    except:
        pass
    start()
    pause = True
    


def tab_text(txt):
    global x
    global cteni
    txt = txt.replace("\n", " ")
    words = list(txt.split(" "))
    print(x)
    x_now = 0
    for i in range(x-1, len(words), 1):
        cas = v.get()
        cteni = Label(root, text=words[i], font= ('Arial 40 bold'))
        cteni.place(relx=.5, rely=.5,anchor= CENTER)
        root.update()
        root.after(int(cas*1000))
        
        if pause:
            break
        cteni.destroy()
        x_now = i
    x = x+x_now


def clicked():
    global btn_pause
    global btn_konec
    global txt
    global vlozeni
    global x
    global pause
    txt = vlozeni.get("1.0",END)
    vlozeni.destroy()
    txt_vlozte.destroy()
    btn.destroy()
    btn_konec = Button(leftframe, text = "KONEC čtení" ,fg = "red", command=clicked_stop)
    btn_konec.grid(column=0, row=1)
    btn_pause = Button(leftframe, text = "Pozastavit čtení" ,fg = "red", command=clicked_pause)
    btn_pause.grid(column=0, row=0)
    root.update()
    x = 1
    pause = False
    tab_text(txt)


start()
# Execute Tkinter
root.mainloop()

exit()