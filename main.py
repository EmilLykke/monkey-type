import pytesseract as tesseract
import pyautogui as py
import time
import keyboard
from pynput.keyboard import Listener

# Global variable to control the loop
stop_loop = False

# Coordinates for screenshot
# Change to fit your screen
x1, y1, x2, y2 = 153, 440, 1366, 590

def on_press(key):
    global stop_loop
    try:
        if key.char == 'q':
            print('Stopping...')
            stop_loop = True
            exit()
    except AttributeError:
        pass

def on_release(key):
    # This function is not required for this script
    pass

# Set up and start the listener in a non-blocking manner
listener = Listener(on_press=on_press, on_release=on_release)
listener.start()

time.sleep(2)  # Initial sleep

# Count loop number 
i = 0

# Click the text
py.click(x1+20, y1+20)

while not stop_loop:
    # Screenshot of text
    image = py.screenshot(region=(x1, y1, x2-x1, y2-y1))

    # Image to text
    text = tesseract.image_to_string(image)

    # Replace escapes
    text = text.replace('\n', ' ')
    print(text)

    # Write text
    # py.typewrite(text)
    keyboard.write(text)

    # Offset the image coordinates 
    if i == 0:
        y1+=45
    i+=1

listener.stop()  # Stop the listener once the loop is exited
