import sys
sys.path.append('../')
from ChatHistory import ChatHistory as ch
from JSON import JSON
import Api_Call_Build
import Conv_Numb
import Rules #from Rules 

def test_JSON_load():
   reader = JSON()
   data = reader.loadData("unit_test")
   test = {"test": "test"}
   assert data == test

def test_JSON_add():
    reader = JSON()
    #new_data = {}
    data = reader.loadData("unit_test")
    data["test2"] = "test2"
    reader.addData("unit_test", data)
    new_data = reader.loadData("unit_test")
    test = {"test": "test", "test2": "test2"}
    assert new_data == test

def test_CH_load():
   hold = ch()
   assert hold.checkFile("./user.csv") == True
   
def test_CH_add():
   hold = ch()
   chat = len(hold.readFile("./user.csv"))
   hold.writeFile("./user.csv", "Hello")
   chat2 = len(hold.readFile("./user.csv"))

   assert chat2 == (chat+1)

def test_generation_small(capsys):
   short = '''def trial6(param_0, param_1):
  op_add = param_0 + param_1
  return op_add'''
   rules = Rules.Rules()
   input_values = ["1,2", "Test749", "trial6", "Yes"]
   def mock_input(s):
       return input_values.pop(0)
   Rules.input = mock_input
   out, err = capsys.readouterr()
   test = Rules.Rules.sentence_break(rules, "I want a program to add two numbers") #then multiply then subtract and subtract then multiply then multiply
   print("MP ", rules.mp)
   mp = rules.mp
   mp = mp.replace(" ", "")
   mp = mp.replace("\n", "")
   short = short.replace(" ", "")
   short = short.replace("\n", "")
   print(mp == short)
   assert mp == short
    
def test_generation_medium(capsys):
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
    
def test_generation_large(capsys):
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

def test_generation_none():
    pass

def test_generation_multi_fail():
    pass

def test_API_generation(capsys):
   code = ''' import requests
   def get_get_test():
     response = requests.get("https://api.nasa.gov/planetary/apod?hd=True&api_key=DEMO_KEY")
     if response.status_code == 200 or response.status_code == 201:
     
       return response.json()
     else:
       return "Request failed"
    '''
   api = Api_Call_Build.API_Rules()
   input_values_api = ["test156", "get", "trial65", "https://api.nasa.gov/planetary/apod?hd=True&api_key=DEMO_KEY", "no", "no", "no", "yes", "no", "j", "yes", "no"]
   def mock_input_5(s):
      #print(input_values_3)
      return input_values_5.pop(0)
   Api_Call_Build.input = mock_input_5
   out, err = capsys.readouterr()
   test = Api_Call_Build.API_Rules.api_rule_test("Get API")
   api_test = api.pro
   api_test = api_test.replace(" ", "")
   api_test = api_test.replace("\n", "")
   code = code.replace(" ", "")
   code = code.replace("\n", "")
   assert api_test == code

def test_expansion():
    pass

def test_Regex():
   hold = Conv_Numb.regexe("I want a program to add 12345 variables together.")
   test = ["12345 variables"]
   assert hold == test

def test_number_translation():
   hold = Conv_Numb.getNum("I want a program to add one million two hundred thousand thirty thousand four thousand five hundred sixty seven variables together")
   test = "I want a program to add 1234567 variables together"
   assert hold == test


    
