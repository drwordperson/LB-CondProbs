# If you are using Windows, and getting errors about the character encoding, you may need to set the environment variable PYTHONUTF8=1 from the command line first.
import re

# Open a language-specific config file because we need a list of consonants and vowels.

configfile = input("Language-specific corpus config file:")

with open(configfile) as letsdothis:
    exec(letsdothis.read())

# Generate list of all possible V and CV characters

pairs = []
for i in range(len(vowels_l)):
    k = '-' + vowels_l[i] + '-'
    pairs.append(k)

for i in range(len(consonants_l)):
    for j in range(len(vowels_l)):
        k = '-' + consonants_l[i] + vowels_l[j] + '-'
        pairs.append(k)

print(pairs)

#Make a list of words -> call this words_l.  Get the length of words (= the total number of words), call it words_len.

words_l = []

p = f'({whitespace})(\\S+)({whitespace})'
pattern = re.compile(p)
matches = pattern.findall(text)
for match in matches:
    words_l.append(' -' + match[1] + '- ')
    
words_len = len(words_l)

# Now, we are going to define a number of functions for operations we will use repeatedly.

# (1)  This function takes a wordlist, finds words that contain a pair (you can supply whatever complex conditions you want), and outputs a dictionary of the form pair: list of words containing pair (given the conditions you supplied).
#      PairsInWords_d is the output
def FindWords(regex, wordlist): # condition needs to be put in single quotes, e.g. AUB('pairA').  words_l is probably the wordlist you want to use most.
    for pairA in pairs: #Pick a pair from the list of pairs
        output_list = [] #We're opening the list that'll get put in the dictionary
        for word in wordlist: #Now we're going through every word in the list of words
            condition = re.sub('pair', pairA, regex)
            p = f'({condition})' #We're looking for the pattern pairA in that word.  SO THIS IS THE PART YOU SUPPLY IN ADVANCE
            pattern = re.compile(p) #Compile that pattern
            match = re.search(pattern, word) #Search for the pattern 
            if match != None: #Everything from here on out puts the word in the list
                output_list.append(word)
            else:
                 continue
        PairsInWords_d[pairA] = output_list


# (2)  Now we're going to define a function for generate a dictionary with the form pair: [list of words containing pair].
#      PairsInWords_len is the output
def LenDic(dictionary):
    for key, value in dictionary.items():
        l = len(value)
        PairsInWords_len[key] = l
        

#  (3)  Another function for making dictionaries!  This time the dictionary for words containing A U B.  It takes as input a dictionary with the form pair: [list of words containing pair]
#       UPairsInWords_d is the output
def FindWordsAUB(regex, dictionary):
    for key, value in dictionary.items():
        for pairA in pairs:
            output_list = []    
            for word in value:
                        condition = re.sub('pair', pairA, regex)
                        p = f'({condition})'
                        pattern = re.compile(p)
                        match = re.search(pattern, word)  
                        if match != None:
                            output_list.append(word)
                        else:
                            continue
            k = key + 'U' + pairA
            UPairsInWords_d[k] = output_list


#  (4)  This function contains the actual conditional probability calculation.  Conditional probability of A given B = P(A U B) / P(B) Output is  a dictionary containing AUB: conditional probability value.
#       CondProb_d is the output
def CondProb(UDatabase_len, Database_len):
    for key, value in UDatabase_len.items():
        k = key.split('U') # Here we're grabbing the right B.  This should create a string with two entries, which are A and B.
        k1 = k[1] # The second one of those two is B and we'll need it for the next step
        n = Database_len[k1] # Grab the dictionary value for the appropriate B
        try:
            c = (value/words_len)/(n/words_len)
            CondProb_d[key] = c
        except ZeroDivisionError: # If B is zero, which is a fairly common occurrence
            CondProb_d[key] = 0
     

# Co-occurrence within the same word:  conditional probability of pair A given pair B.     
     
PairsInWords_d = {}
regex = 'pair'
FindWords(regex, words_l)

PairsInWords_len = {}
LenDic(PairsInWords_d)
PPairsInWords_len = PairsInWords_len # Rename the dictionary so that it does not get overwritten when we perform this operation again.

UPairsInWords_d = {}
regex = 'pair'
FindWordsAUB(regex, PairsInWords_d)
     
PairsInWords_len = {}  # Time to perform the length function on this new dictionary.
LenDic(UPairsInWords_d)
UPairsInWords_len = PairsInWords_len # Again, rename the dictionary to avoid confusion.

CondProb_d = {}
CondProb(UPairsInWords_len, PPairsInWords_len)

with open("CondProbSameWord.txt", 'w') as f:  
    for key, value in CondProb_d.items():  
        f.write('%s:%s\n' % (key, value))



