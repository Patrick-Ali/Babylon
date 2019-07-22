from TextAnalysis import TextAnalysis as TA
from JSON import JSON
from Py_Write import PyCreate as PC
from pathlib import Path


class Rules():
    reader = JSON()
    text_analysis = TA()
    write = PC()
    sample_param = []
    params_func = []
    param_count = 0
    var_count = 0
    file = ""

    def rule_test(self, sentence):
        hold =  sentence
        split_and = hold.split("and")
        program = ''
        count = 0
        if len(split_and) > 1:
            for part in split_and:
                print("And around: ", self.params_func)
                print("Sample params: ", self.sample_param)
                split_then = part.split("then")
                if len(split_then) > 1:
                    for bit in split_then:
                        #self.params_func = []
                        count += 1
                        if count < len(split_then):
                            temp = self.generate_code(bit, count, False, program)
                            program = temp
                            print(program)
                        else:
                            temp = self.generate_code(bit, count, True, program)
                        #program += temp
            
                else:
                    count += 1
                    temp = self.generate_code(part, count, True, program)
                    #program += temp
                count = 0#
                program = ''#
                self.var_count = 0
                self.sample_param = []
                self.params_func = []
                self.param_count = 0
                print("Here 101")
        else:
            print("Here 5")
            split_then = hold.split("then")
            if len(split_then) > 1:
                print("Here 6")
                for bit in split_then:
                    count += 1
                    print(count, len(split_then))
                    if count < len(split_then):
                        print("Here 4")
                        print(count)
                        temp = self.generate_code(bit, count, False, program)
                        program = temp
                        print(program)
                    else:
                        temp = self.generate_code(bit, count, True, program)
                    #program += temp
            else:
                print("Here 2")
                count += 1
                temp = self.generate_code(split_then[0], count, True, program)
                #program += temp
                
    def sentence_break(self, text):
        #Break the user input into tokens
        sentences = self.text_analysis.tokenize_text(text)

        #If the text is not empty
        if len(sentences) > 0:
            print("Here 1")
            #For each sentence in the user input
            for sentence in sentences:
                hold = self.rule_test(sentence)



    def generate_code(self, text, count, ret, program):
        #print(text)
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
        #print(combine_text)
        #Check if the user refrences any available functions
        possible_operations = self.domain_search(combine_text)

        #Check if there is any operations and begin analysing them
        ## Break into generate code function
        print("Here 3")
        #print(possible_operations)
        if len(possible_operations) > 0 and len(possible_operations) < 2:
            print("Here 60")
            ## Rework for multiple operations
            domain = possible_operations[0][0]
            operation = possible_operations[0][1]
            specifics = self.operation_specifics(domain, operation)
            #print(count)
            #If the user has asked for the answer from previous function they only need add the next parameter
            if count == 1:
                #self.params_func = []
                print("Here 45")
                params_text = input("""Please provide smaple input, e.g. for
                        'I want a program to add two numbers togther.'
                        the input would be '1, 2'. Use comma (,) to denote each input. \n
                        Enter input samples: """ )
                params_split = params_text.split(",")
                print("Param split")
                print(params_split)
                #sample_param = []
                for param in params_split:
                    self.sample_param.append(param)
                #params = []
                print("Params")  
                ##Check operations requirements match user input
                for i in range(len(self.sample_param)):
                    if self.sample_param[i] != 'ans':
                        param = "param_"+str(i)
                        self.params_func.append(param)
                    else:
                        param = "param_empty"
                        self.params_func.append(param)
                        
            print(self.params_func)       
            if len(self.params_func) > 0:
                #print("Count " + str(count))
                hold = self.domain_analysis(specifics, self.params_func, text, self.sample_param, count, ret, program)
                #print("Hold 1 " + hold)
                return hold
                      
        elif len(possible_operations) >= 2:
            print("Here 4")
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
            #print(clean_text)
            #print(operations)
            #print(line_two)
            count_param = 0
            for op in operations:
                #print(op)
                #print(count)
                #print((count + 1) != line_two)
                if (count_param + 1) != line_two:
                    clean_text = clean_text.replace(op, "")
                count_param += 1
            print(clean_text)
            #print("Count 1 " + str(count))
            self.generate_code(clean_text, count, ret, program)
            #return line_one + line_two
                #pass
                #Ask user to chose between possible soloutions
                #Potential automation of similarity between sentences
        else:
            again = True
            while again == True:
                print("I do not understand the request, perhaps try rephrasing or look at operations I can do. ")
                test = input("To try again enter T or to exit enter E: ")
                test = self.text_analysis.lower_capital(test)
                if test == 't':
                    again = False
                    hold = input("Enter whole text: \n")
                    self.sentence_break(hold)
                    break
                else:
                    again = False
                    print("Exiting...")
                    break
                ##line_two = "To view available operations enter show operations."
            #return line_one + line_two
        #Tell user we are not sure what they want,
            
    def operation_specifics(self, domain, operation):
        operation = self.reader.getData(domain, operation)
        return operation
    
    def code_search_params(self, text):
        hold = self.reader.getData("py", "functions")
        #print(text)
        temp = hold[text]['vars']
        return temp
        

    def code_search(self, text):
       hold = self.reader.getData("py", "functions")
       #print(hold)
       match = []
       for key in hold:
           if key in text:
               #print("Key " + key)
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
    
    def create_function_code(self, file, description, params, operation, sample_param, count, ret, program):
        #print("Count 2 " + str(count))
        hold = self.generate_function_code(file, params, operation[0], (file+".py"), count, ret, program, sample_param)
        if hold == "Done":
            self.add_program(file, description)
        return hold
        #Lower name from capitals
        
        ##self.run_program(file, sample_param)
        ##self.run_pro("run_pro.py")
        #ask user for file name

    def domain_analysis(self, text, params, description, sample_param, count, ret, program):
        clean_text = self.text_analysis.lower_capital(text)
        depunctuated_text = self.text_analysis.remove_punctuation(clean_text)#
        operation = self.code_search(depunctuated_text)
        #print("Test " + str(count))
        #print(depunctuated_text)
        #print(operation)
        print("Params: ", params)
        if len(operation) > 0 and len(operation) < 2: #Temp till multi operations supported
            #print(operation)
            self.param_count = self.code_search_params(operation[0])
            self.var_count += self.param_count#self.code_search_params(operation[0])
            if "function" in depunctuated_text:
                #file = ''
                check = 0
                if count == 1:
                    self.file = input("What do you want to call the program? \n Enter name: ")
                    self.file = self.text_analysis.lower_capital(self.file)
                    check = self.checkFile("./"+self.file+".py", False)
                if check == 0:
                    #print("Count 3 " + str(count))
                    hold = self.create_function_code(self.file, description, params, operation, sample_param, count, ret, program)
                    return hold
                    #self.add_program(file, description)
                    #Lower name from capitals
                    #self.generate_function_code(file, params, operation[0], (file+".py"))
                    #self.run_program(file, sample_param)
                    #self.run_pro("run_pro.py")
                    #ask user for file name
                elif check == 1:
                    while check == 1:
                        confirm = self.text_analysis.lower_capital(input("The file already exists, do you want to overwrite it. \n Y for yes and N for no, or E to exit: "))
                        #Overwrite file with new function
                        if confirm == 'y':
                            check = 0
                            con = self.checkFile("./"+self.file+".py", True)
                            #print(con)
                            #print("Count 4 " + str(count))
                            hold = self.create_function_code(self.file, description, params, operation, sample_param, count, ret, program)
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
                                #print("Count 5 " + str(count))
                                hold = self.create_function_code(self.file, description, params, operation, sample_param, count, ret, program)
                                
                                return hold
                                
    def generate_function_code(self, name, params, operation, file, count, ret, program, sample_params):
        #Create funciton using the operation found in the domain description
        print("Count 6 " + str(count))
        return self.write.create_function(name, params, operation, file, count, ret, program, sample_params, self.var_count, self.param_count)
        
    def get_data(self):
        try:
            data = self.reader.getData("programs", "programs")
            return data
        except:
            return {}
        
    def run_program(self, name, params):
        imp = self.write.create_import(name)
        run = self.write.create_app_run_multi()
        clas = name+"."
        call = self.write.create_call(name, params)
        prin = self.write.create_print((clas+call))
        indent = self.write.get_indent()
        new_line = self.write.get_new_line()

        line = imp + new_line + run + new_line + indent + prin

        confirm = self.checkFile("./run_pro.py", True)

        #print(confirm)

        self.write.write_line("run_pro.py", line)
        
    def add_program(self, name, description):
      data = self.get_data()
      data[name] = description
      self.reader.addData("programs", data)
      
    def run_pro(self, file):
        result = self.write.call_py(file)
        print(result)
        return result
    
    def checkFile(self, path, remove):
        try:
            file = Path(path)
            if file.is_file():
                if remove == True:
                    #print("Here")
                    file.unlink()
                    return 12
                elif remove == False:
                    return 1 #"File already exists"
            else:
                return 0
        except Exception as e:
            raise ValueError(e.message)


#Ask to rephrase or look at operation list

if __name__ == '__main__':
   #Testing
   rules = Rules()
   test = rules.sentence_break("I want a program to add two numbers then multiply and subtract then multiply") #then multiply then subtract


               
