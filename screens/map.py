from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.properties import ListProperty
from kivy_garden.mapview import MapMarkerPopup
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.storage.jsonstore import JsonStore
from kivy.clock import Clock
from functools import partial


class MapScreen(Screen):

	def __init__(self, **kwargs):
		super(MapScreen, self).__init__(**kwargs)
		self.store = JsonStore("json/geographie.json")
		self.countries = self.store.get('countries')
		Clock.schedule_once(self.load_markers, 1)

	def show_dialog(self, *args, **kwargs):
		country=args[0]

		content_popup = BoxLayout(orientation='vertical')
		content_popup.add_widget(Label(text="Capitale : "+country.get("capital_city")))
		content_popup.add_widget(Label(text="Hymne : "+country.get("anthem")))
		content_popup.add_widget(Label(text="Monnaie : "+country.get("currency")))

		popup = Popup(title=country.get("title"),content=content_popup,size_hint=(None, None), size=(400, 400))
		popup.open()


	def load_markers(self, dt):
		for country in self.countries:
			marker_popup = MapMarkerPopup(
				lat=country.get("lat"),
				lon=country.get("lon"),
				source="images/marker.png",
				popup_size=(230,130)
			)
			marker_popup.bind(on_release=partial(self.show_dialog, country))

			self.ids["mapview"].add_marker(marker_popup)
