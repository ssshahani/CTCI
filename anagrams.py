# -*- coding: utf-8 -*-
"""
Created on Sun Jul  8 20:15:38 2018

@author: Sahil S
"""


def GroupAnagrams():
    strings = initialise_anagrams()
    anagrams = {}
    for i in range(len(strings)):
        word = "".join(sorted(strings[i].lower()))
        if word not in anagrams.keys():
            anagrams[word] = []
        anagrams[word].append(strings[i])

    keys = anagrams.keys()
    index = 0
    for key in keys:
        values = anagrams.get(key)
        for j in range(len(values)):
            strings[index] = values[j];
            index += 1
    print(strings)


def initialise_anagrams():
    strings = [0] * 8
    strings[0] = "abed"
    strings[1] = "later"
    strings[2] = "bead"
    strings[3] = "alert"
    strings[4] = "altered"
    strings[5] = "bade"
    strings[6] = "alter"
    strings[7] = "alerted"
    return strings

GroupAnagrams()