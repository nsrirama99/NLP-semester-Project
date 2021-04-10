# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 17:39:15 2021

@author: Nathan Srirama
"""

from openie import StanfordOpenIE

#with StanfordOpenIE() as client:
client = StanfordOpenIE()

text = 'Barack Obama was born in Hawaii. Richard Manning wrote this sentence'
print('Text: %s.' % text)
    
for triple in client.annotate(text):
    print('|-', triple)
    
#graph_image = 'graph.png'
#client.generate_graphviz_graph(text, graph_image)
#print('Graph generated: %s' % graph_image)
   
with open('test.txt', 'r') as r:
    corpus = r.read().replace('\n', ' ').replace('\r', '')
        
triple_corpus = client.annotate(corpus)
print('Corpus: %s [...].' % corpus)
print('Found %s triples in the corpus.' % len(triple_corpus))
for triple in triple_corpus:
    print('|-', triple)