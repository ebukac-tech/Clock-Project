import time
from tkinter import *
from tkinter import ttk

#------------------------------------------
#TIMER FUNCTIONS
#------------------------------------------

#start button, stop button
def startTimer():
    # display the necessary widgets
    hrs_entryBox.place_forget()
    label1.place_forget()
    mins_entryBox.place_forget()
    label2.place_forget()
    secs_entryBox.place_forget()
    timerLabel.place(relx=0.5, rely=0.4, anchor='center')
    #get values
    if hrs_entryBox.get().isnumeric():
        hrs_value = int(hrs_entryBox.get())
    else:
        hrs_value=0
    if mins_entryBox.get().isnumeric():
        mins_value = int(mins_entryBox.get())
    else:
        mins_value=0
    if secs_entryBox.get().isnumeric():
        secs_value = int(secs_entryBox.get())
    else:
        secs_value=0


#re-insert placeholders of entry box when out of focus
def putHrs(event):
    if hrs_entryBox.get().isnumeric():
        pass
    else:
        hrs_entryBox.insert(0, "HRS")
        hrs_entryBox.config(foreground='gray')

def putMins(event):
    if mins_entryBox.get().isnumeric():
        pass
    else:
        mins_entryBox.insert(0, "MINS")
        mins_entryBox.config(foreground='gray')

def putSecs(event):
    if secs_entryBox.get().isnumeric():
        pass
    else:
        secs_entryBox.insert(0, "SECS")
        secs_entryBox.config(foreground='gray')


#clear placeholders when clicked
def remove_hrs(event):
    if hrs_entryBox.get().isnumeric():
        pass
    else:
        hrs_entryBox.delete(0, END)
    hrs_entryBox.config(foreground='black')

def remove_mins(event):
    if mins_entryBox.get().isnumeric():
        pass
    else:
        mins_entryBox.delete(0, END)
    mins_entryBox.config(foreground='black')

def remove_seconds(event):
    if secs_entryBox.get().isnumeric():
        pass
    else:
        secs_entryBox.delete(0, END)
    secs_entryBox.config(foreground='black')


#window init
root = Tk()
root.title("Ebuka's Clock")
window_height = 250
window_width = 350
root.geometry(f"{window_width}x{window_height}")
root.resizable(False, False)

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
timerLabel = ttk.Label(timer, text="00:00:00", font=('Arial', 40))

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

#clear placeholders
hrs_entryBox.bind("<FocusIn>", remove_hrs)
mins_entryBox.bind("<FocusIn>", remove_mins)
secs_entryBox.bind("<FocusIn>", remove_seconds)

#put placeholders (when out of focus)
hrs_entryBox.bind("<FocusOut>", putHrs)
mins_entryBox.bind("<FocusOut>", putMins)
secs_entryBox.bind("<FocusOut>", putSecs)

#buttons
start_timerbtn = ttk.Button(timer, text="Start", command=startTimer)
start_timerbtn.place(relx=0.5, rely=0.7, anchor="center")

notebook.pack()

root.mainloop()