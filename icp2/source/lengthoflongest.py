list=["PHP", "Exercises", "Backend"]
i=0
word_len=[]
for i in range(len(list)):
    listex=[]

    listex.insert(i,str(len(list[i])))
    listex.insert(i+1,list[i])
    word_len.insert(i,listex)
    i+=1
word_len.sort()
print(word_len[-1])
