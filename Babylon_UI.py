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
        

class message(AnchorLayout):
    def __init__(self, anchor, **kwargs):
        super().__init__(**kwargs)

        
        self.size_hint_y = None

        self.padding = [20,20,20,20]
        
        self.anchor_x = anchor
        self.anchor_y = 'top'
        
class ChatPage(BoxLayout):
    
    def __init__(self, **kwargs):
        
        super().__init__(**kwargs)

        test = ["b ", "b", "u ", "u"]
        
        #Create a scrollable area
        self.size_hint_y = None

        #Allow objects to stack top to bottom
        self.orientation='vertical'

        self.padding = [10,10,10,10]

        hold = ch()
        chat = hold.readFile("./chat.csv")
        
        for msge in range(len(chat)):
            length = len(chat[msge])
            leng_check = round(length/62, 2)

            if leng_check > 1:

                temp = chat[msge][:72]
                hold = chat[msge][72:]
                count = 2
                
                current = chat[msge][0]
                while count > 0:
                    if temp not in test:
                        self.display_msg(temp)
                    
                    if count == 2:
                        if len(hold) > 72:
                            temp = current + hold
                            hold = hold[72:]
                            
                        else:
                           temp = current + hold
                           
                    if len(temp) <= 73:
                        count -= 1
                continue

            if chat[msge] not in test:
                self.display_msg(chat[msge])
            
                        
    def display_msg(self, msg):
        
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
    def __init__(self, text, **kwargs):
        super().__init__(**kwargs)
        self.hint_text = text
        self.multiline = True 
        self.focus = True
        

class BabylonApp(App):
    
    userInput = UserIn("Example: I want a program to add two numbers.")
    chat = ChatPage()# Container for adding messages
    hold = ch()
    chatPannel = ChatPannel()# Container for scrolling
    
    def build(self):

        #Create the base sections for the app
        grid = ChatPageMain(1,3)

        #Create the header section which contains the
        #App title and settings button
        header = ChatPageMain(2,1)
        
        #Set the header to fill 10% of the app height 
        header.size_hint_y = 0.10

        #App title set to 80% width of the header 
        title = Lab("Babylon", 0.80, [255,0,0,0.25], 0)
        #title.size_hint_x = 0.80

        #Settings button set to 10% width of the header  
        settings = Button(text="Settings", size_hint_x = 0.10)

        #Add title and settings button to the app 
        header.add_widget(title)
        header.add_widget(settings)

        #Create the footer section which contains the
        #User input and submit button
        footer = ChatPageMain(2,1)
        footer.size_hint_y = 0.10

        #User input set to 80% width of the footer
        self.userInput.size_hint_x = 0.80

        #Submit button set to 10% width of the footer  
        submit = Button(text="Submit", size_hint_x = 0.10)
        #On clicking submit call send_message function
        submit.bind(on_press=self.send_message)

        #Add user input and submit button to the app
        footer.add_widget(self.userInput)
        footer.add_widget(submit)

        #Add header section to the app
        grid.add_widget(header)

        #Create the section where the chat will appear
        
        

        #Allow the chat to be scrollable
        self.chat.bind(minimum_height=self.chat.setter('height'))

        #Add chat section to the app
        self.chatPannel.add_widget(self.chat)
        grid.add_widget(self.chatPannel)

        #Add footer section to the app
        grid.add_widget(footer)

        #When user presses key call the on_key_down function 
        Window.bind(on_key_down=self.on_key_down)
        
        return grid

    #Reset user input to original state
    def focus_text_input(self, _):
        self.userInput.focus = True
        self.userInput.do_backspace(from_undo=False, mode='bkspc')

    def botResponse(self, userInput):
        #print("Hello")
        chatLog = self.hold.writeFile("./chat.csv", ("bParoting: " + userInput))

        
    def send_message(self, _):
        
        #Refresh the chat
        chatLog = self.hold.writeFile("./chat.csv", ('u' + self.userInput.text))
        self.botResponse(self.userInput.text)
        self.chatPannel.remove_widget(self.chat)
        self.chat = ChatPage()
        self.chat.bind(minimum_height=self.chat.setter('height'))
        self.chatPannel.add_widget(self.chat)
        
        #Set the user input to original state
        self.userInput.text = ''
        Clock.schedule_once(self.focus_text_input, 0.1)
        
    def on_key_down(self, instance, keyboard, keycode, text, modifiers):

        #Allows the user to press enter to submit input
        if keycode == 40:
            self.send_message(None)
  

if __name__ == '__main__':
    
    BabylonApp().run()

    
