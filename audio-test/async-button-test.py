from tkinter import *

running = True  # Global flag

def scanning():
    if running:  # Only do this if the Stop button has not been clicked
        print("hello")

    # After 1 second, call scanning again (create a recursive loop)
    root.after(1000, scanning)

def start():
    """Enable scanning by setting the global flag to True."""
    global running
    running = True

def stop():
    """Stop scanning by setting the global flag to False."""
    global running
    running = False

root = Tk()
root.title("Title")
root.geometry("500x500")

app = Frame(root)
app.grid()

start = Button(app, text="Start Scan", command=start)
stop = Button(app, text="Stop", command=stop)

start.grid()
stop.grid()

root.after(1000, scanning)  # After 1 second, call scanning
root.mainloop()