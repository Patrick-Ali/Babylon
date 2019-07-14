from kivy.app import App
from kivy.uix.button import Button
from kivy.core.window import Window

from Babylon_UI import ChatPageMain, ChatPannel, message, ChatPage, Lab, UserIn

from ChatHistory import ChatHistory as ch


class BabylonApp(App):

    """
        Class for building the user interface for the Babylon application,
        inherits from Kivy's App class.
    """
    
    userInput = UserIn("Example: I want a program to add two numbers.")
    chat = ChatPage()# Container for adding messages
    hold = ch()
    chatPannel = ChatPannel()# Container for scrolling
    
    def build(self):

        """
            Method that is called when the class is initalised. Handels building
            the user interface for the app.
        """

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
        #On clicking submit call user_submit function
        submit.bind(on_press=self.user_submit)

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
        """
            Mehtod returns focus to the user input section once the user has
            submited text
        """
        self.userInput.focus = True
        self.userInput.do_backspace(from_undo=False, mode='bkspc')

    def botResponse(self, userInput):
        """
            Method handles getting the response from the bot based on its
            response. Takes the input from the user and calls method to analyse. it
        """
        
        chatLog = self.hold.writeFile("./chat.csv", ("bParoting: " + userInput))

        
    def user_submit(self, _):
        """
            Method manages handeling the user input.
        """
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
        """
            Method is activated when the user press down a key. It listens for
            when the user presses enter and submits the user input for analysis.
        """

        #Allows the user to press enter to submit input
        if keycode == 40:
            self.user_submit(None)
  

if __name__ == '__main__':
    
    BabylonApp().run()
