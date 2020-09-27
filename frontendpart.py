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

        self.add_widget(AsyncImage(source="https://img.pngio.com/assistance-png-5-png-image-assistance-png-800_600.png"))#image we need to present
        self.bottom_layout=FloatLayout(size=(600,600))
        
        #button to start meeting reminder.
        self.meeting=Button(
            text="Meeting Reminder",
            background_color=(1,0.5,0.5,2),
            size_hint=(0.2,0.2),
            pos_hint={'x':0.3,'y':0.5}
             )

        self.meeting.bind(on_press=self.meeting_callback)
        self.bottom_layout.add_widget(self.meeting)
        
        #button to start halthcare(if we add that or any other thing we can ad here)
        self.medicine=Button(
            text="Medicine Reminder",
            background_color=(1,0.5,0.5,2),
            size_hint=(0.2,0.2),
            pos_hint={'x':0.5,'y':0.5}
             )

        self.medicine.bind(on_press=self.medicine_callback)
        self.bottom_layout.add_widget(self.medicine)

        self.add_widget(self.bottom_layout)
    
    #this is function for meeting reminder one,add here you backend code that need to be perform
    def meeting_callback(self,instance):
       
    #this is for medicine one
    def medicine_callback(self,instance):
        

class MykivyApp(App):

    def build(self):
        Window.clearcolor=(1,1,1,1)
        return myLayout()
if __name__=='__main__':
       MykivyApp().run()
