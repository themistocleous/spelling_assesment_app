import os
import re
import math
import string
import sys
import getopt
import numpy as np
import pandas as pd
from scipy import interp
from collections import Counter
from toipa import phonetic
import warnings

# To ignore code warnings at the output. Deactivate this if you modify the code.
warnings.filterwarnings("ignore")


def levenshtein(source, target):
    source_word = range(len(source) + 1)
    target_word = range(len(target) + 1)
    mtable = [[(i if j == 0 else j) for j in target_word] for i in source_word]
    for i in source_word[1:]:
        for j in target_word[1:]:
            deletion_dist = mtable[i - 1][j] + 1
            insertion_dist = mtable[i][j - 1] + 1
            sub_trans_cost = 0 if source[i - 1] == target[j - 1] else 1
            substition_dist = mtable[i - 1][j - 1] + sub_trans_cost
            mtable[i][j] = min(deletion_dist, insertion_dist, substition_dist)
            if i > 1 and j > 1 and source[i - 1] == target[j - 2] \
                    and source[i - 2] == target[j - 1]:
                trans_dist = mtable[i - 2][j - 2] + sub_trans_cost
                mtable[i][j] = min(mtable[i][j], trans_dist)
    distance = mtable[len(source)][len(target)]
    return float(distance) / max(len(source), len(target))


def rdlevenshtein(row):
    return levenshtein(str(row['target']), str(row['response']))


def replacest(text):
    text = text.strip()
    chars = " ˌːˈ\n"
    for symb in text:
        if symb in chars:
            text = text.replace(symb, "")
    return text


def rdlevenshteinphonetics(row):
    t = phonetic(str(row['target']))
    t1 = replacest(t)
    r = phonetic(str(row['response']))
    r1 = replacest(r)
    return levenshtein(t1, r1)


def spellingdistance(FILE):
    """Calculate spelling distance"""
    DF = pd.read_csv(FILE)
    DF['target'] = DF.target.str.lower()
    DF['response'] = DF.response.str.lower()
    DF['type'] = DF.type.str.lower()
    DF['target'] = DF['target'].str.replace(" ", "")
    DF['response'] = DF['response'].str.replace(" ", "")
    DF['type'] = DF['type'].str.replace(" ", "")
    DF['target'] = DF['target'].str.strip()
    DF['response'] = DF['response'].str.strip()
    DF['type'] = DF['type'].str.
    EMPTY = DF[DF.response.isna()]
    DF = DF[DF.response.notnull()]
    NW = DF[DF.type == "nonword"]
    W = DF[DF.type == "word"]
    if NW.empty == False:
        NW['spelling_score'] = NW.apply(rdlevenshteinphonetics, axis=1)
    if W.empty == False:
        W['spelling_score'] = W.apply(rdlevenshtein, axis=1)
    EMPTY['spelling_score'] = "NA"
    newdf = pd.concat([NW, W, EMPTY], axis=0)
    return newdf


def main(argv):
    inputfile = ''
    outputfile = ''
    try:
        opts, args = getopt.getopt(argv, "hi:o:", ["ifile=", "ofile="])
    except getopt.GetoptError:
        print('python spelling.py -i <inputfile> -o <outputfile>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('python spelling.py -i <inputfile> -o <outputfile>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            FILE = arg
            out = spellingdistance(FILE)
        elif opt in ("-o", "--ofile"):
            outputfile = arg
            out.to_csv(outputfile)
            print("Spelling run without errors")


if __name__ == "__main__":
    main(sys.argv[1:])
