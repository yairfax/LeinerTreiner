import numpy as np
import taamim_torah
import taamim_haftorah
import math

def get_notes(taamim, is_haf):
    notes = []
    timing = []
    pronunc = []

    trop_notes = taamim_torah.trop_notes if not is_haf else taamim_haftorah.trop_notes
    trop_name = taamim_torah.trop_name if not is_haf else taamim_haftorah.trop_name

    for taam in taamim:
        notes += trop_notes[taam]
        notes += [np.nan]

        timing += [1 for i in range(len(trop_notes[taam]))]
        timing += [1]

        pronunc += trop_name[taam]
        pronunc += [""]
    
    notes = notes[:-1]
    timing = [i for i in range(len(timing))]
    timing = timing[:-1]
    timing = [i/len(timing) for i in timing]
    pronunc = pronunc[:-1]

    return notes, timing, pronunc

def grad_descent(g_notes, g_times, e_notes, e_times):
    times = g_times

    for i in range(100):
        grad = np.array([0 for i in range(len(times))])
        for i in range(len(times)):
            e_note, e_time, dist = closest_point(e_notes, e_times, g_notes[i], times[i])
            grad[i] = -times[i]*(1/dist) if dist != 0 else 0
        times -= .01*grad
        # print(grad)

    return times

def closest_point(e_notes, e_times, g_note, g_time):
    closest_note = e_notes[0]
    closest_time = e_times[0]
    dist = euclid(e_notes[0], g_note, e_times[0], g_time)
    print(e_notes)
    print(e_times)
    print(g_note)
    print(g_time)
    # print("%f %f %f %f" % (e_notes[0], g_note, e_times[0], g_time))
    for i in range(1, len(e_notes)):
        if e_notes[i] != np.nan:
            temp_dist = euclid(e_notes[i], g_note, e_times[i], g_time)
            if temp_dist < dist:
                closest_note = e_notes[i]
                closest_time = e_times[i]
                dist = temp_dist
                print("hello")
    
    print("%f %f %f" % (g_note, g_time, dist))
    return closest_note, closest_time, dist

def euclid(x1, x0, y1, y0):
    return math.sqrt((x1-x0)**2 + (y1-y0)**2)
