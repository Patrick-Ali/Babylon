#Part 1 - Look through domains for matching operation, e.g. add in math domain
#Part 2 - Look for potential perameters, ask user for sample input
#Part 3 - Consider if there is an extension, e.g. add then mulitply
#Part 4 - Consider if the user wants more than one program, e.g. add two numbers and multiply two numbers

from TextAnalysis import TextAnalysis as TA
from JSON import JSON
from Py_Write import PyCreate as PC

class Rules():

   reader = JSON()
   text_analysis = TA()
   write = PC()

   def analyse(self, text):
      sentences = self.text_analysis.tokenize_text(text)
      
      if len(sentences) > 0:
         for sentence in sentences:
            clean_text = self.text_analysis.lower_capital(sentence)
            #print(clean_text)
            depunctuated_text = self.text_analysis.remove_punctuation(clean_text) # For synonyms
            #print(depunctuated_text)
            tokens_one = self.text_analysis.tokenize_sentence(clean_text)
            #print(tokens_one)
            tokens_two = self.text_analysis.tokenize_sentence(depunctuated_text)
            #print(tokens_two)
            combine_text = self.text_analysis.combine_text(tokens_one, tokens_two)
            #print(combine_text)
            possible_operations = self.domain_search(combine_text)
            #print(possible_operations)
            if len(possible_operations) > 0 and len(possible_operations) < 2:
               domain = possible_operations[0][0]
               operation = possible_operations[0][1]
               #print(domain + "\n" + operation)
               specifics = self.operation_specifics(domain, operation)
               print(specifics)
               params_text = input("""Please provide smaple input, e.g. for
               'I want a program to add two numbers togther.'
                the input would be '1, 2'. Use comma (,) to denote each input. \n
                Enter input samples: """ )
               params_split = params_text.split(",")
               sample_param = []
               for param in params_split:
                  sample_param.append(param)
               params = []
               for i in range(len(sample_param)):
                  param = "param_"+str(i)
                  params.append(param)
               print(params)
               if len(params) > 0:
                  
                  self.domain_analysis(specifics, params, sentence, sample_param)
                  
               #print(sample_param)
               #domain_analysis()
               # Ask user for sample input, 'No Input' for no perameters
               #sample_input = []
            elif len(possible_operations) > 2:
               pass
               #Ask user to chose between possible soloutions
               #Potential automation of similarity between sentences
            else:
               pass
               #Tell user we are not sure what they want,
               #Ask to rephrase or look at operation list
      else:
         return "No text"

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
            #print(hold)
            if key in text:
               match.append((domain, key))
      return match

   def domain_analysis(self, text, params, description, sample_param):
      clean_text = self.text_analysis.lower_capital(text)
      depunctuated_text = self.text_analysis.remove_punctuation(clean_text)#
      operation = self.code_search(depunctuated_text)
      print("Here 1")
      print(operation)
      if len(operation) > 0 and len(operation) < 2: #Temp till multi operations supported
         print("Here 2")
         print(depunctuated_text)
         if "function" in depunctuated_text:
            file = input("What do you want to call the program? \n Enter name: ")
            file = self.text_analysis.lower_capital(file)
            self.add_program(file, description)
            #Lower name from capitals
            self.generate_function_code(file, params, operation[0], (file+".py"))
            self.run_program(file, sample_param)
            self.run_pro("run_pro.py")
            #ask user for file name
   
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

      self.write.write_line("run_pro.py", line)
      
   def add_program(self, name, description):
      data = self.get_data()
      data[name] = description
      self.reader.addData("programs", data)
      
   def run_pro(self, file):
      result = self.write.call_py(file)
      print(result)
      return result
      

if __name__ == '__main__':
   #Testing
   rules = Rules()
   test = rules.analyse("I want a program to add two numbers togther.")
   #print(test)
