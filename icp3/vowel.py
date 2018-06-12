string=input("enter the string to count the number of vowels ")

# initially number of vowels assigned to zero
number_of_vowels=0

# vowels( a,e,i,o,u ) will be comapared individually with the words in the given sentence

number_of_vowels += string.count("a")
number_of_vowels += string.count("e")
number_of_vowels += string.count("i")
number_of_vowels += string.count("o")
number_of_vowels += string.count("u")

print(" number of vowels is:", number_of_vowels)