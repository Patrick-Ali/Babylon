import sys
sys.path.append('../')
from ChatHistory import ChatHistory as ch
from JSON import JSON
import Api_Call_Build
import Conv_Numb
import Expanding
import Rules #from Rules 
from TextAnalysis import TextAnalysis as ta

# def test_JSON_load():
#    reader = JSON()
#    data = reader.loadData("unit_test")
#    test = {"test": "test"}
#    assert data == test

# def test_JSON_add():
#     reader = JSON()
#     #new_data = {}
#     data = reader.loadData("unit_test")
#     data["test2"] = "test2"
#     reader.addData("unit_test", data)
#     new_data = reader.loadData("unit_test")
#     test = {"test": "test", "test2": "test2"}
#     assert new_data == test

# def test_CH_load():
#    hold = ch()
#    assert hold.checkFile("./user.csv") == True
   
# def test_CH_add():
#    hold = ch()
#    chat = len(hold.readFile("./user.csv"))
#    hold.writeFile("./user.csv", "Hello")
#    chat2 = len(hold.readFile("./user.csv"))

#    assert chat2 == (chat+1)

# def test_generation_small(capsys):
#    short = '''def trial6(param_0, param_1):
#   op_add = param_0 + param_1
#   return op_add'''
#    rules = Rules.Rules()
#    input_values = ["1,2", "Test749", "trial6", "No"]
#    def mock_input(s):
#        return input_values.pop(0)
#    Rules.input = mock_input
#    out, err = capsys.readouterr()
#    test = Rules.Rules.sentence_break(rules, "I want a program to add two numbers") #then multiply then subtract and subtract then multiply then multiply
#    print("MP ", rules.mp)
#    mp = rules.mp
#    mp = mp.replace(" ", "")
#    mp = mp.replace("\n", "")
#    short = short.replace(" ", "")
#    short = short.replace("\n", "")
#    print(mp == short)
#    assert mp == short
    
# def test_generation_medium(capsys):
#     medium = '''def trial7(param_0, param_1, param_3):
#    op_add = param_0 + param_1
#    hold1 = op_add
   
#    op_mul = hold1 * param_3
#    return op_mul'''
#     rules = Rules.Rules()
#     input_values_2 = ["1,2,ans,3", "Test741852", "trial7", "No"]
#     def mock_input_2(s):
#         #print(input_values_2)
#         return input_values_2.pop(0)
#     Rules.input = mock_input_2
#     out, err = capsys.readouterr()
#     test = Rules.Rules.sentence_break(rules, "I want a program to add two numbers then multiply")
#     mp = rules.mp
#     mp = mp.replace(" ", "")
#     mp = mp.replace("\n", "")
#     medium = medium.replace(" ", "")
#     medium = medium.replace("\n", "")
#     assert mp == medium
    
# def test_generation_large(capsys):
#     large = '''def trial9(param_0, param_1, param_3):
#    op_add = param_0 + param_1
#    hold1 = op_add
   
#    op_mul = hold1 * param_3
#    return op_mul

# def trial89(param_0, param_1, param_3):
#    op_sub = param_0 - param_1
#    hold1 = op_sub
   
#    op_mul = hold1 * param_3
#    return op_mul'''
#     rules2 = Rules.Rules()
#     input_values_3 = ["1,2,ans,3", "Test753852", "Trial9", "5,2,ans,9", "trial89", "No"]
#     def mock_input_3(s):
#         #print(input_values_3)
#         return input_values_3.pop(0)
#     Rules.input = mock_input_3
#     out, err = capsys.readouterr()
#     test = Rules.Rules.sentence_break(rules, "I want a program to add two numbers then multiply and subtract then multiply")
#     mp = rules2.mp
#     mp = mp.replace(" ", "")
#     mp = mp.replace("\n", "")
#     print(mp)
#     large = large.replace(" ", "")
#     large = large.replace("\n", "")
#     print(large)
#     assert mp == large

# def test_generation_none(capsys):
#    code = ""
#    test_input_none = [
#       "e"
#    ]
#    rules5 = Rules.Rules()
#    def mock_input_9(s):
#       return test_input_none.pop(0)
#    Rules.input = mock_input_9
#    out, err = capsys.readouterr()
#    test = Rules.Rules.sentence_break(rules5, "")
#    mp = rules5.mp
#    mp = mp.replace(" ", "")
#    mp = mp.replace("\n", "")
#    #print(mp)
#    large = code.replace(" ", "")
#    large = large.replace("\n", "")
#    assert mp == large

# def test_generation_multi_fail(capsys):
#    short = '''def trial6(param_0, param_1):
#      op_add = param_0 + param_1
#      return op_add'''
#    rules7 = Rules.Rules()
#    input_values_multi = ["1", "1,2", "Test1749", "trial6", "No"]
#    def mock_input_multi(s):
#       print(input_values_multi)
#       return input_values_multi.pop(0)
#    Rules.input = mock_input_multi
#    out, err = capsys.readouterr()
#    test = Rules.Rules.sentence_break(rules7, "I want a program to add subtract two numbers") #then multiply then subtract and subtract then multiply then multiply
#    print("MP ", rules7.mp)
#    mp = rules7.mp
#    mp = mp.replace(" ", "")
#    mp = mp.replace("\n", "")
#    short = short.replace(" ", "")
#    short = short.replace("\n", "")
#    print(mp == short)
#    assert mp == short

