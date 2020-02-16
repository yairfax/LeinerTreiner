from aubio import source, notes, midi2note
import numpy as np

def extract_notes_from_file(start_note, path):
    s = source(path)

    downsample = 1
    samplerate = 44100 // downsample

    win_s = 4096 // downsample # fft size
    hop_s = 512  // downsample # hop size

    samplerate = s.samplerate

    tolerance = 0.8

    notes_o = notes("default", win_s, hop_s, samplerate)

    print("%8s" % "time","[ start","vel","last ]")

    # total number of frames read
    total_frames = 0
    notes_obj = []
    while True:
        samples, read = s()
        new_note = notes_o(samples)
        if (new_note[0] != 0):
            note_str = ' '.join(["%.2f" % i for i in new_note])
            print("%.6f" % (total_frames/float(samplerate)), new_note)
            if new_note[0] < 60:
                notes_obj.append(int(new_note[0]))
        total_frames += read
        if read < hop_s: break

    return notes_obj
