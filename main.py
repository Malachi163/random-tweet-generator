import random
f = open("Tweets.txt", "r")


#big objective - make tweet generator
# smaller objective - make a dictionary of words -> list if objects that follow
tweets = {}
wordBefore = ""

for line in f:
  for word in line.split():
    if wordBefore not in tweets:
      tweets[wordBefore] = [word]

    else:
      tweets[wordBefore].append(word)
    
   # print(word + " follows " + wordBefore)
    wordBefore = word
    

    
word = "America"
newTweet = ""
newTweet = newTweet + word + " "
for i in range(140):
  if word not in tweets:
    break
  nextWords = tweets[word]
  word = (random.choice(tweets[word]))
  newTweet = newTweet + word + " "
  
  
print(newTweet)


# word = "America"
# newTweet = ""
# newTweet = newTweet + word + " "
# for i in range(140):
#   if(word.startswith("https")):
#     del(tweets[i])

#   else:
#     nextWords = tweets[word]
#     word = (random.choice(tweets[word]))
#     newTweet = newTweet + word + " "
  
  
# print(newTweet)
  
  
   


   
   

    
