#Part 1 - Look through domains for matching operation, e.g. add in math domain
#Part 2 - Look for potential perameters, ask user for sample input
#Part 3 - Consider if there is an extension, e.g. add then mulitply
#Part 4 - Consider if the user wants more than one program, e.g. add two numbers and multiply two numbers

from TextAnalysis import TextAnalysis as TA
from JSON import JSON
from Py_Write import PyCreate as PC

class Rules():

   json = JSON()
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
      else:
         return "No text"

   def domain_search(text):
      
      

if __name__ == '__main__':
    rules = Rules()
    test = rules.analyse("I want a program to add two numbers togther.")
    #print(test)
