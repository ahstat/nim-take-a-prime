import numpy as np

def generate_seq(type_seq = 'primes', n = 1000):
    if(type_seq == 'primes'):
        return(generate_seq_primes(n))

# From https://stackoverflow.com/questions/2068372/
# primes return prime number in [1,n] = [1, n+1[
def generate_seq_primes(n):
    from sympy import sieve
    primes = np.array(list(sieve.primerange(1, n+1)), dtype='int')
    return(primes)

# Ex:
# input : seq = numpy.array([2, 3, 5, 7]),  n = 10
# output: 0 1 1 0 1 0 1 0 0 0
#
# Note: output index begin with 1 
# (see the position of the first 1 in the previous example)
def to_hot_vector(seq, n):
    hot_seq = np.zeros(n, dtype='int')
    hot_seq[seq-1] = 1
    return hot_seq


# Option 1: one element to check, one column for input and output
# Option 2: many elements to check, one row for each seq for input and output
# This automatically checked with the type of object.
# outfile is the directory
# If seq is a numpy array: save as one column (easier to load)
# If many arrays in seq: save each array as one line
def saving_seq(seq, outfile):
    if(type(seq) == list): # For saving multiple arrays of different sizes
        # https://stackoverflow.com/questions/9565426
        with open(outfile,"w") as f:
            f.write("\n".join(",".join(map(str, x)) for x in seq))
    else: # For saving 1 array
        np.savetxt(outfile, seq, delimiter=',', fmt='%d') 