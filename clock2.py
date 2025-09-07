from tkinter import *
from tkinter import ttk

root = Tk()
root.title("My Clock")

notebook = ttk.Notebook(root)
#make frames
timer = ttk.Frame(notebook)
stopwatch = ttk.Frame(notebook)
localTime = ttk.Frame(notebook)
#add to notebook
notebook.add(timer, text="Timer")
notebook.add(stopwatch, text="Stopwatch")
notebook.add(localTime, text="Local time")

#TIMER
hrs_entryBox = ttk.Entry(timer, width=5)
hrs_entryBox.place(relx=0.6, rely=0.5)

label1 = ttk.Label(timer, text=":")
label1.place(relx=0.45, rely=0.5)

mins_entryBox = ttk.Entry(timer, width=5)
mins_entryBox.place(relx=0.5, rely=0.5)

label2 = ttk.Label(timer, text=":")
label2.place(relx=0.55, rely=0.5)

secs_entryBox = ttk.Entry(timer, width=5)
secs_entryBox.place(relx=0.4, rely=0.5)

notebook.pack()

root.mainloop()