import sys
sys.path.append('../')
from ChatHistory import ChatHistory as ch
import Rules #from Rules 

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

##def test_pro_write(capsys):
##    short = '''def trial6(param_0, param_1):
##   op_add = param_0 + param_1
##   return op_add'''
##    rules = Rules.Rules()
##    input_values = ["1,2", "Test789", "trial6", "No"]
##    def mock_input(s):
##        return input_values.pop(0)
##    Rules.input = mock_input
##    out, err = capsys.readouterr()
##    test = Rules.Rules.sentence_break(rules, "I want a program to add two numbers") #then multiply then subtract and subtract then multiply then multiply
##    print("MP ", rules.mp)
##    mp = rules.mp
##    mp = mp.replace(" ", "")
##    mp = mp.replace("\n", "")
##    short = short.replace(" ", "")
##    short = short.replace("\n", "")
##    print(mp == short)
##    assert mp == short
    
def test_pro_wirte_then(capsys):
    medium = '''def trial7(param_0, param_1, param_3):
   op_add = param_0 + param_1
   hold1 = op_add
   
   op_mul = hold1 * param_3
   return op_mul'''
    rules = Rules.Rules()
    input_values_2 = ["1,2,ans,3", "Test741852", "trial7", "No"]
    def mock_input_2(s):
        #print(input_values_2)
        return input_values_2.pop(0)
    Rules.input = mock_input_2
    out, err = capsys.readouterr()
    test = Rules.Rules.sentence_break(rules, "I want a program to add two numbers then multiply")
    mp = rules.mp
    mp = mp.replace(" ", "")
    mp = mp.replace("\n", "")
    medium = medium.replace(" ", "")
    medium = medium.replace("\n", "")
    assert mp == medium
    
def test_pro_write_large(capsys):
    large = '''def trial9(param_0, param_1, param_3):
   op_add = param_0 + param_1
   hold1 = op_add
   
   op_mul = hold1 * param_3
   return op_mul

def trial89(param_0, param_1, param_3):
   op_sub = param_0 - param_1
   hold1 = op_sub
   
   op_mul = hold1 * param_3
   return op_mul'''
    rules2 = Rules.Rules()
    input_values_3 = ["1,2,ans,3", "Test753852", "Trial9", "5,2,ans,9", "trial89", "No"]
    def mock_input_3(s):
        #print(input_values_3)
        return input_values_3.pop(0)
    Rules.input = mock_input_3
    out, err = capsys.readouterr()
    test = Rules.Rules.sentence_break(rules, "I want a program to add two numbers then multiply and subtract then multiply")
    mp = rules2.mp
    mp = mp.replace(" ", "")
    mp = mp.replace("\n", "")
    print(mp)
    large = large.replace(" ", "")
    large = large.replace("\n", "")
    print(large)
    assert mp == large






    
