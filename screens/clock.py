
from datetime import datetime, timedelta
import collections
import math
from kivy.uix.screenmanager import Screen
from kivy.clock import Clock
from kivy.clock import Clock
from kivy.uix.label import Label
from kivy.properties import ObjectProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Color, Line

Position = collections.namedtuple('Position', 'x y')

class ClockScreen(Screen):
	pass


class ClockWidget(FloatLayout):


	def __init__(self, **kwargs):
		super(ClockWidget, self).__init__(**kwargs)
		self.now = datetime.now()
		Clock.schedule_interval(self.update_clock, 1)


	def position_on_clock(self, fraction, length):
		center_x = self.size[0]/2
		center_y = self.size[1]/2
		return Position(
			center_x + length * math.sin(2 * math.pi * fraction),
			center_y + length * math.cos(2 * math.pi * fraction),
		)

	def update_clock(self, *args):

		time = datetime.now()
		hands = self.ids["hands"]
		seconds_hand = self.position_on_clock(time.second/60, length=0.45*hands.size[0])
		minutes_hand = self.position_on_clock(time.minute/60+time.second/3600, length=0.40*hands.size[0])
		hours_hand = self.position_on_clock(time.hour/12 + time.minute/720, length=0.35*hands.size[0])
		self.ids["text_hour"].text = "Il est [color=ff0000]" + str(time.hour) + " heures[/color] et [color=00ff00]" + str(time.minute) + " minutes[/color]"

		hands.canvas.clear()
		with hands.canvas:
			Color(0, 0, 1)
			Line(points=[hands.center_x, hands.center_y, seconds_hand.x, seconds_hand.y], width=1, cap="round")
			Color(0, 1, 0)
			Line(points=[hands.center_x, hands.center_y, minutes_hand.x, minutes_hand.y], width=2, cap="round")
			Color(1, 0, 0)
			Line(points=[hands.center_x, hands.center_y, hours_hand.x, hours_hand.y], width=3, cap="round")