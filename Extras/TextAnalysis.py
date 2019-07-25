from nltk.tokenize import sent_tokenize as sentences
from nltk.tokenize import word_tokenize as words
from nltk.corpus import stopwords
from nltk.corpus import wordnet as wn

import string

class TextAnalysis():
    
    def synonym(self, word):
        
        syns = []
        
        for syn in wn.synsets(word):
            for lemma in syn.lemmas():
                syns.append(lemma.name())
                
        return set(syns)
            
    def similarity(self, word1, word2):

        #Convert string into sysnet object to get full lemma
        word1_syns = wn.synsets(word1)
        word2_syns = wn.synsets(word2)
        sim = 0
        
        if word1_syns and word2_syns:

            #Convert sysnet objects into string arrays
            word1_string = [s.name() for s in word1_syns]
            word2_string = [s.name() for s in word2_syns]

            #Garner the sysnet for simialrity score
            word1_lemma = wn.synset(word1_string[0])
            word2_lemma = wn.synset(word2_string[0])
            
            sim = word1_lemma.wup_similarity(word2_lemma)

        return sim

    def stop_words(self, tokens):
        
        stop_words_en = set(stopwords.words('english'))
        filtered = []

        for word in tokens:
            
          if word not in stop_words:
            filtered.append(word)
            
        return filtered

    def tokenize_text(self, text):
        token_text = sentences(text)
        return token_text
    
    def tokenize_sentence(self, sentence):
        token_sentence = words(sentence)
        return token_sentence

    def remove_punctuation(self, text):
        clean_text = text.translate(str.maketrans('', '', string.punctuation))
        return clean_text
    
    def lower_capital(self, text):
        text = text.lower()
        return text
    
    def combine_text(self, tokens_one, tokens_two):
        for token in tokens_one:
            if token not in tokens_two:
                tokens_two.append(token)
        return tokens_two
    
    
if __name__ == '__main__':
    pass
    
