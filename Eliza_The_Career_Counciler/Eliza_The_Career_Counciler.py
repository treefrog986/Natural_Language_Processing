
#re is the standard library for regular expressions
import re
#random is used to randommly pick something from an arrray of items
import random

# Natural Language Processing
# Eli Sailer-Haugland
# Lab 1: Eliza, the career councilir

# 1. This is a career councilur application. This program will
# get user input, and respond in a variety of ways. It can check
# for keywords in the memory, it can spot specific lanuage, and it
# can spot key phrases of which it will both RESPOND and store certains
# data points in memory. Some triggers will then use the memory to either
# respond to the user in anotehr statement or to spur the conversation elsewhere

# 2. Using the program is simple. The user will input a sentence (that includes
# puncuation) and the program will output a response based on the mass vairety
# of phrasing provided in the programa. If the user inputs specific language like
# gibberish, rude or abusive language, or certain keywords related to what a career
# counciler might respond to, the program will respond accordingly. Here is a snipit
# of what this program may do

# [Eliza] What is your major?
# [User]I am majoring in Computer Science.
# [Eliza] Wow! Computer Science is an interest major! Do you like Computer Science?

# 3. The algorithm will be explained in broader detail within the program, but here
# is the basic algorim. The program will first prompt you with a name, you will then
# respond with a certain phrase like "My name is Eli.", fromm there, a convesation will
# occur. Here's the general format of the algorithm. If, sometime in the program, a nmae
# was stored in memory, the program will throw the name into a variable, and that variable
# name will shown up throughout the program as a prompt to respond to Eliza. if there are
# keywords or phrases spotting in the user's respondse, Eliza will respond to the messaage
# accordingly, regardless of the rest of the statement. If there is a specifc way a user
# responds to Eliza such that it matches the phrasing of a suggested input, it will output a
# specific type of language, use memmory (if necessary) and add to memory for later use (if
# necessary). If it detects no specific phrases or keywords, Eliza will output a question
# (from a set of questions) to spur the conversation! Refer yourself to comments withnin the
# program for more specific details.

# Memory is a python dictionary. When a user trigger specific phrasings, memory will be called
# to either gather data or retrieve data for use in Eliza's response. The keys of each memory pair
# is already preprogrammed into the phrasew section
memory = {}

#Pronouns and Pronoun_mapping are both used for pronoun flipping
pronouns= re.compile(r'\bI|[Ww]e|[Yy]ou|my|our|your|[Mm]e\b')
pronoun_mapping = {
    'I': 'you',
    'we': 'You',
    'you':'I',
    'my':'your',
    'our':'your',
    'your ':'my',
    'me':'you'
}
#If there are specific keywords or patters in the user's input (the key),
# the program with automatically output a phrase (the phrase) purely based on
# that keyword OR phrase pattern. Some patterns are specified below as they deal with
# specific patterns.
spotting = {
    # The following ptterns detects gibberish in a number of ways.
    # If the input consists of 3 consecutive vowels, 3 consecutive consonants, or
    # words longer thans 12 letter, it will detect the input as gibberish
    r'.*([aeiouyAEIOUY]{4}|[a-zA-Z]{12}|[bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWWXZ]{4}).*':'I\'m sorry, I did not understand you',
    # The following patter detechs abusive language. if, in any capacity,
    # abusive language is deteched, it will output a warning not to use 
    # that type of language
    r'.*(fuck(ing|)|stupid|sucks|iduit|bitch|annoy(ed|ing)).*':'Please don\'t use abusive language!',
    r'.*([Jj]ob).*':'What jobs are you looking for?',
    r'.*([Ss]alary).*':'How might a job\'s salary impact which job you choose?',
    r'.*([Rr]etirement).*': 'Do you think it\'s important for you to think about retirement now?',
    r'.*([Bb]enefits).*': 'How would a company\'s benefits impaact what jobs you choose to apply for?',
    r'.*([Rr]esumes?).*': 'Why do you ask about resumes?',
    r'.*([Tt]ravel).*': 'How might a job\'s requirement to travel affect where you work?',
    r'.*([Ff]amily).*': 'How might your family be important for your job searching?',
    r'.*(yay|yes|awesome|excit(ing|ed)).*': 'I am gkad that you are excited! Lookig for a job can be fun!',
    r'.*([Ii]nterviews?).*': 'What skills might be the most important when interviewing for a job?'
}
# This array of arrays consists of questions to spur the conversation. For each array x in the array spurring,
# x[0] is the phrase of which Eliza will spur out, x[1] is the required names of memory that must exist in 
# memory in order for that array to be used. 
# note: /x/ means use the xth element (which reference the memory) in the array stored in x[1]
spurring = [
    ['Where are you from?',[]],
    ['You said earlier that you live in /0/. How might that affect where you want to work?',['hometown']],
    ['What are some /0/ courses that you have taken that could be beneficial on your resume?',['major']],
    ['How might learning about /0/ be beneficial in finding a job?',['courses']],
    ['Why is it so important for you to look for a job now?',[]],
    ['What is your dream job?',[]],
    ['Where do you find yourself living in the future?',[]],
    ['What kind of jobs might be in /0/?',['desiredLocal']]
]
#These are the possible phrasing for the program
#This is a colelction of arrays that work together, for each array x in the array phrses
#x[0] is the input templates. These phrases are used to capute data from the user and/or output the appropiate response
# x[1] is the response to the phraae Eliza will output from the program.
# Please note, \x is different than /x/ as \x directly reference the group number of the regex phrase in x[0]
# x[2] indicates whether or not daata will be stored in memory, and what the name of the piece of memory should be
# (There are special cases such as 'p', but if '' is ix x[2], no memmory will be stored)
# x[3] references what should be placed in memory[x[2]]. r'\x' returns a string memory to story in memory, r'' means that Eliza will not be importing into mmemory
# x[4] describes what keys/values of memory it will use and impleemnt them in x[1] (Eliza's response)
phrases = [
    [r'(I live in |My hometown is |I am from )(.*).',r'How might living in \2 affect your career?','hometown',r'\2',[]],
    [r'((Hi, |Hello, )?[Mm]y name is) (.*).',r'Hello There /0/ \n[Eliza] What is your major?','name', r'\3',['name']],
    [r'(((I am|I\'m) majoring in)|My major is) (.*).', r'Wow! /0/ is an interest major! Do you like /0/?', 'major', r'\4',['major']],
    [r'.*I (am|feel) (stressed|concerned|worried)(.*).', r'Do not worry /0/, Feeling \2 about getting a job is normal, but I am here to help you!','',r'',['name']],
    [r'.*(I (don\'t|do not) know).*', r'/0/, not knowing is okay, but I suggest you think about what /1/ jobs you feel like you could apply for!','',r'',['name','major']],
    [r'What (is|are) (.*)\?', r'What do you think \2 \1?','',r'',[]],
    [r'(can|may) (I|you) (.*) (you|me)(.*)\?', r'How \1 \2 \3 \4\5?', 'p', r'',[]],
    [r'(Some Places )?I want to (live in|travel to|work in) (include |are )?(.*).', r'/0/ is an excellent place to work, /1/! Do you plan on movning after graduating?','desiredLocal', r'\4',['desiredLocal','name']],
    [r'(Some courses )?(I(\'ve| have) taken (courses like|include|are|)) ([a-zA-Z\,\s]*).','Are those courses hard at all?', 'courses',r'\5',[]],
    [r'(They|[Cc]lasses) (can be|are) (hard|difficult).', "While classes can be dificult, they can also be very impressive to employers!",'',r'',[]],
    [r'What are (.*)\?', r'What do you think \1 are?','p',r'',[]],
]

