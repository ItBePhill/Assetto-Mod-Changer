import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import threading
import os
import json
import shutil
import datetime
from time import sleep
import subprocess
import tkfilebrowser
#Assetto Mod Changer Ver 0.1
#Made By Phillip Wood
#https://github.com/ItBePhill/Assetto-Mod-Changer
#py installer commandpyinstaller --noconfirm --onefile --console --add-data "C:/Users/phill/AppData/Local/Programs/Python/Python310/Lib/site-packages/tkfilebrowser;tkfilebrowser/"  "D:/programing languages/Python/Assetto Mod Changer/Main.py"
#If you didn't get this from me or my Github it is not legit and should be deleted as it may be altered!
# I do not Charge for what I make so if you paid for this refund it and delete it as it may be altered!
#FUCK YOU MICROSFT YOU PIECES OF SHIT!
def Log(ob):
    global f
    now = datetime.datetime.now()
    ob = str(ob)
    final = "\n\n"+now.strftime("%Y-%m-%d %H:%M:%S") + ": " + ob
    print(final)
    f = open(os.path.join(os.getcwd(), "Logs", str(len(logs)))+ " " +now.strftime("%Y-%m-%d")+ " log.txt" , "a")
    f.write(final)
    return f



version = "0.1"
paths = {
    "destination" : r"D:\programing languages\Python\Assetto Mod Changer"
}
collection = {
    "name" : "AYO DEVIL MAY CRY ANIME??????"
}
collections = {

}
logs = []
if not os.path.exists(os.path.join(os.getcwd(), "Logs")):
    os.mkdir(os.path.join(os.getcwd(), "Logs"))

for i in os.listdir(os.path.join(os.getcwd(), "Logs")):
    if i.endswith(".txt"):
        logs.append(i)
    
if not os.path.exists(os.path.join(os.getcwd(), "Collections")):
    os.mkdir(os.path.join(os.getcwd(), "Collections"))
try:
    with open("Paths.json", "r") as r:
        data = json.load(r)
        r.close()

except Exception as e:
    Log(str(e) + " (Don't Worry this is supposed to happen!)")
    with open("Paths.json", "w") as w:
        json.dump(paths, w)
        w.close()

else:
    with open("Paths.json", "r") as r:
        data = json.load(r)
        r.close()
        

fl = []
selected = None
root = tk.Tk()
root.geometry("800x600")
root.title("Assetto Mod Changer v2 ver: "+version)
#Setup------------------------------------------------------
def createcoll():
    Setup =  tk.Toplevel(root)
    Setup.geometry("300x400")
    Setup.title("Create a Collection")
    #lists all files and adds a checkbox for each
    Log("Createcoll")
    destlab = ttk.Label(Setup, text = "Assetto Corsa Folder:")
    destlab.pack()
    dest = ttk.Entry(Setup, width = "100")
    dest.pack()
    dest.insert(0,paths["destination"])
    namelab = ttk.Label(Setup, text = "Pick a Name for your Collection")
    namelab.pack()
    nameent = ttk.Entry(Setup)
    nameent.pack(pady = 10)
    filelab = ttk.Label(Setup, text = "Mods added:")
    filelab.pack()
    def selectmods():
        def delete(x):
            fd.pop(x)
            fdbutt[x].pack_forget()
            Log(fd)
        global selected
        global fd
        fd = tkfilebrowser.askopendirnames()
        fd = list(fd)
        fdbutt = []
        for i in range(len(fd)):
            fdbutt.append(ttk.Button(text = fd[i], command = lambda x = i: delete(x)))
            fdbutt[i].pack()
        return selected, fd
    def Create():
        name = nameent.get()
        name = name.replace(' ', '_')
        collection["name"] = name
        x = 0
        for i in fd:
                collection["File"+str(x)] = i
                x+=1
        Log(collection)
        with open("Collections/"+name+".json", "w") as w:
            json.dump(collection, w)
        for i in fd:
            try:
                shutil.copytree(i, os.path.join(os.getcwd(), "Collections", name, i))
            except Exception as e:
                print(e)
            else:
                shutil.copytree(src = i, dst = os.path.join(os.getcwd(), "Collections", name))

        complete = ttk.Label(Setup, text = name+" Successfully Created")
        complete.pack()
        sleep(2)
        Setup.destroy()
    paths["destination"] = dest.get()
    cont = ttk.Button(Setup, text = "Create Collection", command = Create)
    cont.pack()
    mods = ttk.Button(text = "Add or remove mods", command = selectmods)
    mods.pack()


