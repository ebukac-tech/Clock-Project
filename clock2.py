import time
from tkinter import *
from tkinter import ttk

#button functions
def start_timerFunction(totalSeconds=None):
    try:
        num_hrs = int(hrs_entryBox.get())
        num_mins = int(mins_entryBox.get())
        num_secs = int(secs_entryBox.get())
    except ValueError:
        num_hrs=0
        num_mins=0
        num_secs=0
        print("input something valid")

    #-rm entry boxes
    hrs_entryBox.place_forget()
    mins_entryBox.place_forget()
    secs_entryBox.place_forget()
    label1.place_forget()
    label2.place_forget()
    #add timer label
    timerLabel.place(relx=0.5, rely=0.7, anchor="center")

    totalSeconds = int((num_hrs*3600)+(num_mins*60)+num_secs)

    mins, secs = divmod(totalSeconds, 60)
    hrs, mins = divmod(mins, 60)

    timerLabel.config(text="{:02d}:{:02d}:{:02d}".format(hrs, mins, secs))
    print("done")
    totalSeconds-=1
    timer.after(1000, start_timerFunction, totalSeconds)

root = Tk()
root.title("Ebuka's Clock")
window_height = 250
window_width = 350
root.geometry(f"{window_width}x{window_height}")

notebook = ttk.Notebook(root, padding=10)
#make frames
timer = ttk.Frame(notebook, width=window_width, height=window_height)
stopwatch = ttk.Frame(notebook)
localTime = ttk.Frame(notebook)
#add to notebook
notebook.add(timer, text="Timer")
notebook.add(stopwatch, text="Stopwatch")
notebook.add(localTime, text="Local time")

#-----------------------------------------
#TIMER
#-----------------------------------------

#display - timer
timerLabel = ttk.Label(timer, text="00:00:00")

#entry boxes
hrs_entryBox = ttk.Entry(timer, foreground="gray", font=("Arial", 20), width=5)
hrs_entryBox.place(relx=0.2, rely=0.4, anchor="center")
hrs_entryBox.insert(0, "HRS")

label1 = ttk.Label(timer, text=":", font=("Arial", 15))
label1.place(relx=0.35, rely=0.4, anchor="center")

mins_entryBox = ttk.Entry(timer, foreground="gray", font=("Arial", 20), width=5)
mins_entryBox.place(relx=0.5, rely=0.4, anchor="center")
mins_entryBox.insert(0, "MINS")

label2 = ttk.Label(timer, text=":", font=("Arial", 15))
label2.place(relx=0.65, rely=0.4, anchor="center")

secs_entryBox = ttk.Entry(timer, foreground="gray", font=("Arial", 20), width=5)
secs_entryBox.place(relx=0.8, rely=0.4, anchor="center")
secs_entryBox.insert(0, "SECS")

#clear placeholders when clicked
hrs_entryBox.bind("<FocusIn>", lambda event: hrs_entryBox.delete(0, END))
mins_entryBox.bind("<FocusIn>", lambda event: mins_entryBox.delete(0, END))
secs_entryBox.bind("<FocusIn>", lambda event: secs_entryBox.delete(0, END))

#re-insert placeholders when out of focus

def putHrs(event):
    if hrs_entryBox.get().isnumeric():
        pass
    else:
        hrs_entryBox.insert(0, "HRS")

def putMins(event):
    if mins_entryBox.get().isnumeric():
        pass
    else:
        mins_entryBox.insert(0, "MINS")

def putSecs(event):
    if secs_entryBox.get().isnumeric():
        pass
    else:
        secs_entryBox.insert(0, "SECS")

hrs_entryBox.bind("<FocusOut>", putHrs)
mins_entryBox.bind("<FocusOut>", putMins)
secs_entryBox.bind("<FocusOut>", putSecs)

#buttons
start_timerbtn = ttk.Button(timer, text="Start", command=start_timerFunction)
start_timerbtn.place(relx=0.5, rely=0.7, anchor="center")

notebook.pack()

root.mainloop()