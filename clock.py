from tkinter import *
from tkinter import ttk
#from datetime import date
import time
from time import strftime

time_object = time.localtime()

root = Tk()
root.title("Ebuka's Clock")
root.resizable(width=0, height=0)

display_notebook = ttk.Notebook(root, padding=10)
world_clock = ttk.Frame(display_notebook)
stopwatch = ttk.Frame(display_notebook)
alarm = ttk.Frame(display_notebook)
timer = ttk.Frame(display_notebook)
display_notebook.add(timer, text="Timer")
display_notebook.add(stopwatch, text="Stopwatch")
display_notebook.add(world_clock, text="World clock")
display_notebook.add(alarm, text="Alarms")
display_notebook.pack()

#WORLD CLOCK
    #display
ttk.Label(world_clock, text="Localtime", font=("courier", 25)).pack(pady=5, padx=30)
current_time = strftime("%H:%M:%S")
current_time_label = ttk.Label(world_clock, text=current_time, font=("courier", 30), foreground="red")
current_time_label.pack()

    #function
def update(): #update time label
    current_time = strftime("%H:%M:%S")
    current_time_label.config(text=current_time)
    root.after(1000, update)
update()

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>STOPWATCH<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    #display
ttk.Label(stopwatch, text="STOPWACTH", font=("courier", 15)).pack()

stopwatch_display = ttk.Label(stopwatch, text="00:00:00", font=("courier", 25))
stopwatch_display.pack()


    #functions
def start_stopwatch(total_secs=-1): # i used total_secs =0 (-1) because the start value is always 0
    global startdisplaying_stopwatch, totalSecs_stopwatch
    total_secs+=1
    stop_mins, stop_secs = divmod(total_secs, 60)
    stop_hours, stop_mins = divmod(stop_mins, 60)
    stopwatch_display.config(text="{:02d}:{:02d}:{:02d}".format(stop_hours, stop_mins, stop_secs))
    totalSecs_stopwatch = total_secs
    start_stopwatch_button.state(['disabled'])
    stop_stopwatch_button.state(['!disabled'])
    startdisplaying_stopwatch = root.after(1000, start_stopwatch, total_secs) # a kind of while lop to why it keep repeating
    

def reset_stopwatch():
    global totalSecs_stopwatch
    root.after_cancel(startdisplaying_stopwatch)
    stopwatch_display.config(text="00:00:00")
    stop_stopwatch_button.config(text="STOP", command=stop_stopwatch)
    start_stopwatch_button.state(['!disabled'])
    stop_stopwatch_button.state(['disabled'])
    totalSecs_stopwatch=0


def stop_stopwatch():
    root.after_cancel(startdisplaying_stopwatch)

    stopwatch_stopped=1
    if stopwatch_stopped==1:
        stop_stopwatch_button.config(text="CONTINUE", command=continue_stopwatch)


def continue_stopwatch(nigga=None):
    global stopwatch_continued
    stopwatch_continued = 1
    global totalSecs_stopwatch
    if nigga==None:
        nigga=totalSecs_stopwatch-1
    global startdisplaying_stopwatch
    nigga+=1
    stop_mins, stop_secs = divmod(nigga, 60)
    stop_hours, stop_mins = divmod(stop_mins, 60)
    stopwatch_display.config(text="{:02d}:{:02d}:{:02d}".format(stop_hours, stop_mins, stop_secs))
    if stopwatch_continued == 1:
        stop_stopwatch_button.config(text="STOP", command=stop_stopwatch)
    startdisplaying_stopwatch = root.after(1000, start_stopwatch, nigga)

    #buttons
start_stopwatch_button = ttk.Button(stopwatch, text="START", command=start_stopwatch)
start_stopwatch_button.pack()

reset_stopwatch_button = ttk.Button(stopwatch, text="RESET", command=reset_stopwatch)
reset_stopwatch_button.pack()

stop_stopwatch_button = ttk.Button(stopwatch, text="STOP", command=stop_stopwatch)
stop_stopwatch_button.pack()
stop_stopwatch_button.state(['disabled'])


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>TIMER<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    #display
description = ttk.Label(timer, text="TIMER SECTION")
description.pack(pady=10)

timer_label = ttk.Label(timer, text="00:00:00", font=("courier", 15))
#timer_label.place(relx=0.5, rely=0.5, anchor="center")

hours_value = IntVar()
entry_hours = ttk.Entry(timer, textvariable=hours_value, width=5)
entry_hours.place(relx=0.3, rely=0.5, anchor="center")
ttk.Label(timer, text="HRS").place()

mins_value = IntVar()
entry_mins= ttk.Entry(timer, textvariable=mins_value, width=5)
entry_mins.place(relx=0.5, rely=0.5, anchor="center")
ttk.Label(timer, text="MINS").place()

