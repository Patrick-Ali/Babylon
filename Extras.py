#from kivy.uix.gridlayout import GridLayout  # one of many layout structures
#Main Grid - top layer, chat screen, text input
#Child Grid - add to chat screen 4 cols 2 rows,
    ##1 row and column for app, second row and column for user 
##orientation = 'vertical'
##self.row_default_height = Window.height/2
##self.row_force_default = True
#print(self.cols)
#print(self.rows)
##self.size_hint_y = None
##self.minimum_height=.setter('height')
##self.size(Window.width, Window.height)
##self.size_hint(None, None)
##class MainWindow(Window):
    ##def __init__(self, **kwargs):
        ##super().__init__(self)
##self.size(Window.width, Window.height)
##self.size_hint(None, None)
##self.cols = 2
##self.rows = 1

#def _on_resize(width, height):
            #print(width, height)
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
        #grid.bind(minimum_height=grid.setter('height'))
        #win = MainWindow()


#self.use_bubble = True
##grid.rows_minimum[0]= 120/5 #(Window.height/100)*20
#settings.background_normal = "Gear2.png"
#text=u"⚙️"
##header.size_hint(1,1)
#self.userInput = UserIn("Test Input")
#textinput = TextInput(text='Hello world')
#self.userInput.select_all()
#self.userInput.do_backspace(from_undo=False, mode='bkspc')
#self.userInput.focus = True
#self.hint_text = 'Test input'
# But we want to take an action only when Enter key is being pressed, and send a message
# allow for ...text input.
#print(Window.height)

    #path = ""

    #def __init__(file):
        #self.path = file
#print(temp)

#return hold.checkFile("./user.csv")
#assert ch.checkFile("./user.csv") == True
#if __name__ == "__main__":
    #print(test_check())

#from kivy.uix.stacklayout import StackLayout

#self.background_color = (255, 0, 0, 1)
#with self.canvas:
#Color(255,0,0,1)
#Rectangle(pos=self.pos, size=self.size)

#,[0,0,0,0.25]
#,size_hint_y = None, height = 40
#for i in range(25):
#btn = Button(text= str(i),size_hint_y = None, height = 40)
#self.add_widget(btn)
#btn = Button(text= str(i), size_hint_x = 0.40)
#btn = Button(text= str(i), size_hint_x = 0.40)

#Demo chat
        #for i in range(25):
            #if alter:
                #msg = message("left")
                #bot = Lab(str(i), 0.40,[25,181,254,0.50]) 
                #msg.add_widget(bot)
                #self.add_widget(msg)
                #alter = False
            #else:
                #msg = message("right")
                #user = Lab(str(i), 0.40,[0,0,255,0.50])
                #msg.add_widget(user)
                #self.add_widget(msg)
                #alter = True
#print("Here")
#print(msge)
#test = len(chat) == len(bot)
#alter = True

#print(self.userInput.text)
#msg = message("right")
#userHold = Lab(self.userInput.text, 0.40,[0,0,255,0.50])
#msg.add_widget(userHold)
#self.chat.add_widget(msg)

#Line(rounded_rectangle=(self.pos[0], self.pos[1], self.size[0]+1.9, self.size[1]+1.9, 10))

#False

        #chat = hold.readFile("./user.csv")
        #bot = hold.readFile("./bot.csv")
        
        
        #count = 0

        #if len(chat) >= len(bot):
            #for msge in range(len(chat)):
                #if count < len(bot):
                    #msg = message("left")
                    #botHold = Lab(bot[count], 0.40,[25,181,254,0.50])
                    #msg.add_widget(botHold)
                    #self.add_widget(msg)
                    #count+=1
                
                #msg = message("right")
                #user = Lab(chat[msge], 0.40,[0,0,255,0.50])
                #msg.add_widget(user)
                #self.add_widget(msg)
                
        #elif len(bot) > len(chat):
            #for msge in range(len(bot)):
                #msg = message("left")
                #botHold = Lab(bot[msge], 0.40,[25,181,254,0.50])
                #msg.add_widget(botHold)
                #self.add_widget(msg)

                #if count < len(chat):
                    #msg2 = message("right")
                    #user = Lab(chat[count], 0.40,[0,0,255,0.50])
                    #msg2.add_widget(user)
                    #self.add_widget(msg)
                    #count+=1

