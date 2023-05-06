# Import Module
from tkinter import *
import time
 
# create root window
root = Tk()
root.attributes('-fullscreen',True)
txt = ""
v = DoubleVar() 
cas = 0.1
# root window title and dimension
root.title("Rychloctecka")
# Set geometry (widthxheight)
 
# all widgets will be here
leftframe = Frame(root)
leftframe.pack(side = LEFT, padx=10, pady=10)

txt_vlozte = Label(leftframe, text="Vlozte text, který bude chtít číst: ")
txt_vlozte.grid(column=0, row=0)

slider = Scale(leftframe, from_=0.01, to=1, orient=HORIZONTAL, label = "Rychlost čtení (s)", resolution=0.01, variable=v)
slider.set(0.01)
slider.grid(column=0, row=5)

vlozeni = Text(root, width=10)
vlozeni.pack(side = RIGHT, fill = X, expand = True, padx=10, pady=10, ipadx=10, ipady=10)

def clicked_end():
    root.destroy()
end = Button(root, text = "KONEC PROGRAMU" ,fg = "red", command=clicked_end)
end.pack(side = BOTTOM, padx=10, pady=10)

def tab_text(txt):
    txt = txt.replace("\n", " ")
    words = list(txt.split(" "))
    for i in words:
        cteni = Label(root, text=i, font= ('Arial 40 bold'))
        cteni.place(relx=.5, rely=.5,anchor= CENTER)
        root.update()
        time.sleep(cas)
        cteni.destroy()
    cteni = Label(root, text=i, font= ('40 bold'))
    cteni.place(relx=.5, rely=.5,anchor= CENTER)


def clicked():
    txt = vlozeni.get("1.0",END)
    cas = v.get()
    print(cas)
    vlozeni.destroy()
    leftframe.destroy()
    root.update()
    tab_text(txt)

btn = Button(leftframe, text = "START čtení" ,fg = "red", command=clicked)
btn.grid(column=0, row=1)

# Execute Tkinter
root.mainloop()
