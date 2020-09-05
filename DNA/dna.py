from sys import argv, exit
import csv, re

# Checking if the user provided requisite number of arguments
if len(argv) != 3:
    print("Invalid number of arguments")
    exit()

# opening the csv file for reading
file1 =  open(argv[1], 'r')

# using the dictreader method to access the column headings
database = csv.DictReader(file1)
headings = database.fieldnames[1:]

# opening the second file
file2 =  open(argv[2], 'r')
sequence = file2.read()

# using regex to calculate the longest consecutive occurence of STR
occur = []
for i in headings:
    res = max(re.findall('((?:' + re.escape(i) + ')*)', sequence), key = len)
    occur.append(int(len(res)/len(i)))

pattern = ""
for i in occur:
    pattern = str(pattern+str(i)+',')
fin_pattern = pattern.rstrip(',')
# print(fin_pattern)

# converting the csv file data into a list of string data
sequence_list = []
names_list = []
for line in file1:
    new = line.split(',')
    names_list.append(new[0])
    arr = new[1:]
    str  = ""
    for value in arr:
        str = str + value+','
    str = str.rstrip('\n,')
    sequence_list.append(str)

# matching the csv dna data with the pattern created from the text file
count = 0
for i in sequence_list:
    if i == fin_pattern:
        print(names_list[count])
        exit()
    count = count + 1

print("No match")

















