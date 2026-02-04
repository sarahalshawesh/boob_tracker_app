from kivy.app import App 
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout 

class BoobTracker(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='horizontal')
        left_boob = Button(text="left boob")
        right_boob = Button(text="right boob")
        layout.add_widget(left_boob)
        layout.add_widget(right_boob)
        self.add_widget(layout)

class BoobApp(App):
    def build(Self):
        return BoobTracker()

if __name__ == "__main__":
    BoobApp().run()