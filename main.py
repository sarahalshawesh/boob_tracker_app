from kivy.app import App 
from kivy.properties import StringProperty
from kivy.uix.floatlayout import FloatLayout 

class BoobTracker(FloatLayout):
    last_used = StringProperty("left")

    def left_tap(self):
        self.last_used = "left"
    
    def right_tap(self):
        self.last_used = "right"


class BoobApp(App):
    def build(self):
        return BoobTracker()

if __name__ == "__main__":
    BoobApp().run()