from aubio import source, notes, midi2note, pitch
from itertools import groupby
import numpy as np

def extract_notes_from_file(path):
    s = source(path)

    downsample = 1
    samplerate = 44100 // downsample

    win_s = 4096 // downsample # fft size
    hop_s = 512  // downsample # hop size

    samplerate = s.samplerate

    tolerance = 0.8

    # notes_o = notes("default", win_s, hop_s, samplerate)
    pitch_o = pitch("yin", win_s, hop_s, samplerate)
    pitch_o.set_unit("midi")
    pitch_o.set_tolerance(tolerance)

    # print("%8s" % "time","[ start","vel","last ]")

    # total number of frames read
    total_frames = 0
    notes_obj = []
    pitches = []
    confidences = []
    while True:
        samples, read = s()
        # new_note = notes_o(samples)
        pitch_in = pitch_o(samples)[0]
        pitch_in = int(round(pitch_in))
        confidence = pitch_o.get_confidence()
        if confidence < 0.8: pitch_in = 0.
        # print("%f %f %f" % (total_frames / float(samplerate), pitch_in, confidence))
        pitches += [pitch_in]
        confidences += [confidence]
        total_frames += read
        if read < hop_s: break

        # if (new_note[0] != 0):
        #     note_str = ' '.join(["%.2f" % i for i in new_note])
        #     print("%.6f" % (total_frames/float(samplerate)), new_note)
        #     if new_note[0] < 60:
        #         notes_obj.append(int(new_note[0]))
        # total_frames += read
        # if read < hop_s: break

    pitches = list(filter(lambda num: num != 0, pitches))
    pitches = [i[0] for i in groupby(pitches)]

    # print(pitches)
    # print([midi2note(i) for i in pitches])


    std = np.std(pitches)
    mean = np.mean(pitches)
    pitches = list(filter(lambda num: num < mean + std and num > mean - std, pitches))
    
    return pitches


    # print(notes_obj)
    # print([midi2note(i) for i in notes_obj])

    # return notes_obj

# extract_notes_from_file('output.wav')