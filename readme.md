## Overview

```LB-CondProbs.py``` takes a language corpus in a syllabic (V and CV signs) script and calculates the conditonal probability that a given syllabic sign appears given that another syllabic sign is found in that same word. 

This Python script outputs a .txt file with the conditional probabilities calculated for all pairs of signs.  

## Usage

```python LB-CondProbs.py```

For language-specific processing, ```LB-CondProbs.py``` takes a configuration file-- a Python script which lays out the valid consonants and vowels which appear in the corpus of the language in question.  ```LB-CondProbs.py``` also takes a .txt file containing the section of text you would like to use as a corpus.  A config file and data set has been provided for German, and a sample output is as follows.

#### German:

-	-a-U-ca-:0.11851851851851851
-	-a-U-cä-:0
-	-a-U-ce-:0.06711409395973153
-	-a-U-ci-:0.27419354838709675
-	-a-U-co-:0.11290322580645162
-	-a-U-cö-:0
-	-a-U-cu-:0.041666666666666664
-	-a-U-cü-:0
-	-a-U-cy-:0.0625

## Planned Improvements

Wider range of languages.  Conditions include both directionality and adjacency.  Output is a .csv file rather than a Python dictionary.

## Disclaimer

Currently, this script is only made available as a code sample.  Many points of linguistic complexity are elided, and there is still some room to improve the accuracy of the script when it comes to acronyms and foreign words.  Please don't publish with this script!  You have been warned.

## Attribution

This script was developed by Christina Skelton.  Special thanks to Sherrylyn Branchaw and Marvin Martiny for troubleshooting assistance.  

Input data is taken from ```Alphabet-to-Linear-B.py``` and the [Leipzig Corpora Collection](https://corpora.uni-leipzig.de/).
