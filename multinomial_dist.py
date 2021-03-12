import random

def multinomial_sample(n,p,k=1):
  """
  The purpose of this function is to use the concepts of Multinomial distribution to return 
  sames given n, p and k 
  
  :param n(int) : no. of samples
  :param p(list): Probability Mass Value corresponding to each outcome
  :param k(int) : no. of independant trials
 

  """
  assert isinstance(n, int)
  assert isinstance(p, list)
  assert isinstance(k, int)
  assert n > 0 and k > 0
  assert sum(p) == 1 #All probabilities should add upto one 

  samples_list = []
  no_outcomes = len(p)


  for trial in range(k):
    probability_mass_function = []
    weighted_outcomes = random.choices(range(no_outcomes), weights=p, k=n) # #Will store the outcomes for each sample. https://docs.python.org/3/library/random.html
    
    for each_outcome in range(no_outcomes): #For each outcome
      freq = weighted_outcomes.count(each_outcome) #Count the number of times outcome appears in results
      probability_mass_function.append(freq)
    
    samples_list.append(probability_mass_function)
  

  return samples_list

# print(multinomial_sample(10,[1/3,1/3,1/3],k=10))