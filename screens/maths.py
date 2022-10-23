import random
import time

from kivy.uix.screenmanager import Screen
from kivy.storage.jsonstore import JsonStore
from kivy.uix.button import Button
from kivy.clock import Clock

class MathsScreen(Screen):

	def __init__(self, **kwargs):
		super(MathsScreen, self).__init__(**kwargs)

	def on_enter(self, *args):
		self.store = JsonStore("json/maths.json")
		self.questions = self.store.get('questions')
		self.ids["box_choices"].clear_widgets()
		self.show_question()

	def send_response(self, instance):
		if instance.text == self.question.get("answer"):
			self.ids["result"].color=(0,1,0,1)
			self.ids["result"].text = "Bravo !"
		else:
			self.ids["result"].color=(1,0,0,1)
			self.ids["result"].text = "Dommage ! La réponse est : " + self.question.get("answer")
		Clock.schedule_once(self.clean_question, 3)

	def clean_question(self, dt):
		self.ids["box_choices"].clear_widgets()
		self.ids["result"].text=""
		self.show_question()


	def show_question(self):
		self.question=self.questions[random.randint(0, len(self.questions)-1)]
		self.ids["question"].text=self.question.get("title")
		for choice in self.question.get("choices"):
			choice_button = Button(
				text=choice,
				font_size='30sp'
			)
			choice_button.bind(on_press=self.send_response)
			self.ids["box_choices"].add_widget(choice_button)