from TextAnalysis import TextAnalysis as TA
from JSON import JSON
from Py_Write import PyCreate as PC
from pathlib import Path


class API_Rules():
    reader = JSON()
    text_analysis = TA()
    write = PC()
    new_line = "\n"
    indent = "  "
    #sample_param = []
    #params_func = []
    #param_count = 0
    #var_count = 0
    #file = ""

     def api_rule_test(self, sentence):
        hold =  sentence
        program = ''
        count = 0

        #What do you want to call file
        #file = input("What do you want to call file")

        #API json file create name, list of functions
        ## file_add = {file:{"functions":[]}}

        #What functoion(s) would you like to create, e.g. get, post, put...
        #List functions e.g. get, post, pacth
        '''
        func_list_in = input("What functoion(s) would you like to create, e.g. get, post, put... Input list of functions e.g. get, post, pacth")
        func_list = func_list_in.split(",")
        hold = self.reader.getData("py", "functions")
        for key in hold:
            if key in func_list:
              func = hold[key]
                
                    name = input("What do you want to call the function: ")
                    temp_func = file_add[file]["functions"]
                    temp_func.append(name)
                    file_add[file]["functions"] = temp_func
                    line_one = func["start"]
                    line_one = line_one.replace("<name>", name)
                    address = input("What url are you trying to call: ")
                    input = [address]
                    params = ["url", ]
                    query = input("Is there any query string parameters, e.g. q=test. Yes or No")
                    querys = {}
                    q = True
                    if query == "Yes":
                        q = True
                    else:
                        q = False
                    while q == True:
                        key_value = input("Enter querys in key value pairs seperated by a comma (e.g. key,value), to end type end")
                        if key_value == "end":
                            q = False
                        else:
                            temp = key_value.split(",")
                            if len(temp) == 2:
                                querys[temp[0]] = temp[1]
                            else:
                                print("Not recognised")
                    if len(querys) > 0:
                        params.append(querys)
                        input.append("query")
                        
                    head = input("Is there any header parameters, e.g. Autherization : token. Yes or No")
                    headers = {}
                    h = True
                    if head == "Yes":
                        h = True
                    else:
                        h = False
                    while h == True:
                        key_value = input("Enter header values in key value pairs seperated by a comma (e.g. key,value), to end type end")
                        if key_value == "end":
                            h = False
                        else:
                            temp = key_value.split(",")
                            if len(temp) == 2:
                                headers[temp[0]] = temp[1]
                            else:
                                print("Not recognised")
                    if len(headers) > 0:
                        params.append(headers)
                        input.append("head")
                        
                    auth = input("Is there any authorisation parameters, e.g. username, password. Yes or No")
                    if auth == "Yes":
                        cred = input("Enter credentials sperated by a comma, e.g. user, pass")
                        cred = cred.split(",")
                        hold = (cred[0], cred[1])
                        params.append(hold)
                        input.append("auth")
                        
                    ver = input("Do you want to verify SSL certificate. Yes or No")
                    if var == "No":
                        var = False
                        params.append(var)
                        input.append("verify")
                        

                    time_out = input("Do you want to set a timeout for call. Yes or No: ")
                    if auth == "Yes":
                        tim = int(input("Enter timeout, e.g. 1.15 is 1 minute 15 seconds"))
                        params.append(tim)
                        input.append("timeout")
                    ret = input("How do you want the response, for status code type S, for response in text format type T, for response in JSON formate type J")
                    elif ret == "S":
                        pass
                    elif ret == "T":
                    elif ret == "J"
                    
                    #For each input create a variable
                    #Convert dictionairies to strings
                    #To add post, put, patch check for data
                    #Get creation from PY JSON
                    #Create program
                    
                '''
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
            
