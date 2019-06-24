from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
#from kivy.uix.gridlayout import GridLayout  # one of many layout structures
from kivy.uix.textinput import TextInput  # allow for ...text input.

#Main Grid - top layer, chat screen, text input
#Child Grid - add to chat screen 4 cols 2 rows,
    ##1 row and column for app, second row and column for user 

class ChatPageMain(GridLayout):
    def __init__(self, **kwargs):
        
        super().__init__(**kwargs)
        ##orientation = 'vertical'
        ##self.row_default_height = Window.height/2
        ##self.row_force_default = True
        self.cols = 1
        self.rows = 2
        ##self.size_hint_y = None
        ##self.minimum_height=.setter('height')
        ##self.size(Window.width, Window.height)
        ##self.size_hint(None, None)

        
class ChatPannel(ScrollView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.do_scroll_x = False
        self.do_scroll_y = True
        self.size_hint = (1, None)
        self.scroll_type = ['bars', 'content']
        self.size=(Window.width, Window.height)
        

class ChatPage(StackLayout):
    
    def __init__(self, **kwargs):
        
        super().__init__(**kwargs)

        self.size_hint_y = None
        ##self.size(Window.width, Window.height)
        ##self.size_hint(None, None)

        #self.orientation='tb-lr'

        ##self.cols = 2
        ##self.rows = 1

        for i in range(25):
            btn = Button(text=str(i),size_hint_y=None, height=40)
            self.add_widget(btn)
        
        ###---Example Code---###
        ##self.cols = 2  # used for our grid

        # widgets added in order, so mind the order.
        ##self.add_widget(Label(text='IP:'))  # widget #1, top left
        ##self.ip = TextInput(multiline=False)  # defining self.ip...
        ##self.add_widget(self.ip) # widget #2, top right

        ##self.add_widget(Label(text='Port:'))
        ##self.port = TextInput(multiline=False)
        ##self.add_widget(self.port)

        ##self.add_widget(Label(text='Username:'))
        ##self.username = TextInput(multiline=False)
        ##self.add_widget(self.username)

class BabylonApp(App):
    

   
    def build(self):
        grid = ChatPageMain()
        #grid.bind(minimum_height=grid.setter('height'))
        chatPannel = ChatPannel()
        chat = ChatPage()
        chat.bind(minimum_height=chat.setter('height'))
        chatPannel.add_widget(chat)
        grid.add_widget(chatPannel)
        return grid
        ##root = StackLayout(orientation='lr-tb')
        ##btn1 = Button(text="Expand")
        ##root.add_widget(btn1)
        ##for i in range(25):
            ##print("Here")
            ##btn = Button(text=str(i), width=40 + i * 5, size_hint=(None, 0.15))
            ##root.add_widget(btn)
        ##layout = GridLayout(cols=2, row_force_default=True, row_default_height=40)
        ##btn1 = Button(text="Expand")
        ##btn1.bind(state=self.rebuild)
        
        ##layout.add_widget(btn1)
        ##layout.add_widget(Button(text='World 1'))
        ##layout.add_widget(Button(text='Hello 2', size_hint_x=None, width=100))
        ##layout.add_widget(Button(text='World 2'))
        ##return layout
        ##pass

if __name__ == '__main__':
    
    BabylonApp().run()

    
