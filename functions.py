import tkinter as tk
from tkinter import ttk

def openNewWindow(root):
    new= tk.Toplevel(root)
    new.geometry('500x500')
    new.title('ثبت')
    tk.Label(new, text="Hey, Howdy?", font=('Helvetica 17 bold')).pack(pady=30)