seconds_value = IntVar()
entry_seconds = ttk.Entry(timer, textvariable=seconds_value, width=5)
entry_seconds.place(relx=0.7, rely=0.5, anchor="center")
ttk.Label(timer, text="SEC").place()

    #countdown
def ready_entry_box_hours(event):
    hours_value.set("")
def conclude_entry_box_hours(event):
    try:
        if hours_value.get()=="":
            hours_value.set(0)
    except TclError:
        hours_value.set(0)
def ready_entry_box_mins(event):
    mins_value.set("")
def conclude_entry_box_mins(event):
    try:
        if mins_value.get()=="":
            mins_value.set(0)
    except TclError:
        mins_value.set(0)
def ready_entry_box_seconds(event):
    seconds_value.set("")
def conclude_entry_box_seconds(event):
    try:
        if seconds_value.get()=="":
            seconds_value.set(0)
    except TclError:
        seconds_value.set(0)

entry_hours.bind("<FocusIn>", ready_entry_box_hours)
entry_hours.bind("<FocusOut>", conclude_entry_box_hours)

entry_mins.bind("<FocusIn>", ready_entry_box_mins)
entry_mins.bind("<FocusOut>", conclude_entry_box_mins)

entry_seconds.bind("<FocusIn>", ready_entry_box_seconds)
entry_seconds.bind("<FocusOut>", conclude_entry_box_seconds)

def start_timer(total_secs=None):# i used total_Secs = None because i dont know the start value
    timer_label.place(relx=0.5, rely=0.5, anchor="center")
    entry_seconds.place_forget()
    entry_hours.place_forget()
    entry_mins.place_forget()
    #if reset_timer_button.instate(['pressed']):
            #reset_timer()

    if seconds_value.get()==0 and mins_value.get()==0 and hours_value.get()==0:
        pass
    else:
        start_timer_button.config(text="STOP", command=stop_timer)
        global pause_timer, totalSecs_timer
        if total_secs ==None:
            hours, mins, seconds = int(hours_value.get()), int(mins_value.get()), int(seconds_value.get())
            total_secs = hours*3600 + mins*60 + seconds
        if total_secs > -1: 
            mins, secs = divmod(total_secs, 60)
            hours, mins = divmod(mins, 60)
            fuck = "{:02d}:{:02d}:{:02d}".format(hours, mins, secs)
            timer_label.config(text=fuck)
            totalSecs_timer = total_secs
            if reset_timer_button.instate(['pressed']):
                pause_timer = root.after(1000, reset_timer)
            else:
                pause_timer = root.after(1000, start_timer, total_secs-1)

        if total_secs==0:
            print("done")
    
            start_timer_button.state(['!disabled'])
        #sound-playing stuff

def stop_timer():
    root.after_cancel(pause_timer)
    start_timer_button.config(text="CONTINUE", command=continue_timer)
    

def continue_timer(totalSecs_timer_holder=None):
    start_timer_button.config(text="STOP", command=stop_timer)
    global totalSecs_timer
    totalSecs_timer_holder=totalSecs_timer
    if totalSecs_timer_holder ==None:
        hours, mins, seconds = int(hours_value.get()), int(mins_value.get()), int(seconds_value.get())
        totalSecs_timer_holder = hours*3600 + mins*60 + seconds
    if totalSecs_timer_holder > -1: 
        mins, secs = divmod(totalSecs_timer_holder, 60)
        hours, mins = divmod(mins, 60)
        fuck = "{:02d}:{:02d}:{:02d}".format(hours, mins, secs)
        timer_label.config(text=fuck)
        pause_timer = root.after(1000, start_timer, totalSecs_timer_holder-1)
    if totalSecs_timer_holder==0:
        print("done")
        start_timer_button.state(['!disabled'])

def reset_timer():
    timer_label.place_forget()
    entry_hours.place(relx=0.3, rely=0.5, anchor="center")
    entry_seconds.place(relx=0.7, rely=0.5, anchor="center")
    entry_mins.place(relx=0.5, rely=0.5, anchor="center")

    hours_value.set(0)
    mins_value.set(0)
    seconds_value.set(0)

    start_timer_button.config(text="START", command=start_timer)

    #timer_label.config(text="00:00:00")


start_timer_button = ttk.Button(timer, text="START", command=start_timer)
start_timer_button.place(relx=0.5, rely=0.7, anchor="center")

reset_timer_button = ttk.Button(timer, text="RESET", command=reset_timer)
reset_timer_button.place(relx=0.5, rely=0.9, anchor="center")

#ALARM
ttk.Label(alarm, text="This is the alarm section").pack()

root.mainloop()