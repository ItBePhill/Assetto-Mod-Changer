import tkinter as tk
from tkinter import ttk
import tkfilebrowser
import threading
import os
import json
from time import sleep
paths = {
    "destination" : r"D:\programing languages\Python\Assetto Mod Changer"
}
collection = {
    "name" : "AYO DEVIL MAY CRY ANIME??????"
}


fl = []
selected = None
root = tk.Tk()
root.geometry("800x600")
root.title("Assetto Mod Changer v2 ver 0.1")
#Setup------------------------------------------------------
def createcoll():
    Setup =  tk.Toplevel(root)
    Setup.geometry("400x300")
    Setup.title("Create a Collection")
    #lists all files and adds a checkbox for each
    def Select():
        def Create():
            name = nameent.get()
            name = name.replace(' ', '_')
            collection["name"] = name
            x = 0
            for i in fd:
                 collection["File"+str(x)] = i
                 x+=1
            print(collection)

            with open(name+".json", "w") as w:
                 json.dump(collection, w)
            complete = ttk.Label(Setup, text = name+" Successfully Created")
            complete.pack()
            sleep(2)
            Setup.destroy()
            
                
            
        global selected
        fd = tkfilebrowser.askopendirnames(title = "Select the files you want to be in the collection", initialdir = paths["destination"])
        strfd = ""
        for i in fd:
            strfd = strfd + os.path.basename(i)+"\n"
        if selected == None:
            selected = ttk.Label(Setup, text = strfd)
            selected.pack()
            cont = ttk.Button(Setup, text = "Create Collection", command = Create)
            cont.pack()
        else:
            selected.config(text = strfd)
        return selected
    print("Createcoll")
    destlab = ttk.Label(Setup, text = "Assetto Corsa Folder:")
    destlab.pack()
    dest = ttk.Entry(Setup, width = "100")
    dest.pack()
    dest.insert(0,paths["destination"])
    namelab = ttk.Label(Setup, text = "Pick a Name for your Collection")
    namelab.pack()
    nameent = ttk.Entry(Setup)
    nameent.pack(pady = 10)
    conbutt = ttk.Button(Setup, text = "Add or remove Mods", command = Select)
    conbutt.pack()
    filelab = ttk.Label(Setup, text = "Currently added Mods:")
    filelab.pack()
def removecoll():
    print("Removecoll")
#Setup-----------------------------------------------
collstr = ""
ver = ttk.Label(text = "Version 0.1", foreground= "Grey")
ver.pack(anchor = "nw")
cc = ttk.Button(text = "Create Collection", command = createcoll)
cc.pack()
rc = ttk.Button(text = "Remove Collection", command = removecoll)
rc.pack()
created = ttk.Label(text = "P.S Collections Refresh every 5 seconds\nCreated Collections:")
created.pack()
colllab = ttk.Label(text = collstr)
colllab.pack()
def updatecolls():
    global collstr
    for root, dirs, files in os.walk(os.getcwd()):
        for file in files:
            if file.endswith(".json"):
                if collstr.find(file) == -1:
                    collstr += "\n"+file
                    colllab.config(text = collstr)
    up = threading.Timer(5,updatecolls)
    up.start()
    return collstr

updatecolls()
tk.mainloop()