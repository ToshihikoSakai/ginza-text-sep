# -*- coding: utf-8 -*-
import pandas as pd
import spacy

nlp = spacy.load('ja_ginza')

with open("test.txt", mode='r') as f:
    text = f.read()
f.close()

doc = nlp(text)

for line in doc.sents:
    print(line.text)
