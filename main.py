from nltk.book import *
import nltk

#print (text1)
#print (len(text3))
#print (set(text3))
#print (sorted(set(text3)))


#print (text4[173])

fdist1 = FreqDist(text1)
print (len(text1))
print (fdist1)
print (fdist1.most_common(50))