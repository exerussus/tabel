from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.config import Config


Config.set('graphics', 'resizable', 0)
Config.set('graphics', 'width', 1200)
Config.set('graphics', 'height', 800)
Config.write()

class TabelApp(App):
    pass

TabelApp().run()

