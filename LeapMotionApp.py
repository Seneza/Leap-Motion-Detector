import Leap
import sys
import thread
import time
from Leap import CircleGesture
from Leap import KeyTapGesture
from Leap import ScreenTapGesture
from Leap import SwipeGesture

class LeapMotionListener(Leap.Listener):
	finger_names = ["Thumb", "Index", "Middle", "Ring", "Pinky"]
	bone_names = ["Metacarpal", "Proximal", "Intermediate", "Distal"]
	state_names = ["STATE_INVALID", "STATE_START", "STATE_UPDATE", "STATE_END"]

	def on_init(self, controller):
		print("Initialized Listener")

	def on_connect(self, controller):
		print("Motion sensor connected!")

		controller.enable_gesture(Leap.Gesture.TYPE_CIRCLE);
		controller.enable_gesture(Leap.Gesture.TYPE_KEY_TAP);
		controller.enable_gesture(Leap.Gesture.TYPE_SCREEN_TAP);
		controller.enable_gesture(Leap.Gesture.TYPE_SWIPE);

	def on_disconnect(self, controller):
		print("Exited")

	def on_frame(self, controller):
		frame = controller.frame()

		for hand in frame.hands:
			hand_type = "Left Hand " if hand.is_left else "Right Hand"
			print(hand_type + " Hand ID: " + str(hand.id) + " Palm Position: " + str(hand.palm_position))
			normal = hand.palm_normal
			direction = hand.direction
			print("Pitch: " + str(direction.pitch * Leap.RAD_TO_DEG) + " Roll: " + str(normal.roll * Leap.RAD_TO_DEG) + " Yaw: " + str(direction.yaw * Leap.RAD_TO_DEG))


def main():
	listener = LeapMotionListener()
	controller = Leap.Controller()

	controller.add_listener(listener)
	print("Press Enter to quit")

	try:
		sys.stdin.readline()
	except KeyboardInterrupt:
		pass
	finally:
		controller.remove_listener(listener)

if __name__ == "__main__":
	main()