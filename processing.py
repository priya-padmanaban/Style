#!/usr/bin/env python

import nltk, zipfile, argparse
import sys

###############################################################################
## Utility Functions ##########################################################
###############################################################################
# This method takes the path to a zip archive and reads the raw contents of the
# file.

def unzip_corpus(input_file):
    zip_archive = zipfile.ZipFile(input_file)
    contents = [zip_archive.open(fn, 'rU').read().decode('utf-8') for fn in zip_archive.namelist() if fn.endswith(".txt")]
    return contents

###############################################################################
## Stub Functions #############################################################
###############################################################################
def process_corpus(corpus_name):
    input_file = corpus_name + ".zip"
    corpus_contents = unzip_corpus(input_file)
    
    # 1. Toeknization
    
    # (a) Write the name of the corpus to stdout
    print("1. Corpus Name:", corpus_name)
    
    # (b) Delimit the sentences for each document in the corpus.
    
    totalWords = []
    totalTags = []
    
    # POS Tag Output File
    pos_file = open(corpus_name + "-pos.txt", 'w')

    for doc in corpus_contents:
        sentences = nltk.sent_tokenize(doc)
        
        for sentence in sentences:
            # (c) Tokenize the words in each sentences of each document
            words = nltk.word_tokenize(sentence)
            for word in words:
                totalWords.append(word)
            
            # 2. Part-of-Speech
            # (a) Apply the default part-of-speech tagger to each tokenized sentence
            tagged = nltk.pos_tag(words)
            for tag in tagged:
                totalTags.append(tag)
                string = nltk.tuple2str(tag)
                print(string, file=pos_file, end = " ")
            print("\n", file=pos_file, end = "")
        print("\n", file=pos_file, end = "")
    
    # Close the POS tag file
    pos_file.close()
    
    # (d) Count the number of total words in the corpus and write the result to stdout
    wordCount = 0;
    wordCount = len(totalWords)
    print("2. Total Words in the Corpus:", wordCount)

    # 3. Frequency

    # (a) Write the vocabulary size of corpus to stdout
    flat_words = [word.lower() for word in totalWords]
    vocabCount = 0;
    vocabCount = len(set(flat_words))
    print("3. Vocabulary Size of the Corpus:", vocabCount)
    
    # (b) Write the most frequent part-of-speech tag and it's frequency to stdout
    
    tagged_fd = nltk.FreqDist(tag for (word, tag) in totalTags)
    print("4. The most frequent part-of-speech tag is", tagged_fd.most_common(1))
    
    # (c) Frequency of each unique word (lower case)
    
    # Frequency Output File
    freq_file = open(corpus_name + "-word-freq.txt", 'w')
    
    fdist = nltk.FreqDist(flat_words)
    print([pair[0] for pair in sorted(fdist.items(), key=lambda item: item[1], reverse=True)], file=freq_file)
    
    freq_file.close()
    
    # (d) Conditional Frequency Distribution
    
    sys.stdout = open(corpus_name+"-pos-word-freq.txt",'w')
    
    # Reverse 
    pos_reversed = [(b, a.lower()) for a,b in totalTags]
    
    cdf1 = nltk.ConditionalFreqDist(pos_reversed)
    
    cdf1.tabulate()
    
    sys.stdout = sys.__stdout__

    
    # 4. Similar Words
    # (a) Write most similar words to stdout
    NNtags = []
    VBDtags = []
    JJtags = []
    RBtags = []
    for x in totalTags:
        if x[1] == 'NN':
            NNtags.append(x)
        elif x[1] == 'VBD':
            VBDtags.append(x)
        elif x[1] == 'JJ':
            JJtags.append(x)
        elif x[1] == 'RB':
            RBtags.append(x)
            
    print("5. The most frequent word in the POS (NN/VBD/JJ/RB) and respective similar words:")
            
    text = nltk.Text(flat_words)
            
    NN_fd = nltk.FreqDist(NNtags)
    print("Most frequent NN =", NN_fd.most_common(1))
    
    commonNN = NN_fd.most_common(1)[0][0][0]
    print("Words similar to", commonNN, ":")
    text.similar(commonNN)
    print()
    
    VBD_fd = nltk.FreqDist(VBDtags)
    print("Most frequent VBD =", VBD_fd.most_common(1))
    
    commonVBD = VBD_fd.most_common(1)[0][0][0]
    print("Words similar to", commonVBD, ":")
    text.similar(commonVBD)
    print()
    
    JJ_fd = nltk.FreqDist(JJtags)
    print("Most frequent JJ =", JJ_fd.most_common(1))
    
    commonJJ = JJ_fd.most_common(1)[0][0][0]
    print("Words similar to", commonJJ, ":")
    text.similar(commonJJ)
    print()
    
    RB_fd = nltk.FreqDist(RBtags)
    print("Most frequent RB =", RB_fd.most_common(1))
    
    commonRB = RB_fd.most_common(1)[0][0][0]
    print("Words similar to", commonRB, ":")
    text.similar(commonRB)
    print()
    
    # 5. Collocations
    # Piazza: "You should create a nltk.Text object with the lowercase
    #   words of the whole corpus, then call the collocations() method."
    co_text = nltk.Text(flat_words)
    print("6. Collocatoins: ", end="")
    co_text.collocations()
    


###############################################################################
## Program Entry Point ########################################################
###############################################################################
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Assignment 1')
    parser.add_argument('--corpus', required=True, dest="corpus", metavar='NAME',  help='Which corpus to process {fables, blogs}')

    args = parser.parse_args()
    
    corpus_name = args.corpus
    
    if corpus_name == "fables" or "blogs":
        process_corpus(corpus_name)
    else:
        print("Unknown corpus name: {0}".format(corpus_name))
        