class Rules():
    reader = JSON()
    text_analysis = TA()
    write = PC()

    def rule_test(self, sentence):
        hold =  sentence
        split_and = hold.split("and")
        program = ''
        if len(split_and) > 1:
            for part in split_and:
                split_then = hold.split("then")
                if len(split_then) > 1:
                    for bit in split_then:
                        temp = self.generate_code(bit)
                        program += temp
                else:
                    temp = self.generate_code(bit)
                    program += temp
        else:
            split_then = hold.split("then")
            if len(split_then) > 1:
                for bit in split_then:
                    temp = self.generate_code(bit)
                    program += temp
            else:
                temp = self.generate_code(bit)
                program += temp
                
    def sentence_break(self, text):
        #Break the user input into tokens
        sentences = self.text_analysis.tokenize_text(text)

        #If the text is not empty
        if len(sentences) > 0:
            #For each sentence in the user input
            for sentence in sentences:
                hold = rule_test(sentence)



    def generate_code(self, text):
        #Lower capitals
        clean_text = self.text_analysis.lower_capital(sentence)

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
        ## Break into generate code function
        if len(possible_operations) > 0 and len(possible_operations) < 2:
            ## Rework for multiple operations
            domain = possible_operations[0][0]
            operation = possible_operations[0][1]
            specifics = self.operation_specifics(domain, operation)
            
            #If the user has asked for the answer from previous function they only need add the next parameter
            params_text = input("""Please provide smaple input, e.g. for
                    'I want a program to add two numbers togther.'
                    the input would be '1, 2'. Use comma (,) to denote each input. \n
                    Enter input samples: """ )
            params_split = params_text.split(",")
            sample_param = []
            for param in params_split:
                sample_param.append(param)
            params = []
                   
            ##Check operations requirements match user input
            for i in range(len(sample_param)):
                param = "param_"+str(i)
                params.append(param)
                   
            if len(params) > 0:
                self.domain_analysis(specifics, params, sentence, sample_param)
                      
        elif len(possible_operations) >= 2:
            line_one = "I found a list of potential operations that may fit your needs: \n"
            count = 0
            for operation in possible_operations:
                count += 1
                domain = operation[0]
                operation = operation[1]
                specifics = self.operation_specifics(domain, operation)
                line_one += (str(count) + ") " + specifics + " \n")
                line_two = "\n If any operation meets your requirements enter its number."
                return line_one + line_two
                #pass
                #Ask user to chose between possible soloutions
                #Potential automation of similarity between sentences
        else:
            line_one = "I do not understand the request, perhaps try rephrasing or look at operations I can do. "
            line_two = "To view available operations enter show operations."
            return line_one + line_two
        #Tell user we are not sure what they want,
            
    def operation_specifics(self, domain, operation):
        operation = self.reader.getData(domain, operation)
        return operation

    def code_search(self, text):
       hold = self.reader.getData("py", "functions")
       match = []
       for key in hold:
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

   def create_function_code(self, file, description, params, operation, sample_param):
      self.add_program(file, description)
      #Lower name from capitals
      self.generate_function_code(file, params, operation[0], (file+".py"))
      ##self.run_program(file, sample_param)
      ##self.run_pro("run_pro.py")
      #ask user for file name
      

   def domain_analysis(self, text, params, description, sample_param):
      clean_text = self.text_analysis.lower_capital(text)
      depunctuated_text = self.text_analysis.remove_punctuation(clean_text)#
      operation = self.code_search(depunctuated_text)
      if len(operation) > 0 and len(operation) < 2: #Temp till multi operations supported
         if "function" in depunctuated_text:
            file = input("What do you want to call the program? \n Enter name: ")
            file = self.text_analysis.lower_capital(file)
            check = self.checkFile("./"+file+".py", False)
            if check == 0:
               self.create_function_code(file, description, params, operation, sample_param)
               #self.add_program(file, description)
               #Lower name from capitals
               #self.generate_function_code(file, params, operation[0], (file+".py"))
               #self.run_program(file, sample_param)
               #self.run_pro("run_pro.py")
               #ask user for file name
            elif check == 1:
               while check == 1:
                  confirm = self.text_analysis.lower_capital(input("The file already exists, do you want to overwrite it. \n Y for yes and N for no, or E to exit: "))
                  if confirm == 'y':
                     check = 0
                     con = self.checkFile("./"+file+".py", True)
                     #print(con)
                     self.create_function_code(file, description, params, operation, sample_param)
                  elif confirm == 'e':
                     check = 0
                     break
                  else:
                     file = input("What do you want to call the program? \n Enter name: ")
                     file = self.text_analysis.lower_capital(file)
                     check = self.checkFile("./"+file+".py", False)
                     if check == 0:
                        self.create_function_code(file, description, params, operation, sample_param)
               
   
   def generate_function_code(self, name, params, operation, file):
      #Create funciton using the operation found in the domain description
      #Ask user for function name
      self.write.create_function(name, params, operation, file)

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




               
