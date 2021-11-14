
### Chatter Chatterboty, What will you say?
This program will be given names of text files of any type (for example, books)
as well a a choice of whether or not they want to use unigram, bigram, or a trigram 
model to generate random sentences from. Using the textfiles, the program will recognize
patterns of proceeding words to examine. From there, it will generate a number of sentences
(Given from the command line) from the patterns. Unigrams will generate random words (weighted)
from the list of words given in the corpus. Bigrams will use unigram to generate the first word 
and then generate words from the data BASED on the previous word (weighted). Trigrams will use 
unigrams and bigrams to generate the first two words of a sentence, and then generate words based 
on the previous TWO words of the sentence (weighted). Each sentence will be considered finished 
if the next token generated is a period, question mark, or exclamation point.



## Program use Exampple 
$ python3 Chatterbot.py 2 10 pg30000.txt pg26000.txt pg3000.txt pg23000.txt pg40000.txt pg54000.txt pg39000.txt pg100000.txt
This program generates 10 random sentences based on a 2-gram model. Project By Eli Sailer-Haubgland.
1- say is sad tears for not merely saves thy desire of the gospels. 
2- to the foremost of reason for as emperor! 
3- i have never bold to repeat the import. 
4- hélène’s salon was a day when alone and ends to get out a week; and trademark, that terror to him, in a soul knew how to the best, entered the nearness, with the people’s will be drown’d, seemed funny you think he; that no word that live near the french cavalry came the least abashed by ice are your sister of the buffaloes will of person), and fetch ourselves with a plan, madame. 
5- superior being tortured by the round, konovnítsyn rushed to be filled napoleon noticed it a man with but, talks with myself, and you are actions had formerly tormented; and ridicule what deed done sónya had exchanged glances expressed the bridge, at all the clavichord stood at segowlee cantonment. 
6- the facts, and by hector and the next morning the devil! 
7- smoking out other side. 
8- curiosity bore against superior society of russia without knowing them. 
9- threw it was long before. 
10- his royal mother, presuming neither directs all, that his own, ” and made his bony hands. 

## How it works
The program will transform ALL text fromm a single string to an array (for multiple files, it will transform all text to arrays, then concatenate all arrays into 1 array). Unigram models will randomly select a word at random from a weighted corpus (weighted meaning that the array contains duplicates such that the percentage of one word in the text is the percentage of that one word in the array) until it reaches a . ? or !. A brigram dictionary will be used such that the key is the ith position of the unigrmam array and the value is an weighted array of words such that the ith key inputs the i+1 th value. If the bigram model already contains the ith word in the bigram model, we will append the array stored in the value. Then, we will generate a word based on the previous word. Since the vaue is a weighted array, the next word will randomly generate the word in the given value array. The same thing applies to Trigrams, but we use tuples for the third word given the first two words.

