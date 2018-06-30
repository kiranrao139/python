import itertools

from nltk.stem import WordNetLemmatizer
from nltk.util import bigrams
from nltk.tokenize import sent_tokenize, word_tokenize

with open('output2.txt', 'r') as readFile: #open file we want to read
    text = readFile.read() #save text from file

    textSentence = sent_tokenize(text) #make tokenize sentence
    textWord = word_tokenize(text) #make tokenize words
    Lemmatize = WordNetLemmatizer()
    lemmatizedText = [] #initialize new text list for lemmatized words

    #
    for w in textWord:
        lemmatizedText.append(Lemmatize.lemmatize(w))


    lemTextBiGram = list(bigrams(lemmatizedText))

    bigramFreq = dict() #create a dicitonary to store a frequency next to a number
    for bigram in lemTextBiGram:
        if bigram not in bigramFreq:
            bigramFreq.update({bigram:1})
        elif bigram in bigramFreq: #else if bigram in the dictionary
            # then add one to the frequency instead of adding it to the dictionary
            bigramFreq[bigram] = bigramFreq[bigram] + 1


    #https://www.pythoncentral.io/how-to-sort-python-dictionaries-by-key-or-value/
    sortedBigramFreq=sorted(bigramFreq, reverse = True, key = bigramFreq.__getitem__) #sort the dicitonary
    top5 = sortedBigramFreq[0:5] #get the top five bigrams



    #check for duplicate sentences/make duplicates impossible by deleting if found
    bigramSentences = []
    top5String = []

    #turn top 5 bigrams into strings instead of tuples
    for bigram in top5:
        for sentence in textSentence:
            newSentence = list(bigrams(word_tokenize(sentence)))
            if bigram in newSentence:
                bigramSentences.append(sentence)
                textSentence.remove(sentence)

    #concatenate the list of sentences
    concatenate = " ".join(bigramSentences)
    print("\nlemmatization:")
    print(lemmatizedText) # printing lemmetised words
    print("\nfreqemcy of top5:")
    print( dict(itertools.islice(bigramFreq.items(), 5)))#freuency
    print("\nconcaenated text:")
    print(concatenate) # concatination