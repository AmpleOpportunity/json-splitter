import sys
import os
import json
import math

if sys.version_info[0] < 3:
    print('This script requires Python 3 or higher')
    exit()
    
print('Welcome to the JSON Splitter')
print('First, enter the name of the file you want to split')

try:
    # request file name
    file_name = input('filename: ')
    f = open(file_name)
    data = json.load(f)
    number_of_records = len(data)
    
    if isinstance(data, list):
        data_len = len(data)
        print('Valid JSON file found')
        print(number_of_records)
    else:
        print("JSON is not an Array of Objects")
        input("Press any key to exit")
        exit()

except:
    print('Error loading JSON file, exiting')
    input("Press any key to exit")
    exit()

# get numeric input
try:
    records_per_file = abs(float(input('Enter number of records for each JSON: ')))
except:
    print('Error entering number of records, exiting')
    input("Press any key to exit")
    exit()

# check that file is larger than max size
if records_per_file > number_of_records:
    print('Less records than split size, exiting')
    input("Press any key to exit")
    exit()

# determine number of files necessary
num_files = math.ceil(records_per_file/number_of_records * 100)
print('File will be split into',num_files,' files.')
input('Press any key to begin')

# initialize 2D array
split_data = [[] for i in range(0,num_files)]

# determine indices of cutoffs in array
starts = [math.floor(i * number_of_records/num_files) for i in range(0,num_files)]
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
input('Press any key to exit')
