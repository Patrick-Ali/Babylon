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
   wirte = PC()

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
               #print(specifics)
               # Ask user for sample input, 'No Input' for no perameters
               sample_input = []
            elif len(possible_operations) > 2:
               #Ask user to chose between possible soloutions
               #Potential automation of similarity between sentences
            else:
               #Tell user we are not sure what they want,
               #Ask to rephrase or look at operation list
      else:
         return "No text"

   def operation_specifics(self, domain, operation):
      operation = self.reader.getData(domain, operation)
      return operation
      
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
   
   def generate_code(self, text):
      pass
      

if __name__ == '__main__':
   #Testing
   rules = Rules()
   test = rules.analyse("I want a program to add two numbers togther.")
   #print(test)
