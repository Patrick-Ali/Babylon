from kivy.app import App
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.clock import Clock
from Rules import Rules

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
    rules = Rules()
    req = ''
    count_pro = 1
    file_name = ""
    funcs = []
    func_counting = 0
    
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
        if self.count_pro == 2:
            p1 = "bPlease provide smaple input, e.g. for:"
            p2 = "b'I want a program to add two numbers togther.'"
            p3 = "bthe input would be '1, 2'. Use comma (,) to denote each input."
            #self.count_pro += 1
            chatLog = self.hold.writeFile("./chat.csv", p1)
            chatLog = self.hold.writeFile("./chat.csv", p2)
            chatLog = self.hold.writeFile("./chat.csv", p3)
            self.refresh_chat()
            self.count_pro += 1
            print(self.count_pro)
        elif self.count_pro == 4 or self.count_pro == 6 or self.count_pro == 7:
            if self.file_name == "":
                print("Here F")
                f_name = "bWhat do you want to call the program?"
                #self.file_name = f_name
                chatLog = self.hold.writeFile("./chat.csv", f_name)
                self.refresh_chat()
                self.count_pro += 1 #Go from 4 to 5
            else:
                print("Count ", self.count_pro)
                if self.count_pro == 6:
                    self.count_pro = 7
                func_name = "bWhat do you want to call the function?"
                chatLog = self.hold.writeFile("./chat.csv", func_name)
                self.refresh_chat()
        elif self.count_pro == 8:
            write = "bDo you want to write the program to file?"
            chatLog = self.hold.writeFile("./chat.csv", write)
            self.refresh_chat()
            self.count_pro += 1

        #chatLog = self.hold.writeFile("./chat.csv", ("bParoting: " + userInput))
        # temp_count = 0
        #while temp_count < rules.func_count:

    def refresh_chat(self):
        self.chatPannel.remove_widget(self.chat)
        self.chat = ChatPage()
        self.chat.bind(minimum_height=self.chat.setter('height'))
        self.chatPannel.add_widget(self.chat)

    def user_submit(self, _):
        """
            Method manages handeling the user input.
        """
        #Refresh the chat
        chatLog = self.hold.writeFile("./chat.csv", ('u' + self.userInput.text))
        if self.count_pro == 1:
            self.rules.sentence_break(self.userInput.text)
            self.req = self.userInput.text
            self.count_pro += 1
            self.refresh_chat()
            self.botResponse(self.userInput.text)
            print("Func count ", self.rules.func_count)
        elif self.count_pro == 3:
            params_split = self.userInput.text.split(",")
            self.rules.sample_param = []
            self.rules.params_func = []
            for param in params_split:
                self.rules.sample_param.append(param)
            print("Params ", self.rules.sample_param)
            self.count_pro += 1
            self.refresh_chat()
            self.botResponse(self.userInput.text)
        elif self.count_pro == 5:
            if self.file_name == "":
                self.rules.f_name = self.userInput.text
                self.file_name = self.userInput.text
                print("File name: ", self.rules.f_name)
                print("File name GUI: ", self.file_name)
            self.count_pro += 1 #Go From 5 to 6
            self.botResponse(self.userInput.text)
            #
        elif self.count_pro == 7:
            print(self.func_counting, self.rules.func_count)
            if self.func_counting < self.rules.func_count:
                print("Add ", self.userInput.text)
                self.funcs.append(self.userInput.text)
                self.func_counting += 1
                self.refresh_chat()
                if(self.func_counting < self.rules.func_count):
                    self.botResponse(self.userInput.text)
                else:
                    self.rules.funcs = self.funcs
                    print("Funcs ", self.rules.funcs)
                    self.count_pro += 1 #Go from 7 to 8
                    self.refresh_chat()
                    self.botResponse(self.userInput.text)
            elif self.func_counting >= self.rules.func_count:
                self.rules.funcs = self.funcs
                print("Funcs ", self.rules.funcs)
                self.count_pro += 1 #Go from 7 to 8
                self.refresh_chat()
                self.botResponse(self.userInput.text)
        elif self.count_pro == 9:
            self.rules.write_file = self.userInput.text
            print(self.rules.write_file)
            self.refresh_chat()
            self.rules.trial = False
            self.rules.func_count = 0
            self.rules.file = ""
            self.rules.sentence_break(self.req)
            self.count_pro = 1
            self.func_counting = 0
            self.file_name = ""
            self.rules.reset()
            #self.rules.trial = True
            #self.rules.f_name = "Test46"
            #self.rules.write_file = "No"
            #self.rules.sample_param = []
            #self.rules.params_func = []

        else:
            self.refresh_chat()
        
        #self.botResponse(self.userInput.text)
        #self.chatPannel.remove_widget(self.chat)
        #self.chat = ChatPage()
        #self.chat.bind(minimum_height=self.chat.setter('height'))
        #self.chatPannel.add_widget(self.chat)
        
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
