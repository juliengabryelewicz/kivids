from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.properties import ListProperty


class RectangleLabel(Label):
	background_color = ListProperty((0,0,0,1))

class ColorScreen(Screen):

	def __init__(self, **kwargs):
		super(ColorScreen, self).__init__(**kwargs)
		self.selectedColors = []

	def add_color(self, color):
		label = RectangleLabel(background_color=(color[0]/255, color[1]/255, color[2]/255, 1))
		self.ids["choice_colors"].add_widget(label)
		self.selectedColors.append(color)
		self.mix_colors()

	def clean_colors(self):
		self.ids["result_colors"].clear_widgets()
		self.ids["choice_colors"].clear_widgets()
		self.selectedColors = []

	def mix_colors(self):
		self.ids["result_colors"].clear_widgets()
		r = g = b = 0
		rgb_scale = 1
		for item in self.selectedColors:
			r += item[0]/255
			g += item[1]/255
			b += item[2]/255
		ratio = max(r, g, b)
		if ratio > rgb_scale:
			ratio = float(rgb_scale) / ratio
			r *= ratio
			g *= ratio
			b *= ratio
		label = RectangleLabel(text=" ", background_color=(r, g, b, 1))
		self.ids["result_colors"].add_widget(label)