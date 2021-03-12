import string
import random

fname = "pg5200.txt"

with open(fname) as file:
  lines = file.readlines()

sentences = []
# word_list = []

word_dict = {} #Each word is a key with the value being list of tuples with the coordinates (line no, word no)

for items in lines:
  sentences.append(items.split()) 

line_counter = 0 
for line in sentences:
  line_counter += 1
  word_counter = 0 
  for word in line:
    word_counter += 1
    word = word.lower() #Change all Uppercase to Lowercase
    word = word.strip() #Remove whitespace
    word = word.translate(str.maketrans('', '', string.punctuation)) #Remove punctuation
    word_dict.setdefault(word, []).append((line_counter,word_counter)) #populating word_dict
    # word_list.append(word)

message = 'let us not Say We met Late at the night about the secret'

message_words = message.split() 
message_words_filtered = [] 

for i in message_words:
  i = i.lower() #make all words lowercase
  i = i.strip() #remove whitespace
  i = i.translate(str.maketrans('', '', string.punctuation)) #Remove punctuation
  message_words_filtered.append(i)

encrypted_message = []
freq_dict = {}


for filtered_words in message_words_filtered: # https://www.geeksforgeeks.org/counting-the-frequencies-in-a-list-using-dictionary-in-python/
  if (filtered_words in freq_dict):
    freq_dict[filtered_words] += 1
  else:
    freq_dict[filtered_words] = 1


for filt_words in message_words_filtered:
  assert freq_dict[filt_words] < len(word_dict[filt_words]) #making sure there are enough unique tuples for the 
  my_tuple = random.choice(word_dict[filt_words])
  word_dict[filt_words].remove(my_tuple)
  encrypted_message.append(my_tuple)

print(encrypted_message)


# for key,value in word_dict.items():
#   print(key, value)