#for STD output
import sys
#For regular Expressions
import re
#To generate random data from a list
import random
#To concatenate two arrays
import numpy

#ChatterBot: N-Gram Generator
#By Eli Sailer-Haugland



# Get the command line arguments. Each argument in this array 
# is read such that it looks like this: python(v) argv].
args = sys.argv
#Remove the file that is being called as that argument is irrelavent to calling the program
args.remove("Chatterbot.py")
# argv is structred like this (with the remove function implemented)
# [model type, how many times the program shoud run, The files names that want to be ran in the program (many args)]
# num is the model (1 = unigram, 2 = bigram, 3= trigram) that the user wants to run
num = int(args[0])
# times is the number of times the program will generate a sentence
times = int(args[1])
# the names of the files that will be executed (given that it is in the same directory as this py file)
files = args[2:]
#an empty array that will be used to fill single words
unigram = []
#Every puncuation that will be sepearted by a space in order for puncuations to be considered individual tokens
symbol = r'([\,\.\!\?\;\'\:\"\[\]\(\)])'
#For each file in the command line (files that are certain to work are .txt files)
for name in files:
    f = open(name)
    #read the file and delete all new line occurances
    t = f.read().replace('\n', ' ')
    #make the string ALL lowercase letters
    t = t.lower()
    #For all puncuation, eperate them with two spaces, one on each side of the puncuation
    t = re.sub(symbol, r' \1 ', t)
    #For all times there may be two or more spaces in a row, single that down to one space between all tokens
    t = re.sub(r'( )+', ' ', t)
    #Make an arreay with all the words and puncuation in the text and concatenate that onto the unigrma array
    #This array splits the string into tokens where they key character to split is an array
    #NOTE: the order of the words remains the same when a.split is called in the array as they did in the string!
    unigram = numpy.concatenate((unigram,t.split(" ")))
f.close()
#Start of the program
#a is the final string that will be outputed by stdout
a = "This program generates " + str(times) + " random sentences based on a " + str(num) + "-gram model. Project By Eli Sailer-Haubgland.\n"
#If the user wants to use a unigram model
if num == 1:
    #For the number of times you want the program to run
    for i in range(1, times+1):
        #create a tmp string 
        tmp = str(i) + "- "
        #create the p variable
        p = "x"
        #Keep adding random words from unigram until the random unigream value is a end-character
        while p not in ".!?":
            p = random.choice(unigram)
            tmp+= (p + " ")
        #add the tmp string to a
        a += tmp + "\n"
#For all time the usere wants to implement bigram or trigram
if num > 1:
    #create a bigram dictionary
    #This dictionary will be structured as {Key: string, Value: [String] }
    bigram = {}
    #For every string in unigram EXCEPT the last Unigram
    for i in range(0,len(unigram)-1):
        #If the string is not a key in bigram, add {unigram[i], [unigram[i+1]]}
        #Where [unigram[i+1]] is an array
        if unigram[i] not in bigram:
            bigram[unigram[i]] = [unigram[i+1]]
        else:
            #If that string is in bigram, append unigram[i+1] to the value array
            bigram[unigram[i]].append(unigram[i+1])
    #If the user wants to implement bigram
    if num == 2:
        for i in range(1, times+1):
            #creates tmp string
            tmp = str(i) + "- "
            #choose a word from the corpus
            p = random.choice(unigram)
            #choose the first word in a sentence that is NOT an end statement
            while p in ".!?":
                p = random.choice(unigram)
            #add word to tmp
            tmp += p + " "
            #while string is not an end statement, get the value array of the bigram
            #word that was previously chosen. From the value array, pick a random
            #string from the array of strings (The value array is weighted).
            #Continue this process until the string chosen is a . ! or ?
            while p not in ".!?":
                p = random.choice(bigram[p])
                tmp+= (p + " ")
            #ADD TMP and a new line to string
            a += tmp + "\n"
#if the user wants to use a trigram model
if num == 3:
    #Create a trigram dictionary
    #The dictionary is set up like this {Key (tuple that contains the first two words), [String]}
    trigram = {}
    #For every value in the corpus EXCEPT the last two words
    for i in range(0,len(unigram)-2):
        #If the key (unigram[i], ungram[i+1]) is not in trigram, add it to trigram with
        #A value array of [unigram[i+2]]
        if (unigram[i], unigram[i+1]) not in trigram:
            trigram[(unigram[i],unigram[i+1])] = [unigram[i+2]]
        else:
            #if the trigram contains (unigram[i], unigram[i+1]), append
            #unigram[i+2] to the value array
            trigram[(unigram[i], unigram[i+1])].append(unigram[i+2])
    for i in range(1,times + 1):
        #create the temp strinmg
        tmp = str(i) + "- "
        #choose a random word from the corpus
        p = random.choice(unigram)
        #choose a string UNTIL the string is not an end statement
        while p in ".!?":
            p = random.choice(unigram)
        #add string to tmp
        tmp += p + " "
        #create a tuple that holds the first word chosen
        mem = (p,)
        #use the bigram to choose the second word in the sentence
        p = random.choice(bigram[mem[0]])
        #choose a string for the second word until the second word is not . ! or ?
        while p in ".!?":
            p = random.choice(bigram[mem[0]])
        #add the string to tmp
        tmp += p + " "
        #add the second word to the mem tuple such that memm = (word_1, word_2)
        mem += (p,)
        #while the character is not an . ? !, search for the value array given
        #the tuple. The trigram[tuple] will return a value array (weighted)
        #where we can random select a word from that value array
        while p not in ".!?":
            p = random.choice(trigram[mem])
            #reassign the merm tuple to (the second index of mem, the newly chose word)
            mem = (mem[1], p)
            tmp += p + " "
        #add tmp and a new line to a
        a+=tmp + "\n"
#For all puncuation with a space in front of it, remove THAT space
a = re.sub(r' ' + symbol, r'\1', a)
#print a using stdout
sys.stdout.write(a)
