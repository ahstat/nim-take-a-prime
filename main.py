###########################
# Imports and compilation #
###########################
import os
main_dir = 'E:/gitperso/nim-take-a-prime'
os.chdir(main_dir)

import numpy as np
import subprocess # to call C++ program
from helpers.generate_seq import generate_seq, saving_seq
from helpers.make_dir import makedir
import pandas as pd # for read_csv and data management
from helpers.plotting import line_plot, stacked_plot

# Compilation of the C++ code
# mingw32-make.exe -f Makefile
cpp_dir = main_dir + '/helpers/cpp'
subprocess.call(['mingw32-make.exe', '-f', 'Makefile'], cwd = cpp_dir)

##############
# Parameters #
##############
type_seq = 'primes'

# Compute the sequence of the first n_list[n] primes
# 32452843 corresponds to the 2 million first primes
n_list = [1000, 10000, 100000, 1000000, 10000000, 32452843]

#########################
# 0. Create directories #
#########################
out_dir = 'outputs/' + type_seq + '/'
set_dir = out_dir + 'sets/'
nim_dir = out_dir + 'nims/'
plot_dir = out_dir + 'plots/'
makedir('outputs')
makedir(out_dir)
makedir(set_dir)
makedir(nim_dir)
makedir(plot_dir)

############################
# 1. Compute the sequences #
############################
# Set of primes
for n in n_list:
    out_file = set_dir + type_seq + '_' + str(n) + '.csv'
    if not os.path.isfile(out_file):
      seq = generate_seq(type_seq, n)
      saving_seq(seq, out_file)

# Set of primes adding 1
n = 10000
seq = generate_seq(type_seq, n)

seq_with_1 = np.append(1, seq)
out_file = set_dir + type_seq + '_with_1_' + str(n) + '.csv'
saving_seq(seq_with_1, out_file)

# Set of primes without 2
seq_without_2 = seq[1:]
out_file = set_dir + type_seq + '_without_2_' + str(n) + '.csv'
saving_seq(seq_without_2, out_file)

########################################
# 2. Compute the related Nim functions #
########################################
files_to_compute = os.listdir(set_dir)

for file in files_to_compute:
  if not os.path.isfile(nim_dir + file):
    print(nim_dir + file)
    subprocess.call([cpp_dir + '/nimseq.exe', 
                     set_dir + file, 
                     nim_dir + file,
                     file.split('_')[-1].split('.')[0]]) # retrieve n

########################
# 3. Sequence analysis #
########################
nimseq = pd.read_csv(nim_dir + files_to_compute[1], sep=',', header=None)
nimseq = nimseq[0] # pandas Series
# np.array(nimseq) # numpy array

filename = plot_dir + 'sequence_firsts.png'
line_plot(nimseq, filename, width = 480, height = 350)

filename = plot_dir + 'percent_stack_large.png'
stacked_plot(nimseq, filename, width = 1280, height = 1024)

filename = plot_dir + 'percent_stack.png'
stacked_plot(nimseq, filename, width = 550, height = 550)