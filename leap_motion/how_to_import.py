from leapmotion import Leap

print("Hello World!")

from time import sleep

#from packages.leapmotion import Leap

THUMB = 0
INDEX = 1
MIDDLE = 2
RING = 3
PINKY = 4
controller = Leap.Controller()

while not controller.is_connected:
    print(controller.is_connected)
    print('Connecting...')
    sleep(.5)
    pass
print('...Connected!')

while True:
    sleep(.01)
    frame = controller.frame()

    pos_thumb = frame.fingers[THUMB].tip_position
    pos_index = frame.fingers[INDEX].tip_position

    print(pos_thumb.distance_to(pos_index))
