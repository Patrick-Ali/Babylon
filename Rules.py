from TextAnalysis import TextAnalysis as TA
from JSON import JSON
from Py_Write import PyCreate as PC
from Expanding import Expands
from pathlib import Path


class Rules():
    reader = JSON()
    text_analysis = TA()
    write = PC()
    exp = Expands()
    sample_param = []
    params_func = []
    param_count = 0
    var_count = 0
    file = ""
    mp = ""
    file_add = {}
    func_count = 0
    funcs = [""]
    write_file = "No"
    f_name = "Test46"
    trial = True

    #If user input after then split includes 'create API call' call API_Rules 

    def rule_test(self, sentence):
        print("Here 1")
        hold =  sentence
        split_and = hold.split("and")
        program = ''
        master_program = ''
        count = 0
        if len(split_and) > 1:
            for part in split_and:
                split_then = part.split("then")
                if len(split_then) > 1:
                    for bit in split_then:
                        count += 1
                        if count < len(split_then):
                            temp = self.generate_code(bit, count, False, program)
                            if temp is not None:
                                program = temp
                        else:
                            temp = self.generate_code(bit, count, True, program)
                            if temp is not None:
                                master_program += temp
            
                else:
                    count += 1
                    temp = self.generate_code(part, count, True, program)
                    if temp is not None:
                        master_program += temp
                count = 0
                program = ''
                self.var_count = 0
                self.sample_param = []
                self.params_func = []
                self.param_count = 0
        else:
            split_then = hold.split("then")
            if len(split_then) > 1:
                for bit in split_then:
                    count += 1
                    if count < len(split_then):
                        temp = self.generate_code(bit, count, False, program)
                        if temp is not None:
                            program = temp
                        
                    else:
                        temp = self.generate_code(bit, count, True, program)
                        if temp is not None:
                            master_program += temp
            else:
                count += 1
                temp = self.generate_code(split_then[0], count, True, program)
                if temp is not None:
                    master_program += temp
                
        write_conf = self.write_file#"No"#input("Do you want to write the program to file? \n Yes or No: ")
        #print(master_program)
        print(write_conf)
        print("File ", self.file)
        print("File ", self.f_name)
        if write_conf.lower() == "yes":
            self.add_program("test", "test")
            self.write.write_line(self.f_name+".py", master_program)
            self.mp = master_program
            #self.reset()
            return master_program
        else:
            print(self.func_count)
            self.mp = master_program
            print(master_program)
            #self.reset()
            return master_program

    def reset(self):
        self.var_count = 0
        self.sample_param = []
        self.params_func = []
        self.param_count = 0
        self.file = ""
        self.mp = ""
        self.file_add = {}
        self.func_count = 0
        self.funcs = [""]
        self.write_file = "No"
        self.f_name = "Test46"
        self.trial = True
                
    def sentence_break(self, text):
        #Break the user input into tokens
        sentences = self.text_analysis.tokenize_text(text)

        #If the text is not empty
        if len(sentences) > 0:
            
            #For each sentence in the user input
            for sentence in sentences:
                hold = self.rule_test(sentence)



    def generate_code(self, text, count, ret, program):
        print("Here 1.5")
        #Lower capitals
        clean_text = self.text_analysis.lower_capital(text)

        count_text = 0
        extra_p = ""
        ##Replace with regex check
        for text in clean_text:
            if text == "by":
                extra_p = clean_text[count_text+1]
            count_text += 1
                

        #Remove punctuation
        depunctuated_text = self.text_analysis.remove_punctuation(clean_text) # For synonyms

        #Break a sentence into words with punctuation
        tokens_one = self.text_analysis.tokenize_sentence(clean_text)

        #Break a sentence into words without punctuation
        tokens_two = self.text_analysis.tokenize_sentence(depunctuated_text)

        #Get unique words from both sets, e.g. from tokens_1 user-test and from tokens_2 (user, test)
        combine_text = self.text_analysis.combine_text(tokens_one, tokens_two)
        
        #Check if the user refrences any available functions
        possible_operations = self.domain_search(combine_text)

        #Check if there is any operations and begin analysing them
        if len(possible_operations) > 0 and len(possible_operations) < 2:
            domain = possible_operations[0][0]
            operation = possible_operations[0][1]
            specifics = self.operation_specifics(domain, operation)
            #If the user has asked for the answer from previous function they only need add the next parameter
            if count == 1:
                #params_text = "1,2"#input("""Please provide smaple input, e.g. for
                        #'I want a program to add two numbers togther.'
                        #the input would be '1, 2'. Use comma (,) to denote each input. \n
                        #Enter input samples: """ )
                #params_split = params_text.split(",")
                #for param in params_split:
                    #self.sample_param.append(param)  
                ##Check operations requirements match user input
                if self.trial == True:
                    self.sample_param = [1,2]
                for i in range(len(self.sample_param)):
                    if self.sample_param[i] != 'ans':
                        param = "param_"+str(i)
                        self.params_func.append(param)
                    else:
                        param = "param_empty"
                        self.params_func.append(param)
            print("Params ",  self.params_func)          
            if len(self.params_func) > 0:
                hold = self.domain_analysis(specifics, self.params_func, text, self.sample_param, count, ret, program)
                print(hold)
                return hold
                      
        elif len(possible_operations) >= 2:
            line_one = "I found a list of potential operations that may fit your needs: \n"
            count_param = 0
            operations = []
            for operation in possible_operations:
                count_param += 1
                domain = operation[0]
                operation = operation[1]
                operations.append(operation)
                specifics = self.operation_specifics(domain, operation)
                line_three = (str(count_param) + ") " + specifics + " \n")
                print(line_three)
            line_two = int(input("\n If any operation meets your requirements enter its number: "))
            count_param = 0
            for op in operations:
                if (count_param + 1) != line_two:
                    clean_text = clean_text.replace(op, "")
                count_param += 1
            print(clean_text)
            
            self.generate_code(clean_text, count, ret, program)

        else:
            again = True
            while again == True:
                print("I do not understand the request, perhaps try rephrasing or look at operations I can do. ")
                test = input("To try again enter T, to expand the knowledge base enter A, or to exit enter E: ")
                test = self.text_analysis.lower_capital(test)
                if test == 't':
                    again = False
                    hold = input("Enter whole text: \n")
                    self.sentence_break(hold)
                    break
                elif test == 'a':
                    self.expand()
                    again = False
                    self.generate_code(text, count, ret, program)
                else:
                    again = False
                    print("Exiting...")
                    break

    def expand(self):
        dom = input("Do you want to add a new domain? \n Y for yes or N for No: ")
        if dom.lower() == "y":
            self.exp.domain()
        op = input("Do you want to add a new operation? \n Y for yes or N for No: ")
        if op.lower() == "y":
            self.exp.operation()
        func = input("Do you want to add a new function? \n Y for yes or N for No: ")
        if func.lower() == "y":
            self.exp.program_function()
    
    def operation_specifics(self, domain, operation):
        operation = self.reader.getData(domain, operation)
        return operation
    
    def code_search_params(self, text):
        hold = self.reader.getData("py", "functions")
        temp = hold[text]['vars']
        return temp
        

    def code_search(self, text):
       hold = self.reader.getData("py", "functions")
       match = []
       print("Text ", text)
       for key in hold:
           print("Key ", key)
           if key in text:
               match.append(key)
       return match
    
    def domain_search(self, text):
        domains = self.reader.getData("domains", "domains")
        match = []
        for domain in domains:
            hold = self.reader.loadData(domain)
            for key in hold:
                if key in text:
                    match.append((domain, key))
        return match
    
    def create_function_code(self, file, func_name, description, params, operation, sample_param, count, ret, program):
        
        hold = self.generate_function_code(func_name, params, operation[0], (file+".py"), count, ret, program, sample_param)
        #Work needed on program directory
        #if hold == "Done":
            #self.add_program(file, description)
        return hold
        '''Allow the user to run the program and get sample output'''        
        ##self.run_program(file, sample_param)
        ##self.run_pro("run_pro.py")

    def domain_analysis(self, text, params, description, sample_param, count, ret, program):
        print("Here 16")
        clean_text = self.text_analysis.lower_capital(text)
        depunctuated_text = self.text_analysis.remove_punctuation(clean_text)
        operation = self.code_search(depunctuated_text)
        print(len(operation))
        if len(operation) > 0 and len(operation) < 2: 
            self.param_count = self.code_search_params(operation[0])
            self.var_count += int(self.param_count)
            if "function" in depunctuated_text:
                check = 0
                func_name = ''
                print("Count ", count)
                if count == 1:
                    if self.file == '':
                        print("Here 55")
                        self.file = self.f_name#"Test12"#input("What do you want to call the program? \n Enter name: ")
                        self.file = self.text_analysis.lower_capital(self.file)
                        check = self.checkFile("./"+self.file+".py", False)
                        if check == 0:
                            self.file_add = {self.file:{"functions":[]}}
                    #func_name = ""
                    print("Trial ", self.trial)
                    if self.trial == True:
                        func_name = "Test12"#input("What do you want to call the function? \n Enter name: ")
                    else:
                        func_name = self.funcs[self.func_count]
                    func_name = self.text_analysis.lower_capital(func_name)
                    self.func_count += 1 
                if check == 0:
                    temp_func = self.file_add[self.file]["functions"]
                    temp_func.append(func_name)
                    self.file_add[self.file]["functions"] = temp_func
                    hold = self.create_function_code(self.file, func_name, description, params, operation, sample_param, count, ret, program)
                    return hold
                elif check == 1:
                    while check == 1:
                        confirm = self.text_analysis.lower_capital(input("The file already exists, do you want to overwrite it. \n Y for yes and N for no, or E to exit: "))
                        #Overwrite file with new function
                        if confirm == 'y':
                            check = 0
                            con = self.checkFile("./"+self.file+".py", True)
                            
                            hold = self.create_function_code(self.file, func_name, description, params, operation, sample_param, count, ret, program)
                            return hold
                        #Exit from code generation
                        elif confirm == 'e':
                            check = 0
                            break
                        #Try a different file name
                        else:
                            self.file = input("What do you want to call the program? \n Enter name: ")
                            self.file = self.text_analysis.lower_capital(self.file)
                            check = self.checkFile("./"+self.file+".py", False)
                            if check == 0:
                                hold = self.create_function_code(self.file, func_name, description, params, operation, sample_param, count, ret, program)
                                return hold
                                
    def generate_function_code(self, name, params, operation, file, count, ret, program, sample_params):
        #Create funciton using the operation found in the domain description
        return self.write.create_function(name, params, operation, file, count, ret, program, sample_params, self.var_count, self.param_count)
        
    def get_data(self):
        try:
            data = self.reader.loadData("programs")
            return data
        except:
            return {}
        
    def run_program(self, name, params, func_name=None):
        imp = self.write.create_import(name)
        run = self.write.create_app_run_multi()
        clas = name+"."
        call = ""
        if func_name is None:
            call = self.write.create_call(name, params)
        else:
            call = self.write.create_call(func_name, params)
        prin = self.write.create_print((clas+call))
        indent = self.write.get_indent()
        new_line = self.write.get_new_line()

        line = imp + new_line + run + new_line + indent + prin

        confirm = self.checkFile("./run_pro.py", True)

        self.write.write_line("run_pro.py", line)
        
    def add_program(self, name, description):
      data = self.get_data()
      #data[name] = description
      data[self.file] = self.file_add[self.file]
      self.reader.addData("programs", data)
      
    def run_pro(self, file):
        result = self.write.call_py(file)
        return result
    
    def checkFile(self, path, remove):
        try:
            file = Path(path)
            if file.is_file():
                if remove == True:
                    file.unlink()
                    return 12
                elif remove == False:
                    return 1 #"File already exists"
            else:
                return 0
        except Exception as e:
            raise ValueError(e.message)


if __name__ == '__main__':
   #Testing
   rules = Rules()
   test = rules.sentence_break("I want a program to determine the greater of two objects") #add two numbers then multiply and subtract then multiply#then multiply then subtract and subtract then multiply then multiply 


               
