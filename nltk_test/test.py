from nltk.tokenize import sent_tokenize as sentences
from nltk.tokenize import word_tokenize as words
from nltk import pos_tag
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet as wn
import string

def synonym(word):
    syns = []
    for syn in wn.synsets(word):
        for l in syn.lemmas():
            syns.append(l.name())
    return set(syns)

def similarity(word1, word2):
    #print("Here 1")
    print("Word 1: " + word1)
    print("Word 2: " + word2)
    w1 = wn.synsets(word1)
    #print(w11)
    w2 = wn.synsets(word2)
    #print(w22)
    sim = 0
    if w1 and w2:
        w1Str = [s.name() for s in w1]
        w2Str = [s.name() for s in w2]
        w11 = wn.synset(w1Str[0])
        w22 = wn.synset(w2Str[0])
        sim = w11.wup_similarity(w22)
        
        #print("Word 1: " + word1)
        #print("Synsnet: " + w111[0])
        #print("Word 2: " + word2)
        #print("Synsnet: " + w222[0])
    #w1 = wn.synset('ship.n.01')
    #w2 = wn.synset('cat.n.01')
    return sim
    
    
lemmatizer = WordNetLemmatizer()

ps = PorterStemmer()

stop_words = set(stopwords.words('english'))
#print(sorted(stop_words, key=str.lower))
#print('\n')

test = """Hello Mr. Smith, how are you doing today?
    The weather is great, and Python is awesome.
    The sky is pinkish-blue. You shouldn't
    eat cardboard."""

##Break input into sentences
st = sentences(test)

print("Sentences: ")
print(st)
print("Number of sentences: " + str(len(st)))
print('\n')

##Cycle through sentences and break each it into words
for sentence in st:
    filtered = []
    s = sentence
    s = s.translate(str.maketrans('', '', string.punctuation))
    tokens = words(s)
    print("Words in sentence: ")
    #print(len(tokens))
    print(tokens)
    #print('\n')
    tagged = pos_tag(tokens)
    #print("Word Part Of Speech tags: ")
    #print(tagged)
    #print('\n')
    ##Checking against set of stop words, e.g. hers
    count = 0
    for word in tokens:
        #print(ps.stem(word))
        #lem = lemmatizer.lemmatize(word, tagged[count][1])
        #print(lem)
        #print(tagged[count][1])
        if count > 0 and count < len(tokens):
            sim = similarity(word, tokens[count-1])
            print('\n')
            print("Similarity: " + str(sim))
            print('\n')
        count += 1
        #print("Word: " + word)
        sys = synonym(word)
        #print("Synonims: ")
        #print(sys)
        #print('\n')
        if word not in stop_words:
            filtered.append(word)
    #print(filtered)
