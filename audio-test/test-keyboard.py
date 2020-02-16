import keyboard  # using module keyboard
while True:  # making a loop
    print('test')
    try:  # used try so that if user pressed other than the given key error will not be shown
        if keyboard.is_pressed(' '):  # if key 'q' is pressed 
            print('You Pressed A Key!')
            break  # finishing the loop
    except:
        # keyboard.wait('esc')
        # print('not done')
        break  # if user pressed a key other than the given key the loop will break