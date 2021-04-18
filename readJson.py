# -*- coding: utf-8 -*-
"""
Created on Sun Apr 18 14:49:21 2021

@author: Nathan
"""
import json

with open("test-json.json") as f:
    data = json.load(f)

for x in data:
    print(x)
    
print("\n\nMetadata sections:")
for x in data['metadata']:
    print(x)

print("\n\nTitle:")
print(data['metadata']['title'])
    
print('\n\nAuthors: ')    
for authors in data['metadata']['authors']:
    #print(authors['middle'])
    authorName = authors['first'] + ' '
    if len(authors['middle'])>0:
        authorName += authors['middle'][0] + ". "
    authorName += authors['last']
    
    
    affiliation = authors['affiliation']
    email = authors['email']
    
    print("Author name: ", authorName)
    print("Author affiliation ", affiliation)
    print("Author email: ", email)
    
print('\n\nAbstract:')
print(data['abstract'])

print('\n\nBody Text:')
for x in data['body_text']:
    text = x['text']
    section = x['section'].upper()
    print(section)
    print(text, '\n')