def removecoll():
    print("Removecoll")
#Setup-----------------------------------------------
def Switch(c):
    global current
    if messagebox.askyesnocancel(title = "Are you sure you want to change?", message = "Are you sure you want to change collection (It may take some time)"):
       current = c.replace('_', ' ')
       currlab.config(text = "Currently Selected: " + os.path.splitext(current)[0])
       Log("Changed Collection to "+ current)
       return current
def advanced():
    def Clear(c):
        if c == "OL":
            Log("Opened Logs")
            com = r'explorer /select, '+ os.path.join(os.getcwd(), "Logs")
            subprocess.Popen(com)
        elif c == "P":
            if messagebox.askokcancel(title = "Clear", message = "Clear Paths.json?"):
                Log("Cleared Paths")
                os.remove(os.path.join(os.getcwd(), "Paths.json"))
        elif c == "L":
            if messagebox.askokcancel(title = "Clear", message = "Clear Logs? Warning: this will restart the program"):
                f.close()
                shutil.rmtree(os.path.join(os.getcwd(), "Logs"))
                Log("Cleared Logs")
                sys.exec()
        elif c == "C":
            if messagebox.askokcancel(title = "Clear", message = "Clear Collections?"):
                Log("Cleared Collections")
                shutil.rmtree(os.path.join(os.getcwd(), "Collections"))
            
    Log("advanced")
    advwin = tk.Toplevel(root)
    advwin.geometry("400x300")
    advwin.title("Advanced options")
    warn = ttk.Label(advwin, text = "Advanced Options\nWarning: These options could break things or permenantly delete data")
    warn.pack(pady = 10)
    OpenLogs = ttk.Button(advwin, text = "Open logs folder", command = lambda: Clear("OL"))
    OpenLogs.pack()
    clearPaths = ttk.Button(advwin, text = "Clear Paths.json", command = lambda: Clear("P"))
    clearPaths.pack()
    clearLogs = ttk.Button(advwin, text = "Clear Logs", command = lambda: Clear("L"))
    clearLogs.pack()
    clearColls = ttk.Button(advwin, text = "Clear Collections", command = lambda: Clear("C"))
    clearColls.pack()


current  = ""
collstr = ""
ver = ttk.Label(text = "Version: "+version, foreground= "Grey")
ver.pack(anchor = "nw")
adv = ttk.Button(text = "Advanced", width = "9", command = advanced)
adv.pack(anchor = "nw")
cc = ttk.Button(text = "Create Collection", command = createcoll)
cc.pack()
rc = ttk.Button(text = "Remove Collection", command = removecoll)
rc.pack()
currlab = ttk.Label(text = "Currently Selected: " + os.path.splitext(current)[0])
currlab.pack(pady = 10)
created = ttk.Label(text = "P.S Collections Refresh every 10 seconds\nCreated Collections:")
created.pack()
def updatecolls():
    global collstr
    for root, dirs, files in os.walk(os.path.join(os.getcwd(), "Collections")):
        for file in files:
            if file.endswith(".json"):
                if collstr.find(file) == -1:
                    collstr += "\n"+file
                    collections[file] = ttk.Button(text = os.path.splitext(file)[0].replace('_', ' '), command = lambda i = file: Switch(i))
                    collections[file].pack()
                    Log("Updated "+str(collections))

    up = threading.Timer(10,updatecolls)
    up.start()
    return collstr
updatecolls()
def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        with open("Paths.json", "w") as w:
            json.dump(paths, w)
            w.close()
        root.destroy()
        quit()
    f.close()
root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()