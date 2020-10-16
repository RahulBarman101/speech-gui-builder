import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout

class MyApp(App):
    def build(self):
        if self.text is not None:
            return Label(text=self.text)
        else:
            return FloatLayout()

    def make(self,type,t=None):
        if type == 'text':
            self.text = t
        else:
            self.text = None

# MyApp().run()