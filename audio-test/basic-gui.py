from tkinter import *
import pyaudio
import wave
import _thread

recording = False
playing = False

def stop():
    global playing
    global recording
    recording = False
    playing = False

def record():
    if not recording and not playing:
        _thread.start_new_thread(recordWav, ())
    else:
        print('Already Recording!')


def recordWav():
    global recording
    chunk = 1024  # Record in chunks of 1024 samples
    sample_format = pyaudio.paInt16  # 16 bits per sample
    channels = 2
    fs = 44100  # Record at 44100 samples per second
    seconds = 30
    filename = "output.wav"

    p = pyaudio.PyAudio()  # Create an interface to PortAudio

    print('Recording')

    stream = p.open(format=sample_format,
                    channels=channels,
                    rate=fs,
                    frames_per_buffer=chunk,
                    input=True)

    frames = []  # Initialize array to store frames

    # Store data in chunks for 3 seconds
    recording = True
    for i in range(0, int(fs / chunk * seconds)):
        data = stream.read(chunk)
        frames.append(data)
        if not recording:
            break

    # Stop and close the stream 
    stream.stop_stream()
    stream.close()
    # Terminate the PortAudio interface
    p.terminate()

    print('Finished recording')

    # Save the recorded data as a WAV file
    wf = wave.open(filename, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(sample_format))
    wf.setframerate(fs)
    wf.writeframes(b''.join(frames))
    wf.close()

def examplePlay():
    if not recording and not playing:
        _thread.start_new_thread(playWav, ('example.wav',))
    else:
        print('Already Playing!')

def startPlay():
    if not recording and not playing:
        _thread.start_new_thread(playWav, ('output.wav',))
    else:
        print('Already Playing!')

def playWav(filename):
    global playing

    # Set chunk size of 1024 samples per data frame
    chunk = 1024  

    # Open the sound file 
    wf = wave.open(filename, 'rb')

    # Create an interface to PortAudio
    p = pyaudio.PyAudio()

    # Open a .Stream object to write the WAV file to
    # 'output = True' indicates that the sound will be played rather than recorded
    stream = p.open(format = p.get_format_from_width(wf.getsampwidth()),
                    channels = wf.getnchannels(),
                    rate = wf.getframerate(),
                    output = True)

    # Read data in chunks
    data = wf.readframes(chunk)

    # Play the sound by writing the audio data to the stream
    playing = True
    while data and playing:
        stream.write(data)
        data = wf.readframes(chunk)

    # Close and terminate the stream
    stream.close()
    p.terminate()

def analyze():
    seferVal = seferMenuVals[seferE.get()]
    perekVal = int(perekE.get())
    pasukVal = int(pasukE.get())

    print("Sefer:",seferVal," Perek:", perekVal, " Pasuk:", pasukVal)

def analyzeList():
    taamList = taamListE.get().split(',')
    for i in taamList:
        print(i)

root = Tk()
root.title("Leining Treining")
root.geometry("500x500")

app = Frame(root)
app.grid()

# start = Button(app, text="Start Scan", command=start)
example = Button(app, text="Example", command=examplePlay)
record = Button(app, text="Record", command=record)
play = Button(app, text="Play Recording", command=startPlay)
stop = Button(app, text="Stop", command=stop)
analyzeTaam = Button(app, text="Analyze Pasuk", command=analyze)
analyzeListButton = Button(app, text="Analyze List", command=analyzeList)

w = Label(app, text="Click record to record a new Taam or play to replay recording")

# Sefer choice
seferE = StringVar(app)
seferE.set("BeReishit") # initial value

seferMenu = OptionMenu(app, seferE, "BeReishit", "Shemot", "VaYikra", "BaMidbar", "Devarim")
seferMenuVals = {'BeReishit':1,'Shemot':2,'VaYikra':3,'BaMidbar':4,'Devarim':5}

taamListDesc = Label(app, text='Enter a commma-separated list of these words in the entry below:\n'\
    'munach-zarka,zarka,munach-segol,segol,\nmunach-munach-rvii,munach-rvii,rvii,maphakh,pashta,\n'\
    'munach-katon,zakef-katon,zakef-gadol,mercha,\ntipcha,munach-etnachta,etnachta,pazer,\n'\
    'tlisha-ktana,tlisha-gdola,kadma,vazla,azla-geresh,\ngershaim,darga,tvir,yetiv,shalshelet,sof-pasuk')

# # start.grid()
record.grid(row = 2, column = 0)
play.grid(row = 2, column = 1)
stop.grid(row = 2, column = 2)
example.grid(row=2,column=3)
analyzeListButton.grid(row=14, column=0)

w.grid(row =1, column = 0, columnspan=5)
taamListDesc.grid(row=6,column=0, columnspan=5, rowspan=7)

seferL = Label(app, text = "Sefer:")
perekL = Label(app, text = "Perek:") 
pasukL = Label(app, text = "Pasuk:") 

taamListE = Entry(app)
pasukE = Entry(app)
perekE = Entry(app)
# taamListE = Entry(app)

seferL.grid(row=3, column=0)
seferMenu.grid(row=3, column=1)
perekL.grid(row=4, column=0)
perekE.grid(row=4, column=1)
pasukL.grid(row=5, column=0)
pasukE.grid(row=5, column=1)
taamListE.grid(row=13, column=0, columnspan=5)


analyzeTaam.grid(row=6, column=0)

root.mainloop()