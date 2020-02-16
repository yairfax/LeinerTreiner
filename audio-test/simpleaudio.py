import simpleaudio

filename = 'output.wav'
wave_obj = simpleaudio.WaveObject.from_wave_file(filename)
play_obj = wave_obj.play()
play_obj.wait_done()  # Wait until sound has finished playing
