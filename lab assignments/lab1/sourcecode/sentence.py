sent = input("enter the sentence : ")
# splitting all the words in the sentence
words = sent.split()

# finding the length of each word
sent_len = len(words)

# sorting the words based on their length
sorted_sent = sorted(words,key=len)

# printing the longest word
print("longest word is : ", sorted_sent[-1])

# If the remainder is zero, It prints two words from the middle as the no. of words are even
if sent_len%2 == 0:
    mid_index = sent_len/2
    print("middle values are : ", words[int(mid_index - 1)], words[int(mid_index)])

# If the no. of words are odd, it prints the only one middle word
else:
    mid_index = sent_len/2
    print("middle value is : ", words[int(mid_index)])

# created an empty list
revlist = []
for word in words:
    # reversing each word from the sentence by iterating the loop
    revlist.append(word[::-1])
revtext = " ".join(revlist)

print("The given sentence with reversing all the words : ",revtext)