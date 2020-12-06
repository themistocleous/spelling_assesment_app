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


| Pty | Language | Age/Gender | VoiceName | File | Other Languages |
| - | - | - | - | - | - |
| 5 | af | M | afrikaans | other/af |   |
| 5 | an | M | aragonese | europe/an |   |
| 5 | bg | - | bulgarian | europe/bg |   |
| 5 | bs | M | bosnian | europe/bs |   |
| 5 | ca | M | catalan | europe/ca |   |
| 5 | cs | M | czech | europe/cs |   |
| 5 | cy | M | welsh | europe/cy |   |
| 5 | da | M | danish | europe/da |   |
| 5 | de | M | german | de |   |
| 5 | el | M | greek | europe/el |   |
| 5 | en | M | default | default |   |
| 2 | en-gb | M | english | en | (en-uk 2)(en 2) |
| 5 | en-sc | M | en-scottish | other/en-sc | (en 4) |
| 5 | en-uk-north | M | english-north | other/en-n | (en-uk 3)(en 5) |
| 5 | en-uk-rp | M | english_rp | other/en-rp | (en-uk 4)(en 5) |
| 5 | en-uk-wmids | M | english_wmids | other/en-wm | (en-uk 9)(en 9) |
| 2 | en-us | M | english-us | en-us | (en-r 5)(en 3) |
| 5 | en-wi | M | en-westindies | other/en-wi | (en-uk 4)(en 10) |
| 5 | eo | M | esperanto | other/eo |   |
| 5 | es | M | spanish | europe/es |   |
| 5 | es-la | M | spanish-latin-am | es-la | (es-mx 6)(es  6) |
| 5 | et | - | estonian | europe/et |   |
| 5 | fa | - | persian | asia/fa |   |
| 5 | fa-pin | - | persian-pinglish | asia/fa-pin |   |
| 5 | fi | M | finnish | europe/fi |   |
| 5 | fr-be | M | french-Belgium | europe/fr-be | (fr  8) |
| 5 | fr-fr | M | french | fr | (fr 5) |
| 5 | ga | - | irish-gaeilge | europe/ga |   |
| 5 | grc | M | greek-ancient | other/grc |   |
| 5 | hi | M | hindi | asia/hi |   |
| 5 | hr | M | croatian | europe/hr | (hbs 5) |
| 5 | hu | M | hungarian | europe/hu |   |
| 5 | hy | M | armenian | asia/hy |   |
| 5 | hy-west | M | armenian-west | asia/hy-west | (hy 8) |
| 5 | id | M | indonesian | asia/id |   |
| 5 | is | M | icelandic | europe/is |   |
| 5 | it | M | italian | europe/it |   |
| 5 | jbo | - | lojban | other/jbo |   |
| 5 | ka | - | georgian | asia/ka |   |
| 5 | kn | - | kannada | asia/kn |   |
| 5 | ku | M | kurdish | asia/ku |   |
| 5 | la | M | latin | other/la |   |
| 5 | lfn | M | lingua_franca_nova | other/lfn |   |
| 5 | lt | M | lithuanian | europe/lt |   |
| 5 | lv | M | latvian | europe/lv |   |
| 5 | mk | M | macedonian | europe/mk |   |
| 5 | ml | M | malayalam | asia/ml |   |
| 5 | ms | M | malay | asia/ms |   |
| 5 | ne | M | nepali | asia/ne |   |
| 5 | nl | M | dutch | europe/nl |   |
| 5 | no | M | norwegian | europe/no | (nb 5) |
| 5 | pa | - | punjabi | asia/pa |   |
| 5 | pl | M | polish | europe/pl |   |
| 5 | pt-br | M | brazil | pt | (pt 5) |
| 5 | pt-pt | M | portugal | europe/pt-pt | (pt 6) |
| 5 | ro | M | romanian | europe/ro |   |
| 5 | ru | M | russian | europe/ru |   |
| 5 | sk | M | slovak | europe/sk |   |
| 5 | sq | M | albanian | europe/sq |   |
| 5 | sr | M | serbian | europe/sr |   |
| 5 | sv | M | swedish | europe/sv |   |
| 5 | sw | M | swahili-test | other/sw |   |
| 5 | ta | M | tamil | asia/ta |   |
| 5 | tr | M | turkish | asia/tr |   |
| 5 | vi | M | vietnam | asia/vi |   |
| 5 | vi-hue | M | vietnam_hue | asia/vi-hue |   |
| 5 | vi-sgn | M | vietnam_sgn | asia/vi-sgn |   |
| 5 | zh | M | Mandarin | asia/zh |   |
| 5 | zh-yue | M | cantonese | asia/zh-yue | (yue 5)(zhy 5) |


# Help and support

Please do not hesitate to contact me if you get into problems running the code, or if you have questions, suggestions, etc. If you use the code do not forget to cite the paper Themistocleous et al. 2020.


# Cite

**Themistocleous, Charalambos**, Neophytou, Kyriaki, Rapp, Brenda, & Tsapkini, Kyrana (2020). A Tool for Automatic Scoring of Spelling Performance. Journal of Speech, Language, and Hearing Research. doi:10.1044/2020_JSLHR-20-00177
