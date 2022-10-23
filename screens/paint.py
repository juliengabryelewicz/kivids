import random
from datetime import datetime, timedelta
from kivy.uix.screenmanager import Screen
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.graphics import Color, Line

class PaintScreen(Screen):

	def clear_canvas(self):
		self.ids["paint_widget"].canvas.clear()
	pass

class PaintWidget(Widget):

	def on_touch_down(self, touch):
		try:
			color = (random.random(), 1, 1)
			with self.canvas:
				Color(*color, mode='hsv')
				d = 30.
				touch.ud['line'] = Line(points=(touch.x, touch.y))
		except Exception as err:
			pass

	def on_touch_move(self, touch):
		try:
			touch.ud['line'].points += [touch.x, touch.y]
		except Exception as err:
			pass