#, Line
#from kivy.uix.image import Image

##class Symbols(Image):
##    
##    def __init__(self, source, **kwargs):
##        super().__init__(**kwargs)
##        self.source = source
##        self.y = self.parent.y + self.parent.height - 250
##

#print(length)
#print(leng_check)
#cont = False

#self.padding = [0,0,0,0]
            #if chat[msge][0] == 'b':
                #msg = message("left")
                #botHold = Lab(chat[msge][1:], 0.40,[25,181,254,0.50], 10)
                #msg.add_widget(botHold)
                #self.add_widget(msg)
                
            #elif chat[msge][0] == 'u':
                #msg = message("right")
                #user = Lab(chat[msge][1:], 0.40,[0,0,255,0.50], 10)
                #msg.add_widget(user)
                #self.add_widget(msg)
                
            #else:
                #continue

#print(chat[msge][:72])
#print(chat[msge][73:])
#print(count)
#print("Temp: " + temp)
#print("Temp len " + str(len(temp)))
#print("Message: " + msg)

##class BabylonApp(App):
##    
##    userInput = UserIn("Example: I want a program to add two numbers.")
##    chat = ChatPage()# Container for adding messages
##    hold = ch()
##    chatPannel = ChatPannel()# Container for scrolling
##    
##    def build(self):
##
##        #Create the base sections for the app
##        grid = ChatPageMain(1,3)
##
##        #Create the header section which contains the
##        #App title and settings button
##        header = ChatPageMain(2,1)
##        
##        #Set the header to fill 10% of the app height 
##        header.size_hint_y = 0.10
##
##        #App title set to 80% width of the header 
##        title = Lab("Babylon", 0.80, [255,0,0,0.25], 0)
##        #title.size_hint_x = 0.80
##
##        #Settings button set to 10% width of the header  
##        settings = Button(text="Settings", size_hint_x = 0.10)
##
##        #Add title and settings button to the app 
##        header.add_widget(title)
##        header.add_widget(settings)
##
##        #Create the footer section which contains the
##        #User input and submit button
##        footer = ChatPageMain(2,1)
##        footer.size_hint_y = 0.10
##
##        #User input set to 80% width of the footer
##        self.userInput.size_hint_x = 0.80
##
##        #Submit button set to 10% width of the footer  
##        submit = Button(text="Submit", size_hint_x = 0.10)
##        #On clicking submit call send_message function
##        submit.bind(on_press=self.send_message)
##
##        #Add user input and submit button to the app
##        footer.add_widget(self.userInput)
##        footer.add_widget(submit)
##
##        #Add header section to the app
##        grid.add_widget(header)
##
##        #Create the section where the chat will appear
##        
##        
##
##        #Allow the chat to be scrollable
##        self.chat.bind(minimum_height=self.chat.setter('height'))
##
##        #Add chat section to the app
##        self.chatPannel.add_widget(self.chat)
##        grid.add_widget(self.chatPannel)
##
##        #Add footer section to the app
##        grid.add_widget(footer)
##
##        #When user presses key call the on_key_down function 
##        Window.bind(on_key_down=self.on_key_down)
##        
##        return grid
##
##    #Reset user input to original state
##    def focus_text_input(self, _):
##        self.userInput.focus = True
##        self.userInput.do_backspace(from_undo=False, mode='bkspc')
##
##    def botResponse(self, userInput):
##        #print("Hello")
##        chatLog = self.hold.writeFile("./chat.csv", ("bParoting: " + userInput))
##
##        
##    def send_message(self, _):
##        
##        #Refresh the chat
##        chatLog = self.hold.writeFile("./chat.csv", ('u' + self.userInput.text))
##        self.botResponse(self.userInput.text)
##        self.chatPannel.remove_widget(self.chat)
##        self.chat = ChatPage()
##        self.chat.bind(minimum_height=self.chat.setter('height'))
##        self.chatPannel.add_widget(self.chat)
        
        #Set the user input to original state
        #self.userInput.text = ''
        #Clock.schedule_once(self.focus_text_input, 0.1)
        
    #def on_key_down(self, instance, keyboard, keycode, text, modifiers):

        #Allows the user to press enter to submit input
        #if keycode == 40:
            #self.send_message(None)
  

