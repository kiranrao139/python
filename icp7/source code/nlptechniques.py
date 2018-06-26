import urllib.request
from bs4 import BeautifulSoup
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk import pos_tag, ne_chunk, wordpunct_tokenize, ngrams
from nltk.stem import PorterStemmer, WordNetLemmatizer

# Assigning link to a variable
myLink = "https://en.wikipedia.org/wiki/Python_(programming_language)"
f3 = open("output.txt","w")
f3.write("")
f3.close()

f = open("output.txt", "w+", encoding="utf=8")


# Opens the URL
getLink=urllib.request.urlopen(myLink)

# Converts to HTML
soup = BeautifulSoup(getLink,  "html.parser")
f.write(soup.get_text())
f.close()

outputfile = open("output.txt","r", encoding = "utf-8")
textfile = outputfile.read()


# Tokenization
sent_tokens = sent_tokenize(textfile)
word_tokens = word_tokenize(textfile)

print(sent_tokens)
print("\n")
print("\n")
print(word_tokens)

print("\n")

# stemming
Pstemmer = PorterStemmer()
print(Pstemmer.stem(textfile))

print("\n")

# Lemmatization
lemmatizer = WordNetLemmatizer()
print(lemmatizer.lemmatize(textfile))

print("\n")

# Parts of speech tagging
text1 = word_tokenize(textfile)
print(pos_tag(text1))

print("\n")

# Named Entity Recognition
sent = "kiran are yuvesh are studying in umkc."
print(ne_chunk(pos_tag(wordpunct_tokenize(sent))))

print("\n")

# Trigram
#sent = "kiran are yuvesh are studying in umkc."
text2 = word_tokenize(textfile)
trigram = ngrams(text2,3)
for t in trigram:
    print(t)



