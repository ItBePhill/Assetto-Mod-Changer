import tkinter as tk
from tkinter import ttk
import threading
import os
import json
paths = {
    "destination" : r"D:\programing languages\Python\Assetto Mod Changer"
}
collection = {
    "name" : ""
}
checks = {
    
}
def OnCheckChange(checks):
    temp = list(checks)
    temp.clear()
    checks = tuple(temp)
    print(checks[1].state())
def createcoll():
    def listdir():
        paths["destination"] = dest.get()
        namelab = ttk.Label(Setup, text = "Enter a name for your collection")
        namelab.pack()
        name = ttk.Entry(Setup)
        name.pack()
        select = ttk.Label(Setup, text = "Select which Mods you will add to this collection:")
        select.pack()
        x = 0
        for i in os.listdir(paths["destination"]):
            x += 1 
            checks[x] = ttk.Checkbutton(Setup,text = i, command = lambda: OnCheckChange(checks) ,onvalue = 1, offvalue = 0)
            checks[x].pack()

        con = ttk.Button(Setup, text = "Continue")
        con.pack()
    
    print("Createcoll")
    cc.pack_forget()
    rc.pack_forget()
    destlab = ttk.Label(Setup, text = "Assetto Corsa Folder:")
    destlab.pack()
    dest = ttk.Entry(Setup, width = "100")
    dest.pack()
    conbutt = ttk.Button(Setup, text = "Continue", command = listdir)
    conbutt.pack()

def removecoll():
    print("Removecoll")

root = tk.Tk()
root.geometry("800x600")
root.title("Assetto Mod Changer v2 ver 0.1")
if os.path.exists("Paths.json") != True:
    Setup = tk.Toplevel(root)
    Setup.geometry("800x600") 
    Setup.title("First Time Setup")
    title = ttk.Label(Setup, text = "First Time Setup")
    title.pack(pady = 10)
    cc = ttk.Button(Setup, text = "Create Collection", command = createcoll)
    cc.pack()
    rc = ttk.Button(Setup, text = "Remove Collection", command = removecoll)
    rc.pack()

    
    




ver = ttk.Label(text = "Version 0.1", foreground= "Grey")
ver.pack(anchor = "nw")
tk.mainloop()