from tkinter import *
import pyaudio
import wave
import _thread
from scrape import *
from analyze import *
from utils import *
from Plotter import *
from play import *

recording = False
playing = False

def example_gen(expected_taamim):
    expected_notes, expected_timing, pronunc = get_notes(expected_taamim)

    transposed_expected = [i + 70 for i in expected_notes]

    play_taam(transposed_expected)

def examplePlay():
    seferVal = seferMenuVals[seferE.get()]
    expected_taamim, words = getTrop(seferVal, int(perekE.get()), int(pasukE.get()))

    pasuk.config(text=words)
    
    _thread.start_new_thread(example_gen, (expected_taamim,))

def exampleListPlay():
    expected_taamim = taamListE.get().split(',')

    example_gen(expected_taamim)

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

def analyze_gen(expected_taamim):
    given = extract_notes_from_file('output.wav')

    expected_notes, expected_timing, pronunc = get_notes(expected_taamim)

    mean_g = np.mean(given)
    mean_e = np.nanmean(expected_notes)

    offset = mean_g - mean_e
    given_transpose = [i - offset for i in given]

    changed_times = np.linspace(0, 1, len(given_transpose))

    plot_taam(expected_notes, expected_timing, given_transpose, changed_times, midi2note(given[0]), pronunc)

def analyze():
    seferVal = seferMenuVals[seferE.get()]
    expected_taamim, _ = getTrop(seferVal, int(perekE.get()), int(pasukE.get()))

    analyze_gen(expected_taamim)

    

def analyzeList():
    expected_taamim = taamListE.get().split(',')

    analyze_gen(expected_taamim)
    

root = Tk()
root.title("Leiner Treiner")
root.geometry("1000x1000")

app = Frame(root)
app.grid()

# start = Button(app, text="Start Scan", command=start)
example = Button(app, text="Pasuk Example", command=examplePlay)
record = Button(app, text="Record", command=record)
play = Button(app, text="Play Recording", command=startPlay)
stop = Button(app, text="Stop", command=stop)
analyzeTaam = Button(app, text="Analyze Pasuk", command=analyze)
analyzeListButton = Button(app, text="Analyze List", command=analyzeList)
listExampleButton = Button(app, text="List Example", command=exampleListPlay)


w = Label(app, text="Click record to record a new Taam or play to replay recording")
pasuk = Label(app)


# Sefer choice
seferE = StringVar(app)
seferE.set("BeReishit") # initial value

seferMenu = OptionMenu(app, seferE, "BeReishit", "Shemot", "VaYikra", "BaMidbar", "Devarim", "Yehoshua", "Shoftim", "Shmuel1", "Shmuel2", "Melachim1", "Melachim2", "Yeshayahu", "Yirmiyahu", "Yechezkel", "Hoshea", "Yoel", "Amos", "Ovadia", "Yonah", "Michah", "Nachum", "Chabakuk", "Tsefaniah", "Chagai", "Zechariah", "Malachi")
seferMenuVals = {'BeReishit':1,'Shemot':2,'VaYikra':3,'BaMidbar':4,'Devarim':5, "Yehoshua":6, "Shoftim":7, "Shmuel1":8, "Shmuel2":9, "Melachim1":10, "Melachim2":11, "Yeshayahu":12, "Yirmiyahu":13, "Yechezkel":14, "Hoshea":15, "Yoel":16, "Amos":17, "Ovadia":18, "Yonah":19, "Michah":20, "Nachum":21, "Chabakuk":22, "Tsefaniah":23, "Chagai":24, "Zechariah":25, "Malachi":26}

taamListDesc = Label(app, text='Enter a commma-separated list of these words in the entry below:\n'\
    'munach-zarka,zarka,munach-segol,segol,\nmunach-munach-rvii,munach-rvii,rvii,maphakh,pashta,\n'\
    'munach-katon,zakef-katon,zakef-gadol,mercha,\ntipcha,munach-etnachta,etnachta,pazer,\n'\
    'tlisha-ktana,tlisha-gdola,kadma,vazla,azla-geresh,\ngershaim,darga,tvir,yetiv,shalshelet,sof-pasuk\n'\
    'Note that munachim are denoted relative to the\ntaam that follows them, so munach-zarka is the\n'\
    'munach preceding a zarka, not including the zarka')

taamListE = Entry(app)
pasukE = Entry(app)
perekE = Entry(app)

seferL = Label(app, text = "Sefer:")
perekL = Label(app, text = "Perek:")
pasukL = Label(app, text = "Pasuk:")

w.grid(row =1, column = 0, columnspan=5)

record.grid(row = 2, column = 0)
play.grid(row = 2, column = 1)
stop.grid(row = 2, column = 2)
example.grid(row=2,column=3)

seferL.grid(row=3, column=0)
seferMenu.grid(row=3, column=1)
perekL.grid(row=4, column=0)
perekE.grid(row=4, column=1)
pasukL.grid(row=5, column=0)
pasukE.grid(row=5, column=1)

analyzeTaam.grid(row=6, column=0)

pasuk.grid(row=7, column=0, columnspan=5, rowspan=3)

taamListDesc.grid(row=10,column=0, columnspan=5, rowspan=12)

taamListE.grid(row=22, column=0, columnspan=5)

analyzeListButton.grid(row=23, column=0)
listExampleButton.grid(row=23, column=1)


root.mainloop()