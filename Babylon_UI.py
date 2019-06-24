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

        

class BabylonApp(App):
    

   
    def build(self):
        grid = ChatPageMain(1,3)
        header = ChatPageMain(2,1)
        footer = ChatPageMain(2,1)
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

    
