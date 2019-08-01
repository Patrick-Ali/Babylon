import sys
sys.path.append('../')
from ChatHistory import ChatHistory as ch
from Rules import Rules

##def test_check():
##    hold = ch()
##    assert hold.checkFile("./user.csv") == True
##    
##
##def test_wirte():
##    hold = ch()
##    chat = len(hold.readFile("./user.csv"))
##    hold.writeFile("./user.csv", "Hello")
##    chat2 = len(hold.readFile("./user.csv"))
##
##    assert chat2 == (chat+1)

def test_pro_write():
    short = '''def trial6(param_0, param_1):
   op_add = param_0 + param_1
   return op_add'''
    rules = Rules()
    test = rules.sentence_break("I want a program to add two numbers") #then multiply then subtract and subtract then multiply then multiply
    assert test == short
