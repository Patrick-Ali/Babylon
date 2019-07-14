from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.uix.anchorlayout import AnchorLayout
from kivy.graphics import Color, Rectangle, RoundedRectangle

from ChatHistory import ChatHistory as ch


class ChatPageMain(GridLayout):
    '''
        Create the layout for the app,
        constructor takes the number of columns (cols) and rows (rows)
        the app should be. Class inherits from Kivy's GridLayout class
    '''
    
    def __init__(self, cols, rows, **kwargs):
        
        super().__init__(**kwargs)
        self.cols = cols
        self.rows = rows
        
        
class ChatPannel(ScrollView):
    '''
        Create the scrollable area for the chat,
        set the scrollable area to be operable on desktop and mobile (scroll_type).
        Class inherits from Kivy's ScrollView class.
    '''
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.do_scroll_x = False
        self.do_scroll_y = True
        self.size_hint = (1, 1)
        self.scroll_type = ['bars', 'content']
        self.size=(Window.width, Window.height)
        

class message(AnchorLayout):

    '''
        Create a section for the message to be placed in which can be placed in the
        scrollable area. Constructor takes the side of the anchor the message should
        be attached to (anchor). Class inherits from Kivy's AnchorLayout class.
    '''
    
    def __init__(self, anchor, **kwargs):
        super().__init__(**kwargs)

        
        self.size_hint_y = None

        self.padding = [20,20,20,20]
        
        self.anchor_x = anchor
        self.anchor_y = 'top'
        
class ChatPage(BoxLayout):
    
    def __init__(self, **kwargs):
        
        super().__init__(**kwargs)

        # Test for the begining of the message and
        #if the message is empty
        test = ["b ", "b", "u ", "u"]
        
        #Create a scrollable area
        self.size_hint_y = None

        #Allow objects to stack top to bottom
        self.orientation='vertical'

        self.padding = [10,10,10,10]

        hold = ch()
        chat = hold.readFile("./chat.csv")

        #Load chat history
        for msge in range(len(chat)):

            #Check the length of the message to prevent clipping
            length = len(chat[msge])
            leng_check = round(length/72, 2)

            # If message length greater than 72
            if leng_check > 1:

                #Chat message upto the 72nd character
                temp = chat[msge][:72]
                #Chat message after 72nd character
                hold = chat[msge][72:]
                
                count = 2

                # Is it the bot or user
                current = chat[msge][0]

                # While the message remains greater than 72 and text needs
                # to be printed
                while count > 0:
                    
                    #Check the message is empty, if not display message
                    if temp not in test:
                        self.display_msg(temp)
                        
                    #If the message is above 72 characters
                    if count == 2:
                        if len(hold) > 72:
                            temp = current + hold
                            hold = hold[72:]
                            
                        else:
                           temp = current + hold

                    #When last part of message needs to be printed
                    if len(temp) <= 73:
                        count -= 1
                continue

            #Check the message is empty, if not display message
            if chat[msge] not in test:
                self.display_msg(chat[msge])
            
                        
    def display_msg(self, msg):
        """
            Method manages displaying a message on screen
            and determing whether it is Babylon or the User. 
        """
        if msg[0] == 'b':
            msge = message("left")
            botHold = Lab(msg[1:], 0.40,[25,181,254,0.50], 10)
            msge.add_widget(botHold)
            self.add_widget(msge)
            
        elif msg[0] == 'u':
            msge = message("right")
            user = Lab(msg[1:], 0.40,[0,0,255,0.50], 10)
            msge.add_widget(user)
            self.add_widget(msge)
                


class Lab(Label):
    """
        Creates a label for the text to be displayed in.
        Inherits from Kivy's Label class.
        Initialisation method takes the text to display, width
        of the label, colour of the label, and the roundness of
        the label.
    """
    colour = [0,0,0,0.25]
    corner = 0
    def __init__(self, text, width, RGBA, corner, **kwargs):
        super().__init__(**kwargs)
        self.text = text
        self.size_hint_x = width
        self.colour = RGBA
        self.corner = corner
        self.text_size = (250, None)
        self.size = self.texture_size

    def on_size(self, *args):
        """
            When the canvas is resized this method is called and adpats the
            rectangles that sit behined the labels to give them their colours.
        """
        self.canvas.before.clear()
        with self.canvas.before:
            Color(self.colour[0], self.colour[1], self.colour[2], self.colour[3])
            
            if self.corner > 0:
                temp = (self.size[0]+10, self.size[1]+10)
                temp_pos = (self.pos[0]-5, self.pos[1]-5)
                RoundedRectangle(pos=temp_pos, size=temp, corner_radius = self.corner)
            else:
                Rectangle(pos=self.pos, size=self.size)


class UserIn(TextInput):
    '''
        Create the area for the user to enter their information.
        Constructor takes the example input as an argument (text).
        Allows for multiline input and sets focus onto area when app is run.
        Class inherits from Kivy's TextInput.
    '''
    def __init__(self, text, **kwargs):
        super().__init__(**kwargs)
        self.hint_text = text
        self.multiline = True 
        self.focus = True
        

    
