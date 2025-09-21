#using time.time()
import time
from tkinter import *
from tkinter import ttk

#------------------------------------------
#TIMER FUNCTIONS
#------------------------------------------

#start button, stop button
def startTimer():
    global duration, start_time, running
    running = True
    global duration, start_time
    # display the necessary widgets
    hrs_entryBox.place_forget()
    label1.place_forget()
    mins_entryBox.place_forget()
    label2.place_forget()
    secs_entryBox.place_forget()
    timerLabel.place(relx=0.5, rely=0.4, anchor='center')
    start_timerbtn.config(text="STOP", command=stop)
    start_timerbtn.place(relx=0.3, rely=0.7, anchor="center")
    reset_timerbtn.place(relx=0.7, rely=0.7, anchor="center")
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

    #countdown
    duration = hrs_value*3600 + mins_value*60 + secs_value
    start_time = time.time()  # <-- records start_time only once, here! after button is pressed
    updateTimer() 

def updateTimer():
    global bruh, totSecsContinue
    elapsed_time = time.time() - start_time
    totSecsRemaining = int(duration - elapsed_time)
    totSecsContinue = totSecsRemaining

    if totSecsRemaining >= 0:
        display_mins, display_secs = divmod(totSecsRemaining, 60)
        display_hrs, display_mins = divmod(display_mins, 60)
        timerLabel.config(
            text=f"{display_hrs:02d}:{display_mins:02d}:{display_secs:02d}"
        )
        bruh = timer.after(200, updateTimer)  # schedule another update
    else:
        pass
          


def stop():
    print("Timer has stopped")
    global running
    running = False
    timer.after_cancel(bruh)
    start_timerbtn.config(text="CONTINUE", command=continue_timer)

def continue_timer():
    global start_time, running
    # set start_time so remaining seconds continue correctly
    start_time = time.time() - (duration - totSecsContinue)
    running = True
    updateTimer()
    start_timerbtn.config(text="STOP", command=stop)
    reset_timerbtn.place(relx=0.7, rely=0.7, anchor="center")

def resetTimer():
    hrs_entryBox.place(relx=0.2, rely=0.4, anchor="center")
    label1.place(relx=0.35, rely=0.4, anchor="center")
    mins_entryBox.place(relx=0.5, rely=0.4, anchor="center")
    label2.place(relx=0.65, rely=0.4, anchor="center")
    secs_entryBox.place(relx=0.8, rely=0.4, anchor="center")
    timerLabel.place_forget()
    timer.after_cancel(bruh)
    start_timerbtn.place(relx=0.5, rely=0.7, anchor="center")
    reset_timerbtn.place_forget()
    start_timerbtn.config(text="START", command=startTimer)


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
    hrs_entryBox.config(foreground='#E8DEDC')

def remove_mins(event):
    if mins_entryBox.get().isnumeric():
        pass
    else:
        mins_entryBox.delete(0, END)
    mins_entryBox.config(foreground='#E8DEDC')

def remove_seconds(event):
    if secs_entryBox.get().isnumeric():
        pass
    else:
        secs_entryBox.delete(0, END)
    secs_entryBox.config(foreground='#E8DEDC')


#window init
root = Tk()
root.title("Ebuka's Clock")
window_height = 250
window_width = 370
root.geometry(f"{window_width}x{window_height}")
#root.resizable(False, False)
root.configure(bg="#171717")

notebook = ttk.Notebook(root)
# for darkmode
style = ttk.Style()
style.theme_use("clam")  # "clam" allows custom colors

style.configure("Black.TFrame", background="#171717")
style.configure("Black.TLabel", background="#171717", foreground="#E8DEDC")
style.configure("Black.TButton", background="#171717", foreground="#E8DEDC")
style.configure("Black.TEntry", fieldbackground="#171717", foreground="white", insertbackground="white")
style.configure("white.TButton", background = '#A6A09B', foreground = 'black')

#make frames
timer = ttk.Frame(notebook, style="Black.TFrame", width=window_width, height=window_height)
stopwatch = ttk.Frame(notebook)
localTime = ttk.Frame(notebook)
#add to notebook
notebook.add(timer, text="           Timer               ")
notebook.add(stopwatch, text="           Stopwatch             ")
notebook.add(localTime, text="           Local time                ")

#-----------------------------------------
#TIMER
#-----------------------------------------

#display - timer
timerLabel = ttk.Label(timer, text="00:00:00", font=('Courier', 40), style="Black.TLabel")

#entry boxes
hrs_entryBox = ttk.Entry(timer, foreground="gray", font=("Courier", 20), width=3, style="Black.TEntry")
hrs_entryBox.place(relx=0.2, rely=0.4, anchor="center")
hrs_entryBox.insert(0, "HRS")

label1 = ttk.Label(timer, text=":", font=("Courier", 15), style="Black.TLabel")
label1.place(relx=0.35, rely=0.4, anchor="center")

mins_entryBox = ttk.Entry(timer, foreground="gray", font=("Courier", 20), width=4, style="Black.TEntry")
mins_entryBox.place(relx=0.5, rely=0.4, anchor="center")
mins_entryBox.insert(0, "MINS")

label2 = ttk.Label(timer, text=":", font=("Courier", 15), style="Black.TLabel")
label2.place(relx=0.65, rely=0.4, anchor="center")

secs_entryBox = ttk.Entry(timer, foreground="gray", font=("Courier", 20), width=4, style="Black.TEntry")
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
start_timerbtn = ttk.Button(timer, text="START", command=startTimer, style="Black.TButton")
start_timerbtn.place(relx=0.5, rely=0.7, anchor="center")

reset_timerbtn = ttk.Button(timer, text="RESET", command=resetTimer, style="Black.TButton")

start_timerbtn.bind("<Enter>", lambda event: start_timerbtn.config(style="white.TButton"))
start_timerbtn.bind("<Leave>", lambda event: start_timerbtn.config(style="Black.TButton"))

reset_timerbtn.bind("<Enter>", lambda event: reset_timerbtn.config(style="white.TButton"))
reset_timerbtn.bind("<Leave>", lambda event: reset_timerbtn.config(style="Black.TButton"))


notebook.pack()

root.mainloop()