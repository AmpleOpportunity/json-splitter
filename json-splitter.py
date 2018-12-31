import os
from os import path
import json
import sys
from sys import getsizeof
import math

print('Welcome to the JSON Splitter')
print('First, enter the name of the file you want to split')

try:
    # request file name
    file_name = input('filename: ')
    f = open(file_name)
    file_size = os.path.getsize(file_name)
    data = json.load(f)
    
    if isinstance(data, list):
        data_len = len(data)
        print('Valid JSON file found')
    else:
        print("JSON is not an Array of Objects")
        exit()

except:
    print(sys.exc_info()[0],'exiting')
    exit()

# get numeric input
try:
    mb_per_file = abs(float(input('Enter maximum file size (MB): ')))
except:
    print(sys.exc_info()[0],'exiting')
    exit()

# check that file is larger than max size
if file_size < mb_per_file * 1000000:
    print('File smaller than split size, exiting')
    exit()

# determine number of files necessary
num_files = math.ceil(file_size/(mb_per_file*1000000))
print('File will be split into',num_files,'equal parts')

# initialize 2D array
split_data = [[] for i in range(0,num_files)]

# determine indices of cutoffs in array
starts = [math.floor(i * data_len/num_files) for i in range(0,num_files)]
starts.append(data_len)

# loop through 2D array
for i in range(0,num_files):
    # loop through each range in array
    for n in range(starts[i],starts[i+1]):
        split_data[i].append(data[n])
    
    # create file when section is complete
    name = os.path.basename(file_name).split('.')[0] + '_' + str(i+1) + '.json'
    with open(name, 'w') as outfile:
        json.dump(split_data[i], outfile)
        
    print('Part',str(i+1),'... completed')

print('Success! Script Completed')