# def test_API_generation(capsys):
#    code = ''' import requests
#    def trial65():
#      response = requests.get("https://api.nasa.gov/planetary/apod?hd=True&api_key=DEMO_KEY")
#      if response.status_code == 200 or response.status_code == 201:
     
#        return response.json()
#      else:
#        return "Request failed"
#     '''
#    api = Api_Call_Build.API_Rules()
#    input_values_api = ["test156", "get", "trial65", "https://api.nasa.gov/planetary/apod?hd=True&api_key=DEMO_KEY", "no", "no", "no", "yes", "no", "j", "yes", "no"]
#    def mock_input_5(s):
#       #print(input_values_3)
#       return input_values_api.pop(0)
#    Api_Call_Build.input = mock_input_5
#    out, err = capsys.readouterr()
#    test = Api_Call_Build.API_Rules.api_rule_test(api, "Get API")
#    api_test = api.pro
#    api_test = api_test.replace(" ", "")
#    api_test = api_test.replace("\n", "")
#    code = code.replace(" ", "")
#    code = code.replace("\n", "")
#    assert api_test == code

# def test_expansion(capsys):
#    code = '''def trial357(param_0, param_1):
#    op_lesser = param_0 < param_1
#    return op_lesser'''
#    test_input = [
#       "a",
#       "n",
#       "y",
#       "science",
#       "lesser",
#       "function determines the lesser of two objects",
#       "y",
#       "lesser",
#       "name,op_lesser",
#       "vars,2",
#       "code,op_lesser = <var1> < <var2>",
#       "return,return op_lesser",
#       "end",
#       "1,2",
#       "test101",
#       "trial357",
#       "no"
#    ]
#    rules6 = Rules.Rules()
#    exp = Expanding.Expands()
#    def mock_input_6(s):
#       #print(test_input)
#       return test_input.pop(0)
#    Rules.input = mock_input_6
#    Expanding.input = mock_input_6
#    out, err = capsys.readouterr()
#    test = Rules.Rules.sentence_break(rules6, "I want a program to determine the lesser of two objects")
#    mp = rules6.mp
#    mp = mp.replace(" ", "")
#    mp = mp.replace("\n", "")
#    #print(mp)
#    large = code.replace(" ", "")
#    large = large.replace("\n", "")
#    #print(large)
#    assert mp == large

# def test_Regex():
#    hold = Conv_Numb.regexe("I want a program to add 12345 variables together.")
#    test = ["12345 variables"]
#    assert hold == test

# def test_number_translation():
#    hold = ta()
#    #con = Conv_Numb
#    temp = hold.tokenize_sentence("I want a program to add one million two hundred thousand thirty thousand four thousand five hundred sixty seven variables together")
#    print(temp)
#    last_num = False
#    cur_num = 0
#    extra = False
#    last = 0
#    next_word = ""
#    words = ["hundred","thousand","million","billion","trillion"]
#    jump = False
#    count = 0
#    start_num = -1
#    final = 0
#    for word in temp:
#        if count+1 < len(temp):
#            next_word = temp[count+1]
#        else:
#            next_word = ""
#        num = Conv_Numb.getNum(word,last_num,cur_num, extra, last, next_word)
#        print("num", num)
#        if num != "Unknown Number":
#            start_num += 1
#            print("Here")
           
#            last_num = True
#            extra_true = num[1]
#            if extra_true == 3:
#                extra_true = False
#                last_num = False
#                cur_num = 0
#                extra = 0
               
#            elif extra_true:
#                cur_num = 0
#                extra = num[0]
#                last = num[2]
#            else:
#                cur_num = num[0]
           
           
#            count += 1
#            final = num[0]
#            continue
#        elif num == "Unknown Number":
#            last_num = False
#            cur_num = 0
#            count += 1
#            if start_num != -1:
#                temp[count - (start_num+2)] = final
#                if (count - (start_num+2)) + 1 < len(temp):

#                    del temp[(count - (start_num+2)+1):(count-2)]
#                    start_num = -1
#    print(temp)

#    holding = " ".join(str(e) for e in temp)

#    print(holding)
#    test = "I want a program to add 1234567 variables together"
#    assert holding == test

# def test_call_pro(capsys):
#    code = "3"
#    test_call_input = [
#       "test15,trial16",
#       "1,2"
#    ]
#    rules9 = Rules.Rules()
#    def mock_input_8(s):
#       return test_call_input.pop(0)
#    Rules.input = mock_input_8
#    out, err = capsys.readouterr()
#    test = Rules.Rules.call_pro(rules9)#sentence_break(rules5, "")
#    res = rules9.res
#    res = res.replace(" ", "")
#    res = res.replace("\n", "")
#    #print(mp)
#    large = code.replace(" ", "")
#    large = large.replace("\n", "")
#    assert res == large
    
