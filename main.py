import tkinter as tk
from tkinter import ttk
from tkinter import simpledialog, filedialog
import tkinter
import os
import sys
from git import Repo
import threading
def exit():
    sys.exit()

urls = ""
loc=""

window = tk.Tk()
window.title("Spotdl GUI")
window.geometry("600x300")
creds="Spotdl GUI By JasperDG, Sun Valley ttk theme By rdbende"
try:
    window.tk.call("source", "theme/sun-valley.tcl")
    window.tk.call("set_theme", "dark")
except:
    Repo.clone_from("https://github.com/rdbende/Sun-Valley-ttk-theme.git", "./theme")
    window.tk.call("source", "theme/sun-valley.tcl")
    window.tk.call("set_theme", "dark")

browseFrame = ttk.Frame()

browseText = ttk.Label(text="Output directory:", master=browseFrame)
browseText.grid(row=1, column=1)

browseEntry = ttk.Entry(width=50, master=browseFrame, state=tk.DISABLED)
browseEntry.grid(row=2, column=1)

def browse():
    global loc
    global browseEntry
    browseEntry.config(state=tk.NORMAL)
    loc = tkinter.filedialog.askdirectory()
    browseEntry.delete(0, tk.END)
    browseEntry.insert(tk.END, loc)
    browseEntry.config(state=tk.DISABLED)

browseBtn = ttk.Button(text="Browse", master=browseFrame, command=browse)
browseBtn.grid(row=2, column=2)

browseFrame.grid(row=1, column=1)

urlsTitleLabel = ttk.Label(text="URLs: ")
urlsTitleLabel.grid(row=2, column=1)

urlsText = tk.Text(urls, width=50, height=10, state=tk.DISABLED)
urlsText.grid(row=3, column=1)

buttonsFrame = ttk.Frame()

def addUrl():
    global urls
    global urlsText
    
    inp = tk.simpledialog.askstring("Add Url", "Enter URL: ")
    if inp!=None:
        if urls!="":
            urls = urls+"\n"
        urls = urls + inp
        urlsText.config(state=tk.NORMAL)
        urlsText.insert(tk.END, inp+"\n")
        urlsText.config(state=tk.DISABLED)

def removeUrl():
    try:
        global urls
        global urlsText
        urlsArr = urls.split("\n")
        urls=""
        urlsArr.pop(len(urlsArr)-1)
        for url in urlsArr:
            if urls!="":
                urls = urls+"\n"
            urls = urls + url

        urlsText.config(state=tk.NORMAL)
        urlsText.delete("1.0", tk.END)
        urlsText.insert(tk.END, urls)
        urlsText.config(state=tk.DISABLED)
    except:
        a=0

def dl(multiThreaded):
    if loc!="" and urls!="":
        global window
        window.destroy()
        tk.messagebox.showinfo("Spotdl GUI", "You can follow the download progress in the command prompt (the black window, multithreaded tasks may not look best).")
        urlsArr = urls.split("\n")
        if multiThreaded:
            for url in urlsArr:
                threading.Thread(target=lambda: os.system(f"cd /d \"{loc}\" && spotdl {url}")).start()
        else:
            for url in urlsArr:
                os.system(f"cd /d \"{loc}\" && spotdl {url}")
        exit()
    elif loc=="":
        tkinter.messagebox.showwarning("Spotdl GUI", "Enter a valid path. Use \"browse\" to select a path.")
    else:
        tkinter.messagebox.showwarning("Spotdl GUI", "Enter URLs. Use \"Add Url\" to add URLs.")



addURlBtn = ttk.Button(text="Add URL", command=addUrl, master=buttonsFrame, width=15, padding=5)
addURlBtn.grid(row=1, column=1)

clearUrl = ttk.Button(text="Clear last URL", command=removeUrl, master=buttonsFrame, width=15, padding=5)
clearUrl.grid(row=2, column=1)

startDlBtn= ttk.Button(text="Start download", command=lambda: dl(False), master=buttonsFrame, width=15, padding=5)
startDlBtn.grid(row=3, column=1)

startDLMBtn = ttk.Button(text="Start download\n(multi-threaded)", command=lambda: dl(True), master=buttonsFrame, width=15, padding=5)
startDLMBtn.grid(row=4, column=1)

buttonsFrame.grid(row=3, column=2)

credsLabel = ttk.Label(text=creds)
credsLabel.grid(row=4, column=1)

quitBtn = ttk.Button(text="Quit", command=lambda: exit(), width=15, padding=5)
quitBtn.grid(row=4, column=2)

window.mainloop()