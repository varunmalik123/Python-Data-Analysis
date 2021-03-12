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
    

inlist = [(1394, 2), (1773, 11), (894, 10), (840, 1), (541, 2), (1192, 5), (1984, 7), (2112, 6), (1557, 2), (959, 8), (53, 10), (2232, 8), (552, 5)]

decrypted_message = []

for tuples in inlist:
  for keys,values in word_dict.items():
    if tuples in values:
      decrypted_message.append(keys)

decrypted_str = ' '.join(word for word in decrypted_message)
print(decrypted_str)

