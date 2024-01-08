# Code for a program to converts a sentence from english to pig latin and pig latin to english
# Author: Dylan Friedman
# FRDDYL002
# 18th April 2022

vowel = ['a', 'i', 'o', 'u', 'e']

def to_pig_latin(s):
    # Converting a sentence from english to pig latin    
    sarr = s.split(' ')
    for n in range(len(sarr)):
        sword = sarr[n]
        if any(char in vowel for char in sword):
            if sword[0] in vowel:
                sword = sword+'way'
            else:
                for i in sword:
                    if i in vowel:
                        x = word.find(i)
                        break
                seqcons = sword[:x]
                sword = sword[x:]+'a'+seqcons+'ay'
        else:
            sword = 'a'+sword+'ay'
        sarr[n]=sword
    s = ' '.join(sarr)
    return s

def to_english(s):
    # Converting a sentence from pig latin to english
    sarr = s.split(' ')
    for n in range(len(sarr)):
        sword = sarr[n]
        if sword[-1:-4:-1] == 'yaw':
            sword = sword[-4::-1]
            sword = sword[-1::-1]
        else:
            sword = sword[-1::-1]
            sword = sword[2:]
            seqcons = sword[:sword.find('a')]
            seqcons = seqcons[-1::-1]
            sword = sword[sword.find('a')+1:]
            sword = sword[-1::-1]
            sword = seqcons + sword
        sarr[n]=sword
    s = ' '.join(sarr)
    return s
