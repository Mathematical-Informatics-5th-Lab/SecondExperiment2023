#戻り値 sound_state:音が鳴っているか
def stroke(current_frame, previous_frame):
	current_hand = current_frame.hands.rightmost
	previous_hand = previous_frame.hands.rightmost
	current_position = current_hand.palm_position
	previous_position = previous_hand.palm_position
	ret = previous["sound_state"]
	if current_hand.palm_velocity >= threshold_velocity:
		if current_position[0] >= 0 > previous_position[0]:
			ret = 1
		elif current_position[0] < 0 <= previous_position[0]:
			ret = 0
	return ret