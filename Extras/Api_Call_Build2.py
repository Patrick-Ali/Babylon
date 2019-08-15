from TextAnalysis import TextAnalysis as TA
from JSON import JSON
from Py_Write import PyCreate as PC
from Rules import Rules 
from pathlib import Path
import json


class API_Rules():
    reader = JSON()
    text_analysis = TA()
    write = PC()
    new_line = "\n"
    indent = "  "
    imports = []
    test_r = Rules()
    pro = ""
    #sample_param = []
    #params_func = []
    #param_count = 0
    #var_count = 0
    #file = ""

    #Import statements
    #Get end for begining
    #List of params for function
    #Combine line 2 and 3 with line 2 ending
    #Specifics

    def api_rule_test(self, sentence):
        hold =  sentence
        program = ''
        count = 0

        file = input("What do you want to call file: ")

        file_add = {file:{"functions":[]}}

        
        func_list_in = input("What functoion(s) would you like to create, e.g. get, post, put... \n Input list of functions e.g. get, post, pacth: ")
        func_list_in = func_list_in.replace(" ", "")
        func_list = func_list_in.split(",")
        hold = self.reader.getData("py", "functions")
        data_funcs = ["post", "put", "patch"]
        program = ""
        for key in hold:
            if key in func_list:
                print(key)
                print(hold)
                func = hold[key]
                imp = func["import"]
                if imp not in self.imports:
                    self.imports.append(imp)
                name = input("What do you want to call the function: ")
                temp_func = file_add[file]["functions"]
                temp_func.append(name)
                file_add[file]["functions"] = temp_func
                
                line_one = func["start"]
                line_one = line_one.replace("<name>", name)
                address = input("What url are you trying to call: ")
                user_input = ["url",]
                params = [address,]
                line_two = func["body"]
                line_three = '"' + address + '"' + ", "
                alt_three = "\"" + "url" + "\"" + ", "
                print("Alt_three ", alt_three)

                if key in data_funcs:
                    data_query = input("This function can pass data as JSON, do you wish to pass data. \n Yes or No ")
                    d = False
                    data = {}
                    if data_query.lower() == "yes":
                        d = True
                    else:
                        d = False
                    while d == True:
                        key_value = input("Enter data in key value pairs seperated by a comma (e.g. key,value), to end type end. \n Data: ")
                        if key_value == "end":
                            d = False
                        else:
                            key_value = key_value.replace(":", ",")
                            #key_value = key_value.replace(" ", "")
                            temp = key_value.split(",")
                        if len(temp) == 2:
                            data[temp[0]] = temp[1]
                        else:
                            print("Not recognised")
                    if len(data) > 0:
                        temp_hold = func["data_json"]
                        temp_hold = temp_hold.replace("<data>", str(json.dumps(data)))
                        line_three += temp_hold + ", "
                        print("Line three ", line_three)
                        params.append(data)
                        user_input.append("data")
                        temp_hold = func["data_json"]
                        temp_hold = temp_hold.replace("<data>", "data")
                        alt_three += temp_hold + ", "

                query = input("Is there any query string parameters, e.g. www.test.com/?q=test. Yes or No: ")
                querys = {}
                q = False
                if query.lower() == "yes":
                    q = True
                else:
                    q = False
                while q == True:
                    key_value = input("Enter querys in key value pairs seperated by a comma (e.g. key,value), to end type end. \n Query: ")
                    if key_value == "end":
                        q = False
                    else:
                        key_value = key_value.replace(":", ",")
                        #key_value = key_value.replace(" ", "")
                        temp = key_value.split(",")
                        if len(temp) == 2:
                            querys[temp[0]] = temp[1]
                        else:
                            print("Not recognised")
                            
                if len(querys) > 0:
                    print("Here q")
                    temp_hold = func["params"]
                    temp_hold = temp_hold.replace("<query>", str(querys))
                    line_three += temp_hold + ", "
                    print("Line three ", line_three)
                    params.append(querys)
                    user_input.append("query")
                    temp_hold = func["params"]
                    temp_hold = temp_hold.replace("<query>", "query")
                    alt_three += temp_hold + ", "
                head = input("Is there any header parameters, e.g. Autherization : token. Yes or No: ")
                headers = {}
                h = False
                if head.lower() == "yes":
                    h = True
                else:
                    h = False
                while h == True:
                    key_value = key_value.replace(" ", "")
                    key_value = input("Enter header values in key value pairs seperated by a comma (e.g. key,value), to end type end. \n Header: ")
                    if key_value == "end":
                        h = False
                    else:
                        key_value = key_value.replace(":", ",")
                        #key_value = key_value.replace(" ", "")
                        temp = key_value.split(",")
                        if len(temp) == 2:
                            headers[temp[0]] = temp[1]
                        else:
                            print("Not recognised")
                if len(headers) > 0:
                    print("Here h")
                    temp_hold = func["headers"]
                    temp_hold = temp_hold.replace("<head>", str(headers))
                    line_three += temp_hold + ", "
                    params.append(headers)
                    print("Line three ", line_three)
                    user_input.append("head")
                    temp_hold = func["headers"]
                    temp_hold = temp_hold.replace("<head>", "head")
                    alt_three += temp_hold + ", "
                        
                auth = input("Is there any authorisation parameters, e.g. username, password. Yes or No: ")

                if auth.lower() == "yes":
                    cred = input("Enter credentials sperated by a comma, e.g. user, pass. \n username, password: ")
                    cred = cred.split(",")
                    pass_hold = (cred[0], cred[1])
                    temp_hold = func["auth"]
                    temp_hold = temp_hold.replace("<user>", "\"" + pass_hold[0] + "\"")
                    temp_hold = temp_hold.replace("<pass>", "\"" + pass_hold[1] + "\"")
                    line_three += temp_hold + ", "
                    params.append(pass_hold)
                    user_input.append("auth")
                    temp_hold = func["auth_rep"]
                    temp_hold = temp_hold.replace("<name>", "auth")
                    alt_three += temp_hold + ", "
                        
                var = input("Do you want to verify SSL certificate. Yes or No: ")
                if var.lower() == "no":
                    var = False
                    temp_hold = func["verify"]
                    temp_hold = temp_hold.replace("<ver>", str(var))
                    line_three += temp_hold + ", "
                    params.append(var)
                    user_input.append("verify")
                    temp_hold = func["verify"]
                    temp_hold = temp_hold.replace("<ver>", "verify")
                    alt_three += temp_hold + ", "

                time_out = input("Do you want to set a timeout for call. Yes or No: ")
                if time_out.lower() == "yes":
                    tim = int(input("Enter timeout, e.g. 1.15 is 1 minute 15 seconds. \n Time: "))
                    temp_hold = func["timeout"]
                    temp_hold = temp_hold.replace("<tim>", str(tim))
                    line_three += temp_hold
                    params.append(tim)
                    user_input.append("timeout")
                    temp_hold = func["timeout"]
                    temp_hold = temp_hold.replace("<tim>", "timeout")
                    alt_three += temp_hold + ", "
                line_param = ""
                for i in user_input:
                    line_param += i + ", "
                line_four = func["body2"]
                line_five = ""
                line_six = func["body3"]
                line_seven = func["return_fail"]
                ret = input("How do you want the response, \n for status code type S, for response in text format type T, for response in JSON formate type J, for specific data type D. \n Return: ")
                if ret.lower() == "s":
                    line_five = func["return_response"]
                elif ret.lower() == "t":
                    line_five = func["return_text"]
                elif ret.lower() == "d":
                    key = input("Name of data being searched for, e.g. autherization. \n Name: ")
                    temp_hold = func["return_spec"]
                    temp_hold = temp_hold.replace("<name>", str(key))
                    line_five = temp_hold + ", "
                else:
                    line_five = func["return_json"]
                
                if line_three[-2:-1] == ",":
                    line_three = line_three[:-2]
                if line_param[-2:-1] == ",":
                    line_param = line_param[:-2]
                if alt_three[-2:-1] == ",":
                    line_param = line_param[:-2]
                    
                line_param.strip()
                line_three.strip()

                print("Line three ", line_three)
                
                end_start = func["end"]
                body_end = func["bod_end"]

                save = input("Do you want to save the settings input or save function as generic template. Yes for saving input, No for saving as generic template. \n Yes or No: ")

                start = ""
                body = ""
                
                if save.lower() == "yes":
                    start = line_one + end_start + self.new_line + self.indent
                    body = line_two + line_three + body_end + self.new_line + self.indent \
                       + line_four + self.new_line + self.indent \
                       + self.new_line + self.indent + self.indent +  line_five \
                       + self.new_line + self.indent + line_six \
                       + self.new_line + self.indent + self.indent + line_seven
                else:
                    start = line_one + line_param + end_start + self.new_line + self.indent
                    body = line_two + alt_three + body_end + self.new_line + self.indent \
                       + line_four + self.new_line + self.indent \
                       + self.new_line + self.indent + self.indent +  line_five \
                       + self.new_line + self.indent + line_six \
                       + self.new_line + self.indent + self.indent + line_seven
                
                program += start + body + self.new_line + self.new_line 
                #print("Line Param: " + line_param)
                #print("Line 1: " + line_one)
                #print("Line 2: " + line_two)
                #print("Line 3: " + line_three)
                #print("Line 4: " + line_four)
                #print("Line 5: " + line_five)
                #print("Line 6: " + line_six)
                #print("Line 7: " + line_seven)
                
        line_zero = ""
        #count = 0
        imp_code = self.reader.getData("py", "import")
        for imp in self.imports:
            line_zero_hold = imp_code
            line_zero_hold = line_zero_hold.replace("<name>", imp)
            line_zero += line_zero_hold + self.new_line

        print(line_zero, program)

        write_conf = input("Do you want to write the program to file? \n Yes or No: ")

        if write_conf.lower() == "yes":
            data = self.reader.loadData("apis")
            #programs{"test":{"function":[]}}
            data[file] = file_add[file]
            print(data)
            self.reader.addData("apis", data)
            self.write.write_line(file+".py", (line_zero + program))
            self.pro = line_zero + program 
            return line_zero + program
        else:
            self.pro = line_zero + program
            return line_zero + program
            
    def call_api(self):
        data = self.reader.loadData("apis")
        for key in data:
            print(key)
            temp_hold = self.reader.getData("apis", key)
            print(temp_hold["functions"])
        select = input("Enter file and function. e.g. Test, test_get. \n Pair: ")
        select = select.replace(":", ",")
        select = select.replace(" ", "")
        temp = select.split(",")
        if len(temp) == 2:
            self.test_r.run_program(temp[0], {}, temp[1])
            self.test_r.run_pro("run_pro.py")
        else:
            print("I can not handle that")
                    
if __name__ == "__main__":
    temp = API_Rules()
    temp.api_rule_test("Put API")
    temp.call_api()
               
                    
