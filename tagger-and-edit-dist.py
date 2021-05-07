# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import nltk
import numpy as np
import sys
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.cluster import AgglomerativeClustering
from matplotlib import pyplot as plt

test = ["this is a test", "this a test", "is a test", "this is test"]

coord = [['CC'], 'c']
card = [['CD'], 'r']
det_exis = [['DT', 'EX', 'WDT'], 'd']
foreign = [['FW'], 'f']
prep = [['IN'], 'i']
adjs = [['JJ', 'JJR', 'JJS'], 'a']
modal = [['MD'], 'm']
nouns = [['NN', 'NNS', 'NNP', 'NNPS'], 'n']
pdt = [['PDT'], 't']
pos = [['POS'], 's']
pronn = [['PRP', 'PRP$', 'WP', 'WP$'], 'p']
advbs = [['RB', 'RBS', 'RBR', 'WRB'], 'x']
vrb = [['VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ'], 'v']

pos_tag_translator = [coord, card, det_exis, foreign, prep, adjs, modal, nouns, pdt, pos, pronn, advbs, vrb]

customSubList = {
        ('a', 'x'): 1
        }


def editDistance(str1, str2, deleteCost = 1, defaultSubCost = 2, subList = {}):
     #initialize both strings to lowercase
     string1 = str1.lower()
     string2 = str2.lower()
    
     #calculate dimensions for matrix which is used for dynamic calculations
     len1 = len(string1)+1
     len2 = len(string2)+1
    
     distArray = np.zeros((len1, len2))
    
     #initialize first row / column in matrix to 0's, and second row / column
     #to insert / delete cost
     for j in range(1, len1):
         distArray[j, 0] = distArray[j-1, 0] + deleteCost
    
     for j in range(1, len2):
         distArray[0, j] = distArray[0, j-1] + deleteCost
    
     #The substitution cost will change at every iteration due to it being
     #dependent on the current characters, initialize here to be in scope for
     #following calculations
     substitutionCost = 0
    
     #Loop through entire matrix and fill with editing distances
     for j in range(1, len1):
         for k in range(1, len2):
            #change substitution cost depending on the current characters
            #found in the strings being compared
            if string1[j-1] == string2[k-1]:
                 substitutionCost = 0
            #calculate specialized subCost here?
            else:
                substitutionCost = defaultSubCost
                
             #calculate the distance between the strings based
            distArray[j, k] = min(distArray[j-1, k] + deleteCost,
                     distArray[j, k-1] + deleteCost,
                     distArray[j-1, k-1] + substitutionCost)
    
     return distArray[len1-1, len2-1]

def convertSentence(sentence):
    output = ''
    tokens = nltk.word_tokenize(sentence)
    posTags = nltk.pos_tag(tokens)
    
    #iterate over words in the sentence
    for word in posTags:
        #iterate through possible pos_tags
        for tag in pos_tag_translator:
            if(word[1] in tag[0]):
                #print(word[1], tag[0], tag[1])
                output += tag[1]
    return output

def createCorpus(corpus):
    convertedCorpus = []
    for sent in corpus:
        convertedCorpus.append(convertSentence(sent))
    
    convertedCorpus = np.asarray(convertedCorpus, dtype=object)
    return convertedCorpus

def createDistMatrixOfCorpus(corpus):
    size = len(corpus)
    mat = np.zeros(shape=(size, size), dtype=float)
    
    convertedCorpus = createCorpus(corpus)
    
    #iterate through created Matrix 'mat' and fill distances
    for j in range(size):
        for k in range(size):
            if(j == k):
                continue
            mat[j, k] = editDistance(convertedCorpus[j], convertedCorpus[k])
    
    return mat        

def getEdit(p1, p2):
    return editDistance(p1, p2)

def clustering(corpus):
    conv = createCorpus(corpus)
    cluster = linkage(conv, metric=getEdit)



if __name__ == "__main__":
    pklFileName = sys.argv[1]
    #tokens = nltk.word_tokenize(test)
    #posTags = nltk.pos_tag(tokens)
    
    #print(posTags)
    #cum = convertSentence(test)
    #convent = createCorpus(test)
    ret = createDistMatrixOfCorpus(test)
    #cluster = clustering(test)
    conv = createCorpus(test)
    cluster = linkage(ret)
    labelList = range(1, len(test)+1)
    plt.figure(figsize=(10,7))
    dendrogram(cluster,
               orientation='top',
               labels=labelList,
               distance_sort='descending',
               show_leaf_counts=True)
    plt.show()
