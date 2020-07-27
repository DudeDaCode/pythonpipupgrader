import os
import tkinter as tk

root= tk.Tk()

root.wm_title("PIP Upgrade")

canvas1 = tk.Canvas(root, width = 300, height = 100, bg = '#e9d700', relief = 'raised')
canvas1.pack()

def upgradePIP ():
    os.system('start cmd /k python.exe -m pip install --upgrade pip') 
    
button1 = tk.Button(text='      Upgrade PIP     ', command=upgradePIP, bg='green', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 50, window=button1)

root.mainloop()
