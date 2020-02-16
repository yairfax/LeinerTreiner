import tkinter
import sys

def doIt():
	print("Button Clicked!")

def exitIt():
	print("Exiting!")
	sys.exit()

top=tkinter.Tk()

bl=tkinter.Button(top,text="Click Me", command=doIt)
bl.pack()

bl2=tkinter.Button(top,text="Exit", command=exitIt)
bl2.pack()

top.mainloop()