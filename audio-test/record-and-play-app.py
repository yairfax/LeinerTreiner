import tkinter
import sys

i = 0
stop = False

def startIt():
	global i
	global stop
	while not stop:
		i = i + 1
		print("i is: ",i)

def stopIt():
	global i
	global stop
	print("stopping")
	stop = True
	i = 0

def exitIt():
	print("Exiting!")
	sys.exit()

top=tkinter.Tk()

startCounterButton=tkinter.Button(top,text="Start", command=startIt)
startCounterButton.pack()

stopCounterButton=tkinter.Button(top,text="Stop", command=stopIt)
stopCounterButton.pack()

exitButton=tkinter.Button(top,text="Exit", command=exitIt)
exitButton.pack()

top.mainloop()