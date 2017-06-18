# Python function to compute the Nim sequence from a sequence.
# This is very slow, DO NOT use it.

import numpy as np

def nimseq_func(seq, n):
  # There is no NA for integers in numpy...
  nimseq = -np.ones(n, dtype = 'int')
  biggest_possible_number = 0

  for site in range(n):
      #if site % np.floor(n/100) == 0:
      #    print(str(np.int(np.floor(100*site/n))) + '%')

      next_one = np.ones(biggest_possible_number + 1, dtype = 'bool')
  
      for seq_i in seq:
          if(site - seq_i < 0):
              # the next one is negative, so the next ones too, 
              # and we can break the computation here
              break
          else:
              not_it = nimseq[site - seq_i]
              next_one[not_it] = 0
              
      # np.argmax returns first occurence of True cf documentation 
      # https://docs.scipy.org/doc/numpy/reference/generated/numpy.argmax.html
      next_nim_seq = np.argmax(next_one)
      nimseq[site] = next_nim_seq
      # print(nimseq)
      if(next_nim_seq == biggest_possible_number):
          print('A new number for site ' + str(site) + ': ' + str(biggest_possible_number))
          biggest_possible_number += 1
  return nimseq