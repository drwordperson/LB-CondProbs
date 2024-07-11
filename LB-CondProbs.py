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

#Make a list of words -> call this words_l.  Get the length of words (= the total number of words), call it words_len.

words_l = []

p = f'({whitespace})(\\S+)({whitespace})'
pattern = re.compile(p)
matches = pattern.findall(text)
for match in matches:
    words_l.append(' -' + match[1] + '- ')
    
words_len = len(words_l)

#Now we generate a dictionary with the form pair: [list of words in pair].

PairsInWords_d = {}

for pairA in pairs:
    output_list = []
    for word in words_l:
        p = f'({pairA})'
        pattern = re.compile(p)
        match = re.search(pattern, word)  
        if match != None:
            output_list.append(word)
        else:
             continue
    PairsInWords_d[pairA] = output_list
    
#Now another dictionary, this time pair: length of list of words.

PairsInWords_len = {}

for key, value in PairsInWords_d.items():
    l = len(value)
    PairsInWords_len[key] = l
    
#Another dictionary!  The dictionary for words containing A U B.

UPairsInWords_d = {}

for key, value in PairsInWords_d.items():
    for pairA in pairs:
        output_list = []    
        for word in value:
                    p = f'({pairA})'
                    pattern = re.compile(p)
                    match = re.search(pattern, word)  
                    if match != None:
                        output_list.append(word)
                    else:
                        continue
        k = key + 'U' + pairA
        UPairsInWords_d[k] = output_list
        
#Now another dictionary, this time pair: length of list of words.

UPairsInWords_len = {}

for key, value in UPairsInWords_d.items():
    l = len(value)
    UPairsInWords_len[key] = l
    
print(type(UPairsInWords_len))   

#Having done that, let's review the equation for conditional probability.  

#Conditional probability of A given B = P(A U B) / P(B) 

# First, let's make dictionary to store the outcome in.

CondProb_d = {}

# The actual calculation

for key, value in UPairsInWords_len.items():
    k = key.split('U') # Here we're grabbing the right B.  This should create a string with two entries, which are A and B.
    k1 = k[1] # The second one of those two is B and we'll need it for the next step
    n = PairsInWords_len[k1] # Grab the dictionary value for the appropriate B
    try:
        c = (value/words_len)/(n/words_len)
        CondProb_d[key] = c
    except ZeroDivisionError: # If B is zero, which is a fairly common occurrence
        CondProb_d[key] = 0
     
# Write an output file       
with open("output.txt", 'w') as f:  
    for key, value in CondProb_d.items():  
        f.write('%s:%s\n' % (key, value))
        
