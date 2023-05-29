import json
from leapmotion import Leap
from time import sleep

THUMB = 0
INDEX = 1
MIDDLE = 2
RING = 3
PINKY = 4
controller = Leap.Controller()

threshold_velocity = 0

def code_id(frame):
    hands = frame.hands
    if len(hands) != 1:
        return -1
    else:
        fingers = hands[0].fingers
        sum = 0
        for finger in fingers:
            if finger.is_extended:
                sum += 1
        return sum

def norm(v):
	ret = 0
	for i in range(3):
		ret += v[i] ** 2
	return ret

def stroke(current_frame, previous):
	current_hand = current_frame.hands.rightmost
	current_position = current_hand.palm_position
	ret = previous["is_stroke"]
	if norm(current_hand.palm_velocity) >= threshold_velocity:
		if current_position[0] >= 0:
			ret = 1
		elif current_position[0] < 0:
			ret = 0
	return ret

def palm_distance(frame):
	hand = frame.hands.rightmost
	return hand.palm_position[1]

def tip_distance(frame):
    pos_thumb = frame.fingers[0].tip_position
    pos_index = frame.fingers[1].tip_position
    return pos_thumb.distance_to(pos_index)

controller.set_policy_flags(Leap.Controller.POLICY_BACKGROUND_FRAMES)
while True:
    if controller.is_connected:
        current_frame = controller.frame()
        previous_frame = controller.frame(1)
        current_hand = current_frame.hands.rightmost
        with open('./test.json') as f:
            previous = json.load(f)
        current = {}
        #####
        current["fingers"] = code_id(current_frame)
        current["is_stroke"] = stroke(current_frame,previous)
        current["palm_distance"] = palm_distance(current_frame)
        # current["tip_distance"] = tip_distance(current_frame)
        #####
        print(current)
        json_file = open('./test.json', mode="w")
        json.dump(current, json_file)
        json_file.close()
    sleep(.001)
