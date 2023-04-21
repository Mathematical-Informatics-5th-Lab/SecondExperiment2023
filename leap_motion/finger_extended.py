from leapmotion import Leap

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
    hands = frame.hands
    if len(hands)==0:
        print("no hands")
    else:
        hand = hands[0]
        fingers = hand.fingers
        extended = []
        for finger in fingers:
            extended.append(finger.is_extended)
        print(extended)
