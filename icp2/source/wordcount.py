fname = input("Enter file name: ")



with open(fname, 'r') as f:
    for line in f:
        num_words = 0
        words = line.split()
        num_words = len(words)

        print(line[:-1] +"," +str(num_words))