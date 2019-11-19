# JUST RUN THIS FILE TO SEE THE MAGIC
#Created By Rohan Chopra


import View as view
import tkinter as tk

window = tk.Tk()
window.title("Minimum Spanning Tree ")
window.geometry("412x324") # size of the window width:- 500, height:- 375
window.resizable(0, 0)
v = view.ViewSpace(window)
v.setUpInitalView()
window.mainloop()