#if __name__ == '__main__':
    
    #BabylonApp().run()

#print(data)
#[value]
#, value

#print("Here")
#print(dict1)
#print(dict2)

#print(dict1[key])

##test = JSON()
##data = {
##    "Test":"Data"
##    }
###dataWhole = test.loadData()
##file = "test"
##dataWhole = test.loadData(file)
###z = {**data, **dataWhole}
##z = test.mergeDict(dataWhole, data)
##print(z)
##test.addData(file, z)
##print(test.getData(file, "Test"))

#print(name)
#print(param_name)
#print(operation)
#print(file)
# Suggestion - variables, values, operations, return
#print(line)
#print("Here")
#print(line)
#line = self.reader.getData("py", operation, "return")
#f.write('print("Hello World")')
#**kwargs, args for input variables
#print(test.stdout)

    #indent = "   "
    #new_line = "\n"
    #test_call()
    #reader = JSON()
    #line = reader.getData("py", "run")
    #test("test2.py", line + new_line)
    #line1 = reader.getData("py", "print", "beginning")
    #line2 = '"Hello World"'
    #line3 = reader.getData("py", "print", "end")
    #sentence = indent + line1 + line2 + line3 + new_line
    #test("test2.py", sentence)
    #test("test2.py")
        #print(len(test.stdout))
        #print(test.stdout[7])

'''Testing py write'''
##    test = PyCreate()
##    test.create_function("add", ["num1", "num2"], "add", "test.py")
##    test.create_app_run("add(", ["1", "2"], "test.py")
##    print(test.call_py("test.py"))
##  test = PyCreate()
##  print(test.py_version())


'''Testing text analysis'''
##test = TextAnalysis()
##word = 'Dog,'
##word = test.lower_capital(word)
##word = test.remove_punctuation(word)
##word2 = 'red'
##sentence = "Hello Mr. Smith, how are you doing today?"
##sentence2 = "The sky is pinkish-blue"
##para = sentence + ' ' + sentence2
##para_tokens = test.tokenize_text(para)
##sentence = test.lower_capital(sentence)
##sentence = test.remove_punctuation(sentence)
##sentence2 = test.lower_capital(sentence2)
##tokens1 = test.tokenize_sentence(sentence2)
##sentence2 = test.remove_punctuation(sentence2)
##tokens2 = test.tokenize_sentence(sentence2)
##print(tokens2)
##for token in tokens1:
##    if token not in tokens2:
##        tokens2.append(token)
##print(tokens1)
##print(tokens2)
##print(para_tokens)
##print(sentence)
##print(word)
##print(test.synonym(word))
##print(test.synonym(word2))
##print(test.similarity(word, word2))

'''Testing rules'''
#print(clean_text)
#print(depunctuated_text)
#print(tokens_one)
#print(tokens_two)
#print(combine_text)
#print(possible_operations)
#print(domain + "\n" + operation)
#print(specifics)
               #print(sample_param)
               #domain_analysis()
               # Ask user for sample input, 'No Input' for no perameters
               #sample_input = []
#print(params)
#print(domain + "\n" + operation)
      #print("Here 1")
      #print(operation)
         #print("Here 2")
         #print(depunctuated_text)
#print(hold)

##print("Hello")

'''Testing Chat History'''

##    #checkFile("./user.csv")
##    hold = ChatHistory()
##    if(hold.checkFile("./bot.csv")):
##        hold.writeFile("./bot.csv", "Hello")
##        chat = hold.readFile("./bot.csv")
##        for msg in chat:
##            print(msg)

##    def __init__(self):
##        pass
              
