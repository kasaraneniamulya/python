from bs4 import BeautifulSoup
from bs4.element import Comment
import urllib.request
import collections
def tag_visible(element):
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False
    if isinstance(element, Comment):
        return False
    return True
#loading visible text vy avoiding all the tags in input.txt
def text_from_html(body):
    soup = BeautifulSoup(body, 'html.parser')
    texts = soup.findAll(text=True)
    visible_texts = filter(tag_visible, texts)
    return u" ".join(t.strip() for t in visible_texts)


html = urllib.request.urlopen('https://en.wikipedia.org/wiki/Python_(programming_language)').read()
f = open('input.txt', 'w', encoding='utf-8')
f.write(text_from_html(html))
f.close()

# reading the input.txt file
data = open('input.txt', encoding='utf-8').read() #loading the visible text into a variable called data
# tokenizing
from nltk.tokenize import *

sentences = data
# sentence tokenizing
sentence_tokens = sent_tokenize(sentences) #breaking the text file into sentences
# word tokenizing
word_tokens = word_tokenize(sentences) #breaking the text file into words
print("Sentence tokenizing")
for sentence in sentence_tokens:
    print(sentence)
print("Word tokenizing")
for word in word_tokens:  #printing words without special symbols
    if not re.search("[($@!:.,'^-_)]", word):
        print(word)

# stemming
from nltk.stem import *

print("Stemming")
ps = PorterStemmer()
ss = SnowballStemmer('english')
ls = LancasterStemmer()
sentences = data
sentence = sent_tokenize(sentences)[4] #considering fourth sentence in the text file
words = word_tokenize(sentence)
for word in words:
    if not re.search("[($@!:.,'^-_)]", word):
        print(word + ":" + ps.stem(word))  #gives root word for given words
        print(word + ":" + ss.stem(word))
        print(word + ":" + ls.stem(word))

# Lemmatization
print("Lemmatization")
lemmatizer = WordNetLemmatizer()
sentence = sent_tokenize(sentences)[4]
words = word_tokenize(sentence)
for word in words:
    if not re.search("[($@!:.,'^-_)]", word):
        print(word + ":" + lemmatizer.lemmatize(word, 'a')) # gives root word for the given word based on parts of speech


# parts of speech
from nltk import pos_tag
print("Parts of speech") #printing parts of speech for all the words in 4th sentence
print(pos_tag(words))

# Name Entity Recognition
from nltk import ne_chunk
print("Name Entity Recognition") #apple has 2 meanings it gives both meanings
print(ne_chunk(pos_tag(words)))

# Trigram
from nltk import trigrams
print("Trigrams")
print(list(trigrams(words)))
triWORD_COUNTS = collections.Counter(list(trigrams(words))) #it gives three three words as one word
print(triWORD_COUNTS)