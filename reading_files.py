import csv
from pprint import pprint
opened_file = open('shakespeare.txt')
read_file = opened_file.read()
print(read_file[:100])
#Instead of reading an entire chunk of the file at once, we can use a for loop to read the file data line by line,
#readline creates a single list
opened_file = open('shakespeare.txt')
file_lines = opened_file.readlines()
print(file_lines[:5])

for line in file_lines[:5]:
    stripped_line = line.rstrip()
    print(stripped_line)



## Reading Line by line 
with open ('shakespeare.txt', 'r') as infile:    
    for line in infile:
        print(line)  # print out each line in the file 


file_lines = [] # List to hold the lines. 
with open ('shakespeare.txt', 'r') as infile:    
    for line in infile:
        file_lines.append(line)

print(f'file_lines has {len(file_lines)} lines in it.')


file_lines[0]
file_lines[2]

for c,line in enumerate(file_lines):
    if c < 10:     
        print(line)
    else:
        break
    

for c,line in enumerate(file_lines):
    if c < 10:     
        print(line.strip())
    else:
        break
    
## Key need to store data as list of list 

with open ('scientists.csv', 'r') as infile:    
    for line in infile:
        print(line)


opened_file = open('scientists.csv')
file_lines = opened_file.readlines()
for line in file_lines[:5]:
    stripped_line = line.rstrip()
    print(stripped_line)

### now we need to make it a list of list
opened_file = open('scientists.csv')
file_lines = opened_file.readlines()
for line in file_lines[1:]:
    stripped_line = line.rstrip()
    stripped_line=stripped_line.split(',')
    print(stripped_line[0])
    
    
csv_text = []
with open('scientists.csv', 'r') as infile:
    for line in infile:
        csv_text.append(line)
        
csv_text
header = csv_text[0].split(",")


for item in csv_text[1:]:
    data_line = item.strip().split(',')
    print(data_line)
    
    

scientists = []

for item in csv_text[1:]:
    data_line = item.strip().split(',')
    data_dict= dict(zip(header,data_line))
    scientists.append(data_dict)


scientists

for row in scientists[:5]:
    print(row['Name'])
    
science=[]
for item in csv_text[1:]:
    data_line = item.strip().split(',')
    science += [{ 'Name': data_line[0], 'Born': data_line[1], 'Died': data_line[2], 'Age': data_line[3], 'Occupation': data_line[4]  } ]             

science

alpha=["a","beta"]
rex=["handy","candy"]

for a,b in zip(alpha,rex):
    print(a,b)
    
from csv import reader
of=open("scientists.csv")
files=reader(of)
my_file=list(files)
print(my_file)

for row in my_file[1:]:
    print(row[0],row[1],row[2])
    
import csv

with open('data_wk1/scientists.csv', 'r') as infile:
    reader = csv.reader(infile)
    for line in reader:
        print(line)
        
        


with open('scientists.csv', 'r') as infile:
    reader = csv.DictReader(infile)  
    for line in reader:
        pprint(line)
        
        
with open('data_wk1/scientists.csv', 'r') as infile:
    reader = csv.DictReader(infile) 
    print(f'Headers: {reader.fieldnames}')