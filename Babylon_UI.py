from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.uix.image import Image

class ChatPageMain(GridLayout):
    def __init__(self, cols, rows, **kwargs):
        
        super().__init__(**kwargs)
        self.cols = cols
        self.rows = rows

class Symbols(Image):
    
    def __init__(self, source, **kwargs):
        super().__init__(**kwargs)
        self.source = source
        self.y = self.parent.y + self.parent.height - 250
        
        
class ChatPannel(ScrollView):
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.do_scroll_x = False
        self.do_scroll_y = True
        self.size_hint = (1, 1)
        self.scroll_type = ['bars', 'content']
        self.size=(Window.width, Window.height)
        


        
class ChatPage(BoxLayout):
    
    def __init__(self, **kwargs):
        
        super().__init__(**kwargs)
        
        #Create a scrollable area
        self.size_hint_y = None

        #Allow objects to stack top to bottom
        self.orientation='vertical'


        for i in range(25):
            btn = Button(text=str(i),size_hint_y=None, height=40)
            self.add_widget(btn)

class Lab(Label):
     def __init__(self, text, **kwargs):
        super().__init__(**kwargs)
        self.text = text

class UserIn(TextInput):
    def __init__(self, text, **kwargs):
        super().__init__(**kwargs)
        self.hint_text = text
        self.multiline = True #False 
        self.focus = True
        

class BabylonApp(App):
    
    userInput = UserIn("I want a program to add two numbers")
   
    def build(self):
        grid = ChatPageMain(1,3)
        print(Window.height)
                header = ChatPageMain(2,1)
        header.size_hint_y = 0.10
        title = Lab("Babylon")
        title.size_hint_x=0.80
        settings = Button(text="Settings", size_hint_x=0.10)
        header.add_widget(title)
        header.add_widget(settings)
        footer = ChatPageMain(2,1)
        footer.size_hint_y = 0.10
        self.userInput.size_hint_x=0.80
        enter = Button(text="Submit",size_hint_x=0.10)
        enter.bind(on_press=self.send_message)
        footer.add_widget(self.userInput)
        footer.add_widget(enter)
        grid.add_widget(header)
        chatPannel = ChatPannel()
        chat = ChatPage()
        chat.bind(minimum_height=chat.setter('height'))
        chatPannel.add_widget(chat)
        grid.add_widget(chatPannel)
        grid.add_widget(footer)
        Window.bind(on_key_down=self.on_key_down)
        return grid
    
    def focus_text_input(self, _):
        self.userInput.focus = True
        self.userInput.do_backspace(from_undo=False, mode='bkspc')
        
    def send_message(self, _):
        print(self.userInput.text)
        self.userInput.text = ''
        Clock.schedule_once(self.focus_text_input, 0.1)
        
    def on_key_down(self, instance, keyboard, keycode, text, modifiers):

        #Allows the user to press enter to submit input
        if keycode == 40:
            self.send_message(None)
  

if __name__ == '__main__':
    
    BabylonApp().run()

    
