import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import *
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import *
from kivy.uix.image import AsyncImage
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout

class myLayout(GridLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.cols=1

        self.add_widget(AsyncImage(source="https://img.pngio.com/assistance-png-5-png-image-assistance-png-800_600.png"))
        self.bottom_layout=FloatLayout(size=(600,600))

        self.lets_start=Button(
            text="Lets Start",
            background_color=(1,0.5,0.5,2),
            size_hint=(0.2,0.2),
            pos_hint={'x':0.3,'y':0.5}
             )

        self.lets_start.bind(on_press=self.lets_start_callback)
        self.bottom_layout.add_widget(self.lets_start)

        self.close=Button(
            text="Close",
            background_color=(1,0.5,0.5,2),
            size_hint=(0.2,0.2),
            pos_hint={'x':0.5,'y':0.5}
             )

        self.close.bind(on_press=self.close_callback)
        self.bottom_layout.add_widget(self.close)

        self.add_widget(self.bottom_layout)

    def lets_start_callback(self,instance):
        x=input("give")
        print(x)

    def close_callback(self,instance):
        print("close")

class MykivyApp(App):

    def build(self):
        Window.clearcolor=(1,1,1,1)
        return myLayout()
if __name__=='__main__':
       MykivyApp().run()