"""Conv Numbers"""
###print(num.lower())
##print("Add " + str(num1))
##    print("Add " + str(num2))
##print("Multi " + str(num1))
##    print("Multi " + str(num2))
##print("Extra: " + str(extra))
###print(element)
##        #print(element == num)
##            #print("Working")
##            #print(nums[element])
##print("Original " + element)
##           print("Cur " + str(cur_num))
##            #last = 0
##print("Last: " + str(last))
###and jump == False:
##                    print("Hello " + str(numb))
                    #last = numb
                    #if jump == False:
                    print("Num " + num)
                    print("Next Word " + next_word)
print("Cur num " + str(cur_num))
#elif multi_now == False:
#and extra != cur_num: #: #and multi_now == False
#print("Cur " + str(cur_num))
            #multis = ["000","0000","000000","000000000","000000000000"]
##            if str(cur_num) in multis:
##                if cur_num == 000:
##                    numb = multi(numb, 100)
##                elif cur_num == 0000:
##                    numb = multi(numb, 10000)
##                elif cur_num == 000000:
##                    numb = multi(numb, 1000000)
##                elif cur_num == 000000000:
##                    numb = multi(numb, 1000000000)
##                elif cur_num == 000000000000:
##                    numb = multi(numb, 1000000000000)
##                last_num = False
##            print("Before " + str(num))
##            print("After " + str(numb))
##    #Track sequence
##    #1,234,567,890
##    #1,234,567,890
##    #1,234,567,891,234
##        #if word in words and next_word in words:
##            #jump = True
##        #elif next_word not in words:
##            #jump = False
###last_word = word
##            print("Number final: " + str(num))
##                    print(count - (start_num+2)+1)
##                    print((count-2))
##                    print(start_num+2)
##                    print(len(temp))        




##API
##Recursive list
            #What do you want to call the function#
            #Get address#
            #Get list of query strings#
            #Get header key, value list#
            #Auth#
            #If post, put, or patch get data and is it JSON data
            #Verify
            #Timeout
            #Return function type (JSON or text), specific data from request
                    #For each input create a variable
                    #Convert dictionairies to strings
                    #To add post, put, patch check for data
                    #Get creation from PY JSON
                    #Create program

        #What functoion(s) would you like to create, e.g. get, post, put...
        #List functions e.g. get, post, pacth
#What do you want to call file
#API json file create name, list of functions

#Clean up
#Ask to rephrase or look at operation list
#print("Here")
#print(result)
#        #print(confirm)
#print("Count 6 " + str(count))
#print("Count 5 " + str(count))
#print(con)
#print("Count 4 " + str(count))
#self.add_program(file, description)
#Lower name from capitals
#self.generate_function_code(file, params, operation[0], (file+".py"))
#self.run_program(file, sample_param)
#self.run_pro("run_pro.py")
#ask user for file name
##print("Count 3 " + str(count))
##file = ''
##self.code_search_params(operation[0])
#print(operation)
#Temp till multi operations supported
#print("Test " + str(count))
#print(depunctuated_text)
#print(operation)
#print("Params: ", params)
##ask user for file name
#Lower name from capitals
#print("Count 2 " + str(count))
##print("Key " + key)
##print(hold)
##print(text)
##line_two = "To view available operations enter show operations."
#return line_one + line_two
#Tell user we are not sure what they want,
#return line_one + line_two
#pass
#Ask user to chose between possible soloutions
#Potential automation of similarity between sentences
#print("Count 1 " + str(count))
#print(op)
#print(count)
#print((count + 1) != line_two)
#print(clean_text)
#print(operations)
#print(line_two)
#print("Here 4")
#print("Hold 1 " + hold)
#print("Count " + str(count))
#print(self.params_func)
#params = []
#print("Params")
#print("Param split")
#print(params_split)
#sample_param = []
#self.params_func = []
#print("Here 45")
#print(count)
#print("Here 60")
## Rework for multiple operations
#print("Here 3")
#print(possible_operations)
## Break into generate code function
#print(combine_text)
#print("Test: ", text)
##print(text)
#print("Here 1")
#print("Here 2")
#print(program)
# print("Here 4")
#print(count)
#print(count, len(split_then))
#print("Here 6")
#print("Here 5")
#print("Here 101")
#master_program += program
#print("And around: ", self.params_func)
#print("Sample params: ", self.sample_param)
#self.params_func = []

