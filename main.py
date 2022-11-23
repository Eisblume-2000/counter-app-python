import tkinter as tk
import os

if os.path.exists(r"C:\ProgramData\counter.txt") == False:
    r = open(r"C:\ProgramData\counter.txt","w")
    r.write("0")
    r.close()
else:
    pass

class GUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("400x500")
        self.window.title("Counter")
        self.window['background'] = '#202124'
        self.window.resizable(0, 0)

        r = open(r"C:\ProgramData\counter.txt","r")
        number = int(r.read())
        r.close()

        self.button = tk.Button(self.window,text="UP",font=("Arial"),command=self.up)
        self.button.place(y=75, relx=0.5, anchor="center", width=100)

        self.label2 = tk.Label(self.window, text=number,font=("Arial"))
        self.label2.place(y=175, relx=0.5,anchor="center", width=50, height=75)

        self.button2 = tk.Button(self.window, text="Down", font=("Arial"),command=self.down)
        self.button2.place(y=275, relx=0.5, anchor="center", width=100)

        self.button3 = tk.Button(self.window, text="Reset", font=("Arial"),command=self.reset)
        self.button3.place(y=400, relx=0.5, anchor="center", width=100)

        self.button4 = tk.Button(self.window, text="Close", font=("Arial"),command=self.close)
        self.button4.place(y=475, relx=0.5, anchor="center", width=100)

        self.window.mainloop()

    def up(self):
        r = open(r"C:\ProgramData\counter.txt", "r")
        number = int(r.read())
        r.close()

        number = number + 1

        r = open(r"C:\ProgramData\counter.txt", "w")
        r.write(str(number))
        r.close()

        self.label2 = tk.Label(self.window, text=number, font=("Arial"))
        self.label2.place(y=175, relx=0.5, anchor="center", width=50, height=75)

    def down(self):
        r = open(r"C:\ProgramData\counter.txt", "r")
        number = int(r.read())
        r.close()

        number = number - 1

        r = open(r"C:\ProgramData\counter.txt", "w")
        r.write(str(number))
        r.close()

        self.label2 = tk.Label(self.window, text=number, font=("Arial"))
        self.label2.place(y=175, relx=0.5, anchor="center", width=50, height=75)

    def reset(self):
        number = 0

        r = open(r"C:\ProgramData\counter.txt", "w")
        r.write(str(number))
        r.close()

        self.label2 = tk.Label(self.window, text=number, font=("Arial"))
        self.label2.place(y=175, relx=0.5, anchor="center", width=50, height=75)

    def close(self):
        self.window.destroy()
        exit()

GUI()