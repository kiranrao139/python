sentence = input('Please enter your sentence: ')
sentWords = [str(word) for word in sentence.split(' ')]
# all the words in the sentence are splitted

finalList = {}
# an empty dictionary

for wrd in sorted(sentWords):
    if wrd in finalList:
        finalList[wrd] = finalList[wrd]+1
    # Else, we are just setting the count as '1'
    else:
        finalList[wrd] = 1
        # wrd as well as frequency is updated in the finalList

# Printing Final List
print("Output : ",finalList)
