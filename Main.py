from tkinter import *

import time, keyboard, pyautogui, threading
window = Tk()

window.title("Auto Clicker V1")

def clickedStart():
    print("Clicked")
    time.sleep(3)

    run = True
    intervalInt = None

    try:
        intervalInt = int(txt.get())
    except:
        pass

    start = time.time()

    while run == True:

        if keyboard.is_pressed("0"):
            run = False
            break

        if intervalInt != None:
            if time.time() >= (start + intervalInt):
                pyautogui.click()
                start = time.time()
        else:
            pyautogui.click()

lbl = Label(window, text="Tıklama Süresi")
lbl.grid(column=1, row=0, padx=(70, 18), pady=(10,0))

txt = Entry(window, width=10)
txt.grid(column=1, row=1, padx=(75, 10))

btn = Button(window, text="Başlat", command=clickedStart, bg="green", fg="lightgreen")
btn.grid(column=1, row=2, padx=(75,10), pady=(15,10))

window.geometry("250x180")

icon = PhotoImage(file="logo.png")
window.iconphoto(False, icon)

window.mainloop()