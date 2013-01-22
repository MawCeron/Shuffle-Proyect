#!/usr/bin/env python
# -*- coding: utf-8 -*-

def shuffle(source, partial, out):
    newPartial = partial
    newSource = ""
    if len(source) == 0:
        out.append(newPartial)
        return
    for i in range(len(source)):
        newPartial = partial + source[i:i +1]
        newSource = source[0:i]
        if i < (len(source)+1):
            newSource = newSource + source[i+1:len(source)]
        shuffle(newSource,newPartial, out)
        
def generate(source):
    out = []
    partial = ""
    shuffle(source, partial, out)
    return out

word = raw_input("Letras a permutar: ")
mix = generate(word)

words = []
for i in range(len(mix)):
    if mix[i] not in words:
        words.append(mix[i])

for i in range(len(words)):
    print words[i]
