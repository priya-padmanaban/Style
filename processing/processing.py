#!/usr/bin/env python
from __future__ import division
import nltk
import zipfile
import argparse
import sys
from nltk.corpus import inaugural
import csv


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

    # testing
    #corpus_contents = input_file.read().decode('utf-8')

    # 1. Tokenizing

    # (a) Write the name of the corpus to stdout
    print("author:", corpus_name)

    # (b) Delimit the sentences for each document in the corpus.

    totalwords = []
    totalsent = []
    totaltags = []
    sentcount = 0

    # POS Tag Output File
    pos_file = open(corpus_name + "-pos.txt", 'w')

    for doc in corpus_contents:
        sentences = nltk.sent_tokenize(doc)

        for sentence in sentences:
            totalsent.append(sentence)
            sentcount = sentcount + 1
            # Tokenize the words in each sentences of each document
            words = nltk.word_tokenize(sentence)
            for word in words:
                totalwords.append(word)

            

            # Part-of-Speech
            tagged = nltk.pos_tag(words)
            for tag in tagged:
                totaltags.append(tag)
                string = nltk.tuple2str(tag)
                print(string, file=pos_file, end=" ")
            print("\n", file=pos_file, end="")
        print("\n", file=pos_file, end="")

        print("word count:", len(totalwords))
        waverage = sum(len(word) for word in totalwords) / len(totalwords)
        print("word avg:", waverage)
        saverage = len(totalwords) / sentcount
        print("sent avg:", saverage)

    pos_file.close()

    # average sentence length
    #for fileid in inaugural.fileids():
    #    avg = sum(len(sent) for sent in inaugural.sents(fileids=[fileid])) / len(inaugural.sents(fileids=[fileid]))
    #    print(fileid, avg)

    # number of total words in the corpus 
    wordCount = 0
    wordCount = len(totalwords)
    #print("2. Total Words in the Corpus:", wordCount)

    # Frequency
    flat_words = [word.lower() for word in totalwords]
    vocabCount = 0
    vocabCount = len(set(flat_words))
    #print("3. Vocabulary Size of the Corpus:", vocabCount)

    tagged_fd = nltk.FreqDist(tag for (word, tag) in totaltags)
    #print("4. The most frequent part-of-speech tag is", tagged_fd.most_common(1))

    # Frequency Output File
    freq_file = open(corpus_name + "-word-freq.txt", 'w')

    fdist = nltk.FreqDist(flat_words)
    print([pair[0] for pair in sorted(fdist.items(), key=lambda item: item[1], reverse=True)], file=freq_file)

    freq_file.close()

    # Conditional Frequency Distribution

    sys.stdout = open(corpus_name + "-pos-word-freq.txt", 'w')

    # Reverse 
    pos_reversed = [(b, a.lower()) for a, b in totaltags]

    cdf1 = nltk.ConditionalFreqDist(pos_reversed)

    cdf1.tabulate()

    sys.stdout = sys.__stdout__

    # Similar Words
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

    print("punctratio:", len(punctags)/len(totalwords))
    print("NNratio:", len(NNtags)/len(totalwords))
    print("VBDratio:", len(VBDtags)/len(totalwords))
    print("JJratio:", len(JJtags)/len(totalwords))
    print("RBratio:", len(RBtags)/len(totalwords))

    download_dir = "authors.csv"
    csv = open(download_dir, "a")
    columnTitleRow = "author,avgword,avgsent,punctratio,nnratio,vbdratio,rbratio,jjratio\n"
    #csv.write(columnTitleRow)
    row = corpus_name + "," + str(waverage) + "," + str(saverage) + "," + str(punctratio) + "," + str(NNratio) + "," + str(VBDratio) + "," + str(RBratio) + "," + str(JJratio) + "\n"
    csv.write(row)

    

    #print("5. The most frequent word in the POS (NN/VBD/JJ/RB) and respective similar words:")

    text = nltk.Text(flat_words)

    NN_fd = nltk.FreqDist(NNtags)
    #print("Most frequent NN =", NN_fd.most_common(1))

    commonNN = NN_fd.most_common(1)[0][0][0]
    #print("Words similar to", commonNN, ":")
    #text.similar(commonNN)
    #print()

    VBD_fd = nltk.FreqDist(VBDtags)
    #print("Most frequent VBD =", VBD_fd.most_common(1))

    commonVBD = VBD_fd.most_common(1)[0][0][0]
    #print("Words similar to", commonVBD, ":")
    #text.similar(commonVBD)
    #print()

    JJ_fd = nltk.FreqDist(JJtags)
    #print("Most frequent JJ =", JJ_fd.most_common(1))

    commonJJ = JJ_fd.most_common(1)[0][0][0]
    #print("Words similar to", commonJJ, ":")
    #text.similar(commonJJ)
    #print()

    RB_fd = nltk.FreqDist(RBtags)
    #print("Most frequent RB =", RB_fd.most_common(1))

    commonRB = RB_fd.most_common(1)[0][0][0]
    #print("Words similar to", commonRB, ":")
    #text.similar(commonRB)
    #print()

    # 5. Collocations
    co_text = nltk.Text(flat_words)
    #print("6. Collocations: ", end="")
    #co_text.collocations()


###############################################################################
## Program Entry Point ########################################################
###############################################################################
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Style')
    parser.add_argument('--corpus', required=True, dest="corpus", metavar='NAME',
                        help='Which corpus to process')

    args = parser.parse_args()

    corpus_name = args.corpus

    if corpus_name == "samples" or "samplesv2":
        process_corpus(corpus_name)
    else:
        print("Unknown corpus name: {0}".format(corpus_name))
