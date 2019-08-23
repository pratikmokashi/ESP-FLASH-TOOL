import os 
import time
from tkinter import *
print(os.getcwd())
window = Tk()
window.title("esp flash tool")
window.geometry('500x210')

lbl = Label(window, text="Hello this is esp flashing tool",font=("Arial Bold",10))
lb_make = Label(window,text="click to make the project")
lb_path = Label(window,text="insert your project path")
lb_flash = Label(window,text="click to flash")
lb_make_flash = Label(window,text="click to make and flash")
lb_monitor = Label(window,text="click to monitor")
lb_erase = Label(window,text="click to erase flash")

make_command ='make'
flash_command ='make flash'
make_flash_command ='make && make flash'
monitor_command = 'make monitor'
erase_flash_command = 'make earase_flash'

def make_clicked():
    lb_make.configure(text="making")
    print(os.getcwd())
    os.system(make_command)

def path_clicked():
    lb_path.configure(text="path inserted")
    res = txt.get()
    time.sleep(0.2)
    os.chdir(res)
    print(os.getcwd())

def flash_clicked():
    lb_flash.configure(text="flashing your esp32")
    time.sleep(0.2)
    os.system(flash_command)
    lb_flash.configure(text="esp32 flashed")

def flash_make_clicked():
    lb_make_flash.configure(text="making and flashing the esp32")
    time.sleep(0.2)
    os.system(make_flash_command)
    lb_make_flash.configure(text="compiled")

def monitor_clicked():
    lb_monitor.configure(text="monitor opened")
    time.sleep(0.2)
    os.system(monitor_command)

def erase_clicked():
    lb_erase.configure(text="erased")
    time.sleep(0.2)
    os.system(erase_flash_command)

txt = Entry(window,width=10)
txt.grid(column=0, row=2)    

btn_path = Button(window, text="PATH",command=path_clicked)
btn_path.grid(column=1, row=2)

btn_make = Button(window, text="MAKE",command=make_clicked)
btn_make.grid(column=1, row=3)

btn_flash= Button(window, text="FLASH",command=flash_clicked)
btn_flash.grid(column=1, row=4)

btn_flash_make= Button(window, text="MAKE+FLASH",command=flash_make_clicked)
btn_flash_make.grid(column=1, row=5)

btn_monitor= Button(window, text="MONITOR",command=monitor_clicked)
btn_monitor.grid(column=1, row=6)

btn_erase= Button(window, text="ERASE",command=erase_clicked)
btn_erase.grid(column=1, row=7)

lbl.grid(column=1, row=0)
lb_path.grid(column=3,row=2)
lb_make.grid(column=3,row=3)
lb_flash.grid(column=3,row=4)
lb_make_flash.grid(column=3,row=5)
lb_monitor.grid(column=3,row=6)
lb_erase.grid(column=3,row=7)




window.mainloop()

