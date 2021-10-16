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

# 1) This program will be given names of text files of any type (for example, books)
# as well a a choice of whether or not they want to use unigram, bigram, or a trigram 
# model to generate random sentences from. Using the textfiles, the program will recognize
# patterns of proceeding words to examine. From there, it will generate a number of sentences
# (Given from the command line) from the patterns. Unigrams will generate random words (weighted)
# from the list of words given in the corpus. Bigrams will use unigram to generate the first word 
# and then generate words from the data BASED on the previous word (weighted). Trigrams will use 
# unigrams and bigrams to generate the first two words of a sentence, and then generate words based 
# on the previous TWO words of the sentence (weighted). Each sentence will be considered finished 
# if the next token generated is a period, question mark, or exclamation point.



# 2) An example 
# $ python3 Chatterbot.py 2 10 pg30000.txt pg26000.txt pg3000.txt pg23000.txt pg40000.txt pg54000.txt pg39000.txt pg100000.txt
# This program generates 10 random sentences based on a 2-gram model. Project By Eli Sailer-Haubgland.
# 1- say is sad tears for not merely saves thy desire of the gospels. 
# 2- to the foremost of reason for as emperor! 
# 3- i have never bold to repeat the import. 
# 4- hélène’s salon was a day when alone and ends to get out a week; and trademark, that terror to him, in a soul knew how to the best, entered the nearness, with the people’s will be drown’d, seemed funny you think he; that no word that live near the french cavalry came the least abashed by ice are your sister of the buffaloes will of person), and fetch ourselves with a plan, madame. 
# 5- superior being tortured by the round, konovnítsyn rushed to be filled napoleon noticed it a man with but, talks with myself, and you are actions had formerly tormented; and ridicule what deed done sónya had exchanged glances expressed the bridge, at all the clavichord stood at segowlee cantonment. 
# 6- the facts, and by hector and the next morning the devil! 
# 7- smoking out other side. 
# 8- curiosity bore against superior society of russia without knowing them. 
# 9- threw it was long before. 
# 10- his royal mother, presuming neither directs all, that his own, ” and made his bony hands. 
# 3) The program will transform ALL text fromm a single string to an array (for multiple files,
# it will transform all text to arrays, then concatenate all arrays into 1 array). Unigram models 
# will randomly select a word at random from a weighted corpus (weighted meaning that the array contains
# duplicates such that the percentage of one word in the text is the percentage of that one word in the array)
# untill it reaches a . ? or !. A brigram dictionary will be used such that the key is the ith position of the 
# ungrma array and the value is an weighted array of words such that the ith key inputs the i+1 th value. If
# the bigram model already contains the ith word in the bigram model, we will append the array stored in the value.
# Then, we will generate a word based on the previous word. Since the vaue is a weighted array, the next word 
# will randomly generate the word in the given value array. The same thing applies to Trigrams, but we use 
# tuples for the third word given the first two words.



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
