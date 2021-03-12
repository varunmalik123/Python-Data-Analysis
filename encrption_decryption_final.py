def encrypt_message(message,fname):
  '''
  Given `message`, which is a lowercase string without any punctuation, and `fname` which is the
  name of a text file source for the codebook, generate a sequence of 2-tuples that
  represents the `(line number, word number)` of each word in the message. The output is a list
  of 2-tuples for the entire message. Repeated words in the message should not have the same 2-tuple. 

  :param message: message to encrypt
  :type message: str
  :param fname: filename for source text
  :type fname: str
  :returns: list of 2-tuples
  '''
  assert(isinstance(message, str))
  assert(isinstance(fname, str))

  import string
  import random

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
    word_dict[filt_words].remove(my_tuple) #Removes my tuple from the dict so it cannot be selected again
    encrypted_message.append(my_tuple)

  return encrypted_message



def decrypt_message(inlist,fname):
  '''
  Given `inlist`, which is a list of 2-tuples`fname` which is the
  name of a text file source for the codebook, return the encrypted message. 

  :param message: inlist to decrypt
  :type message: list
  :param fname: filename for source text
  :type fname: str
  :returns: string decrypted message
  '''
  assert(isinstance(fname, str))
  assert(isinstance(inlist, list))
  
  import string
  import random


  for item in inlist:
    assert(isinstance(item, tuple))

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
      

  decrypted_message = []

  for tuples in inlist:
    for keys,values in word_dict.items():
      if tuples in values:
        decrypted_message.append(keys)

  decrypted_str = ' '.join(word for word in decrypted_message)
  
  return decrypted_str






