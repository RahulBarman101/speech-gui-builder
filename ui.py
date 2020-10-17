import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout

class MakeLayout:
    '''
    The main layout class to add and remove widgets
    creates the layout and sets the widgets in place
    '''
    def __init__(self):
        self.layout = FloatLayout()
    
    def make(self):
        return self.layout

    def add_widget(self,widget,txt):
        '''
        method to add the widget
        params:
        widget -> string: the type of widget to make
        txt -> string: the text of that widget
        '''
        if widget == 'button':
            if txt:
                widget = Button(text=txt,size_hint=(0.3,0.2),pos_hint={'x':1-0.3,'top':1})
            else:
                widget = Button(text="Submit",size_hint=(0.3,0.2),pos_hint={'x':1-0.3,'top':1})
        else:
            widget = Label(text=txt)

        self.layout.add_widget(widget)

    
class MyApp(App):
    '''
    The main class to call for building the GUI
    '''
    def build(self):
        return self.ml.make()

    def make(self,type,t=None):
        '''
        The make function to call to make various kinds of widgets
        params:
        type -> string: The widget type
        t -> string: The text string to display on the widget
        '''
        self.ml = MakeLayout()
        self.ml.add_widget(type,t)

# MyApp().run()