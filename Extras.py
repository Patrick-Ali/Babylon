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