#Note: re.sub(a,b,c) means if the string a is a substring or matching pattern within c, 
#replace instaances of string a with b within c.

def switch(a, arr):
    #For every value in arr (which is x[4]) (ranging from x=0 to len(arr)), replace /x/ with the the string
    #in memory that is also in x[4] of the phrases array
    for i in range(len(arr)):
        #obtain the ith element in the x[4] (phrases) array and find the value in the memory dictionary
        temp = memory[arr[i]]
        #If memmory[arr[i]] is a list/array of strings, randomly choose one of the string within thaat array
        if isinstance(temp, list):
            temp = random.choice(temp)
        a = re.sub('/'+ str(i)+'/',temp, a)
    return a

#This function will be described in sections
# re.match(a,b) - if a is a substring or matching pattern within b, return true, else false
# re.IGNORECASE is optional and simply mean it will be non-case sensitive
# x is the input string
def phrase(x):
    #If memory has the name attribute, the variable name will have vaalue memory['name], else it will have 'User'
    if 'name' in memory:
        name = memory['name']
    else:
        name = 'User'
    #check to see if any of the values of spotting is within x
    for k,v in spotting.items():
        if re.match(k,x, re.IGNORECASE):
            return '[Eliza] '+v+ '\n['+name+'] '
    #check to see if any of the phrases is a substring or matches phrasing within x
    for i in phrases:
        if re.match(i[0], x, re.IGNORECASE):
            # if there exists somme property that requires changing the pronouns or inporting memory
            if i[2] != '':
                # if you need to import memory
                if i[2] != 'p':
                    # get the string value of the xth group of the regex string within x given the pattern i[0]
                    memory[i[2]] = re.sub(i[0], i[3],x)
                    #If memory[i[2]] contains a list of values like "a, b, c, and d."
                    if ',' in memory[i[2]]:
                        #this modifies memory of string x = "a, b, c , and d" to [a,b,c,d]
                        memory[i[2]] = memory[i[2]].split(', ')
                        memory[i[2]][len(memory[i[2]])-1]= memory[i[2]][len(memory[i[2]])-1].replace('and ','')
                else:
                    #for i[2] values 'p', this indicates that pronoun switching occurs
                    x = pronoun(x)
            #if i[4] is not empty, that is, if memory needs to be used for the output
            if i[4]:
                x = re.sub(i[0],i[1],x)
                return'[Eliza] '+ switch(x, i[4])+ '\n['+name+'] '

            return '[Eliza] '+ re.sub(i[0],i[1],x) + '\n['+name+'] '
    #if no such pattern or method of spotting occurs, spur the conversation
    return '[Eliza] ' + spur() + '\n['+name+'] '

#This flips the pronouns of the string, for example "I want your dog" switches to "You want my dog"
def pronoun(x):
    x = x.lower()
    return re.sub(pronouns, lambda s: pronoun_mapping[s.group()],x)

def spur():
    a = random.choice(spurring)
    #While all requirements in spurring variable x[1] are not in memory, choose another random spurring topic.
    while not all(x in memory for x in a[1]):
        a = random.choice(spurring)
    #remove that spurring element from the list of spirts
    spurring.remove(a)
    #return the string involving all of the required pieces of memory
    return switch(a[0],a[1])

#starting input screen
cur = input('[Eliza] Hello, my name is Eliza, and I was created by Eli Sailer-Haugland. What is your name?\n[user] ')
#while input is not exit, continue getting input.
while cur!= 'exit':
    cur = input(phrase(cur))

