import tkinter as tk

root = tk.Tk()
root.title("Sample Tkinter Program")

def button_click():
    label.config(text="Button Clicked!")

label = tk.Label(root, text="Hello, Tkinter!")
label.pack(pady=20)

button = tk.Button(root, text="Click Me!", command=button_click)
button.pack()

root.mainloop()
