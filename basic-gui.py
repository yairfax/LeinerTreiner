from tkinter import *
import pyaudio
import wave
import _thread
from scrape import *
from analyze import *
from utils import *
from plotter import *

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


def startPlay():
    if not recording and not playing:
        _thread.start_new_thread(playWav, ())
    else:
        print('Already Playing!')

def playWav():
    global playing
    filename = 'output.wav'

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
    given = extract_notes_from_file(0, 'output.wav')

    expected_taamim = getTrop(1, int(perekE.get()), int(pasukE.get()))

    offset = given[0] - trop_notes[expected_taamim[0]][0]
    given_transpose = [i - offset for i in given]

    expected_notes, expected_timing, pronunc = get_notes(expected_taamim)

    changed_times = np.linspace(0, 1, len(given_transpose))

    plot_taam(expected_notes, expected_timing, given_transpose, changed_times, midi2note(given[0]), pronunc)

root = Tk()
root.title("Leining Treining")
root.geometry("500x500")

app = Frame(root)
app.grid()

# start = Button(app, text="Start Scan", command=start)
record = Button(app, text="Record", command=record)
play = Button(app, text="Play", command=startPlay)
stop = Button(app, text="Stop", command=stop)
analyzeTaam = Button(app, text="Analyze", command=analyze)

w = Label(app, text="Click record to record a new Taam or play to replay recording")

# # start.grid()
record.grid(row = 2, column = 0)
play.grid(row = 2, column = 1)
stop.grid(row = 2, column = 2)

w.grid(row =1, column = 0, columnspan=5)

seferL = Label(app, text = "Sefer:")
perekL = Label(app, text = "Perek:") 
pasukL = Label(app, text = "Pasuk:") 

seferE = Entry(app)
pasukE = Entry(app)
perekE = Entry(app)

seferL.grid(row=3, column=0)
seferE.grid(row=3, column=1)
perekL.grid(row=4, column=0)
perekE.grid(row=4, column=1)
pasukL.grid(row=5, column=0)
pasukE.grid(row=5, column=1)


analyzeTaam.grid(row=6, column=0)

root.mainloop()