from kivy.app import App 
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout 

class BoobTracker(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
    def on_kv_post(self, base_widget):
        self.ids.left_button.text = "left boob"
        self.ids.right_button.text = "right boob"
        

class BoobApp(App):
    def build(Self):
        return BoobTracker()

if __name__ == "__main__":
    BoobApp().run()