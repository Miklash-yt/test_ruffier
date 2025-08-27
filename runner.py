from kivy.app import App  
from kivy.uix.button import Button
from kivy.properties import BooleanProperty
from kivy.properties import NumericProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.animation import Animation

class Runner(BoxLayout):
    valuee = NumericProperty(0)
    finisheed = BooleanProperty(False)

    def __init__(self, total, steptime, **kwargs):
        super().__init__(**kwargs)
        self.total = total
        self.animation = (Animation(pos_hint={'top' : 0.1}, duration = steptime/2)+Animation(pos_hint={'top': 1.0 }, duration=steptime/2))
        self.btn = Button(text='Приседайте',size_hint=(.4, .3), pos_hint={'top' : 1.0})
        self.add_widget(self.btn)
        self.animation.on_progress = self.next

    def start(self):
        self.valuee = 0
        self.finisheed = False
        self.animation.repeat = True
        self.animation.start(self.btn)

    def next(self, widget, step):
        if step == 1.0:
            self.valuee += 1
            if self.valuee >= self.total:
                self.animation.repeat = False
                self.finisheed = True
               