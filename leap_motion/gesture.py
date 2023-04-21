from leapmotion import Leap
from time import sleep

#from packages.leapmotion import Leap

THUMB = 0
INDEX = 1
MIDDLE = 2
RING = 3
PINKY = 4
controller = Leap.Controller()
controller.enable_gesture(Leap.Gesture.TYPE_SWIPE)
controller.enable_gesture(Leap.Gesture.TYPE_KEY_TAP)
controller.enable_gesture(Leap.Gesture.TYPE_SCREEN_TAP)
controller.enable_gesture(Leap.Gesture.TYPE_CIRCLE)

while not controller.is_connected:
    print(controller.is_connected)
    print('Connecting...')
    sleep(.5)
    pass
print('...Connected!')

while True:
    sleep(.01)
    frame = controller.frame()
    print("a")
    for gesture in frame.gestures():
        if gesture.type == Leap.Gesture.TYPE_SWIPE:
            print("Swipe!")
        if gesture.type == Leap.Gesture.TYPE_KEY_TAP:
            print("Key tap!")
        if gesture.type == Leap.Gesture.TYPE_CIRCLE:
            print("Circle!")    
        if gesture.type == Leap.Gesture.TYPE_SCREEN_TAP:
            print("Screen tap!")        

