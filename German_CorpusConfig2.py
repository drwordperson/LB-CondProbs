import re
with open('GermanLB.txt', encoding='utf8') as f:
    text = f.read()

vowels = 'a|ä|e|i|o|ö|u|ü|y'
vowels_l = ['a', 'ä', 'e', 'i', 'o', 'ö', 'u', 'ü', 'y']

consonants = 'b|c|d|f|g|h|j|k|l|m|n|p|q|r|s|t|v|w|x|z|φ|χ|ʃ'
consonants_l = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z', 'φ', 'χ', 'ʃ']

stops = 'p|b|t|d|k|g|q'
stops_l = ['p', 'b', 't', 'd', 'k', 'g', 'q']

affrics = 'z|φ'
affrics_l = ['z', 'φ']

frics = 'f|s|v|h|w|χ|ʃ'
frics_l = ['f', 's', 'v', 'h', 'w', 'χ', 'ʃ']

nasals = 'n|m'
nasals_l = ['n', 'm']

liquids = 'l|r'
liquids_l = ['l', 'r']

glides = 'j'
glides_l = ['j']

whitespace = r'\n|\s'

voiceless = ['p', 't', 'k', 'f']
voiced = ['b', 'd', 'g', 'v']