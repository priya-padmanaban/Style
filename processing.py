#!/usr/bin/env python
from __future__ import division
import nltk
import zipfile
import argparse
import sys
from nltk.corpus import inaugural
import csv
import pandas as pd
from sklearn import preprocessing, ensemble
from sklearn.externals import joblib


###############################################################################
## Utility Functions ##########################################################
###############################################################################
# This method takes the path to a zip archive and reads the raw contents of the
# file.

def unzip_corpus(input_file):
    zip_archive = zipfile.ZipFile(input_file)
    contents = [zip_archive.open(fn, 'rU').read().decode('utf-8') for fn in zip_archive.namelist() if
                fn.endswith(".txt")]
    return contents

def read_txt(input_file):
    contents = input_file.read().decode('utf-8')
    return contents


###############################################################################
## Stub Functions #############################################################
###############################################################################
def process_corpus(corpus_name):
    input_file = corpus_name + ".zip"
    corpus_contents = unzip_corpus(input_file)

    totalwords = []
    totalsent = []
    totaltags = []
    sentcount = 0

    for doc in corpus_contents:
        sentences = nltk.sent_tokenize(doc)

        for sentence in sentences:
            totalsent.append(sentence)
            sentcount = sentcount + 1
            words = nltk.word_tokenize(sentence)
            for word in words:
                totalwords.append(word)
            tagged = nltk.pos_tag(words)
            for tag in tagged:
                totaltags.append(tag)
                string = nltk.tuple2str(tag)

        waverage = sum(len(word) for word in totalwords) / len(totalwords)
        wtrunc = '%.3f'%(waverage)
        saverage = len(totalwords) / sentcount
        strunc = '%.3f'%(saverage)

    NNtags = []
    VBDtags = []
    JJtags = []
    RBtags = []
    punctags = []
    for x in totaltags:
        if x[1] == 'NN':
            NNtags.append(x)
        elif x[1] == 'VBD':
            VBDtags.append(x)
        elif x[1] == 'JJ':
            JJtags.append(x)
        elif x[1] == 'RB':
            RBtags.append(x)
        elif x[1] == "." or "," or ";" or "-":
            punctags.append(x)

    punctratio = len(punctags)/len(totalwords)
    NNratio = len(NNtags)/len(totalwords)
    VBDratio = len(VBDtags)/len(totalwords)
    JJratio = len(JJtags)/len(totalwords)
    RBratio =len(RBtags)/len(totalwords)

    NNratio = NNratio*100
    ntrunc = '%.3f'%(NNratio)
    VBDratio = VBDratio*100
    vtrunc = '%.3f'%(VBDratio)
    JJratio = JJratio*100
    jtrunc = '%.3f'%(JJratio)
    RBratio = RBratio*100
    rtrunc = '%.3f'%(RBratio)

    open('user.csv', 'w').close() #erase file

    download_dir = "user.csv"
    csv = open(download_dir, "a")
    columnTitleRow = "author,avgword,avgsent,punctratio,nnratio,vbdratio,rbratio,jjratio\n"
    csv.write(columnTitleRow)
    row = "user," + str(waverage) + "," + str(saverage) + "," + str(punctratio) + "," + str(NNratio) + "," + str(VBDratio) + "," + str(RBratio) + "," + str(JJratio) + "\n"
    csv.write(row)
    csv.close()

    test_file = "user.csv"
    df1 = pd.read_csv(test_file, header = 0)
    test_data = df1.iloc[:,1:]
    model2 = joblib.load("file.pkl")
    preds2 = model2.predict(test_data)

    response = []
    response.append(preds2[0])
    response.append(str(wtrunc))
    response.append(str(strunc))
    response.append(str(ntrunc) + "%")
    response.append(str(vtrunc) + "%")
    response.append(str(jtrunc) + "%")
    response.append(str(rtrunc) + "%")
    print(response)

    print(preds2[0])

    return(response)


###############################################################################
## Program Entry Point ########################################################
###############################################################################
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Style')
    parser.add_argument('--corpus', required=True, dest="corpus", metavar='NAME',
                        help='Which corpus to process')

    args = parser.parse_args()
    corpus_name = args.corpus
    process_corpus(corpus_name)
