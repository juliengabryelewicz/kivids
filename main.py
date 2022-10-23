#!/usr/bin/env python3

import locale

from kivy.app import App
from kivy.config import Config
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager
from screens.clock import ClockScreen
from screens.color import ColorScreen
from screens.map import MapScreen
from screens.maths import MathsScreen
from screens.paint import PaintScreen



Config.set('graphics', 'width', '1024')
Config.set('graphics', 'height', '600')
Config.write()

locale.setlocale(locale.LC_ALL, "")

class KividsWidget(BoxLayout):
	pass

class MenuWidget(BoxLayout):
	pass
		
class ScreenWidget(ScreenManager):
	pass

class KividsApp(App):

	def build(self):
		return KividsWidget()


if __name__=="__main__":
	KividsApp().run()
