#Before Copy this Source, Please, Take Owner Permission and Give Credits.
#Thanks.

try:
    from tkinter import *
except ImportError:
    from Tkinter import *
import time
from pwgenfunc import RandPass

#Main
def pwGenerator(size = 8):
    data = RandPass(size)
    new_password = data[0]
    pw_strength = data[1]
    pw_color = data[2]
    PASSWORD.set(new_password);
    label_strength.configure(foreground="white", background=pw_color, text=pw_strength, font=('Segoe UI', 10, 'bold'), bd=10, height=1, width=10)
    gui.clipboard_clear()
    gui.clipboard_append(new_password)
    gui.update()
    time.sleep(.02)
    gui.update()
    gui.mainloop()

#MainWindow
gui = Tk()
gui.title("Password Generator")
gui.config(bg = '#1A1A1A')
gui.title('Password Gen') 
width = 600
height = 342
screen_width = gui.winfo_screenwidth()
screen_height = gui.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
gui.geometry("%dx%d+%d+%d" % (width, height, x, y))

#Var
PASSWORD = StringVar()
PW_SIZE = IntVar()
e1 = Entry(gui, text=PW_SIZE)
PW_SIZE.set(8) # sets the default value for PW size/length

#WindowFrame
Top = Frame(gui, width=width)

Top.pack(side=TOP)
Top.config(bg = '#1A1A1A')
Form = Frame(gui, width=width, background="#1A1A1A",)
Form.pack(side=TOP)
Bot = Frame(gui, width=width)
Bot.pack(side=BOTTOM)

#Label
label_password = Label(Form, font=('Segoe UI', 18), text="Password",foreground="white", background="#1A1A1A", bd=10)
label_password.grid(row=0, pady=10)
label_strength = Label(Form, font=('Segoe UI', 10, 'bold'), foreground="white", background="white", text="Weak", bd=10, height=1, width=10)
label_strength.grid(row=0, column=3, pady=10, padx=10)
label_pw_size = Label(Form, font=('Segoe UI', 18), text="Size",foreground="white", background="#1A1A1A", bd=10)
label_pw_size.grid(row=2, pady=10)
label_instructions = Label(Bot, width=width, font=('Segoe UI', 12, 'bold'), text="Password Generated to your Clipboard!", foreground="white", background="#1A1A1A", bd=1, relief=SOLID)
label_instructions.pack(fill=X)

#Button
password = Entry(Form, textvariable=PASSWORD, font=(18), width=24)
password.grid(row=0, column=1, columnspan=2)
pw_size = Scale(Form, from_=8, to=24, length=200,width=24,sliderlength=14, orient=HORIZONTAL, variable=PW_SIZE, foreground="white", background="#1A1A1A",  font=(16))
pw_size.grid(row=2, column=1, columnspan=2)

#CopytoClip
def Copy_password():
    pyperclip.copy(new_password_str.get())

Button(Top, text = 'COPY TO CLIPBOARD', foreground="white", background="#1A1A1A", command = Copy_password).pack(pady=5)

btn_generate = Button(Form, text="Generate Now", width=20, command=lambda: pwGenerator(PW_SIZE))
btn_generate.grid(row=4, column=1, columnspan=2)

gui.resizable(False, False)
gui.mainloop()
