from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.uix.textinput import TextInput  # allow for ...text input.
from kivy.uix.label import Label

class ChatPageMain(GridLayout):
    def __init__(self, cols, rows, **kwargs):
        
        super().__init__(**kwargs)
        self.cols = cols
        self.rows = rows

        
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
        self.multiline = True#False
        self.focus = True
        #self.use_bubble = True

class BabylonApp(App):
    

   
    def build(self):
        grid = ChatPageMain(1,3)
        print(Window.height)
        ##grid.rows_minimum[0]= 120/5 #(Window.height/100)*20
        header = ChatPageMain(2,1)
        header.size_hint_y = 0.10
        title = Lab("Test")
        title.size_hint_x=0.80
        settings = Button(text="Set",size_hint_x=0.10)
        header.add_widget(title)
        header.add_widget(settings)
        ##header.size_hint(1,1)
        footer = ChatPageMain(2,1)
        footer.size_hint_y = 0.10
        userInput = UserIn("Test Input")
        userInput.size_hint_x=0.80
        enter = Button(text="Sub",size_hint_x=0.10)
        #textinput = TextInput(text='Hello world')
        footer.add_widget(userInput)
        footer.add_widget(enter)
        grid.add_widget(header)
        chatPannel = ChatPannel()
        chat = ChatPage()
        chat.bind(minimum_height=chat.setter('height'))
        chatPannel.add_widget(chat)
        grid.add_widget(chatPannel)
        grid.add_widget(footer)
        return grid
  

if __name__ == '__main__':
    
    BabylonApp().run()

    
