# Automatic Analysis of Spelling


The evaluation of spelling performance in aphasia reveals deficits in written language and can facilitate the design of targeted writing treatments. Nevertheless, manual scoring of spelling performance is time-consuming, laborious, and error prone. Here we provide a code that scores spelling errors based on the normalized Damerau–Levenshtein distance, for both words and non words.

# Using the code

## Prerequisites

1. Install espeak, a free open source text to speech software: http://espeak.sourceforge.net
2. Install Anaconda with Python 3: https://www.anaconda.com/products/individual

The required packages pandas, scipy, and numpy, will be installed automatically.

## Data Preparation for analysis

1. You will need a datafile in csv format with three columns titled: **target**, **response**, and **type**. If you have only words, you will still need the column **type** with labels *word*.


| target | response | type |
| - | - | - |
| skart | skart | nonword |
| feen | feen | nonword |
| strict | strict | word |
| faith | gace | word |

If you there are other columns in the excel file these will not be deleted during the process. However, the order of rows might change so, it is a good practice to have an ID column to function as an index, so that you can sort the excel to its original form.

2. Place the file with the data, at the folder that contains the code.
3. Open the Terminal and cd to the directory that contains the code and run the following command

`python spelling.py -i data.csv -o output.csv 

Above I assume that your data file is titled data.csv and the output file is called output.csv. You can name these files as you like but they need to be in a csv format. A file labelled output.csv will be created in the same location.

## Using the code in other languages

You can use the same code to spell check spelling in langauges other than American English, however you will need to modify, line 10 and change the language "en-us" to your own language (shown in column Language in the following table). For example if you want to score words in German you will need to modify

p = subprocess.run(["espeak", "-q", "--ipa", "-v", "en-us"]

to 

p = subprocess.run(["espeak", "-q", "--ipa", "-v", "de"]

Do not forget to save the file after you make the change.


# Help and support

Please do not hesitate to contact me if you get into problems running the code, or if you have questions, suggestions, etc. If you use the code do not forget to cite the paper Themistocleous et al. 2020.


# Cite

**Themistocleous, Charalambos**, Neophytou, Kyriaki, Rapp, Brenda, & Tsapkini, Kyrana (2020). A Tool for Automatic Scoring of Spelling Performance. Journal of Speech, Language, and Hearing Research. doi:10.1044/2020_JSLHR-20-00177
