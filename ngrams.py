#!/usr/bin/python
# Encoding: utf8

# INPUT: tokenized text (tokens separted by whitespaces)
# ARGUMENT: number of grams
# OUTPUT: each line is a n-gram

import sys

size = sys.argv[1]
size = int(size)

file1 = open("tokens.txt",'r')
file2 = open("trigrams.txt",'w')
def ngrams(input, n):
    input = input.split(' ')
    output = []
    for i in range(len(input)-n+1):
        output.append(input[i:i+n])
    return output

output=""
for line in file1:  
    line = line.strip()

    if len(line)>1:
        result = ngrams(line,size) 
        for ngram in result:
            juntar = ""
           
            for token in ngram:
                juntar += token + " "
            print(juntar)
            #print (juntar, sys.stderr)
            output += juntar + "\n"

file2.write(output)

