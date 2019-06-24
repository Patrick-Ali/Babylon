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
    def __init__(self, cols, rows, **kwargs):
        
        super().__init__(**kwargs)
        ##orientation = 'vertical'
        ##self.row_default_height = Window.height/2
        ##self.row_force_default = True
        self.cols = cols
        self.rows = rows
        print(self.cols)
        print(self.rows)
        ##self.size_hint_y = None
        ##self.minimum_height=.setter('height')
        ##self.size(Window.width, Window.height)
        ##self.size_hint(None, None)

        
class ChatPannel(ScrollView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.do_scroll_x = False
        self.do_scroll_y = True
        self.size_hint = (1, 1)
        self.scroll_type = ['bars', 'content']
        self.size=(Window.width, Window.height)
        
##class MainWindow(Window):
    ##def __init__(self, **kwargs):
        ##super().__init__(self)

        
class ChatPage(BoxLayout):
    
    def __init__(self, **kwargs):
        
        super().__init__(**kwargs)

        self.size_hint_y = None
        ##self.size(Window.width, Window.height)
        ##self.size_hint(None, None)

        self.orientation='vertical'

        ##self.cols = 2
        ##self.rows = 1

        for i in range(25):
            btn = Button(text=str(i),size_hint_y=None, height=40)
            self.add_widget(btn)

        def _on_resize(width, height):
            print(width, height)
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
        #win = MainWindow()
        grid = ChatPageMain(1,3)
        header = ChatPageMain(2,1)
        footer = ChatPageMain(2,1)
        grid.add_widget(header)
        #grid.bind(minimum_height=grid.setter('height'))
        chatPannel = ChatPannel()
        chat = ChatPage()
        chat.bind(minimum_height=chat.setter('height'))
        chatPannel.add_widget(chat)
        grid.add_widget(chatPannel)
        grid.add_widget(footer)
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

    
