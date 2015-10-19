__author__ = 'kayla'
import os


data_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'data')
files = os.listdir(data_dir)
output_file = 'combined_ssRNA.tsv'
combined = list()
print "Starting to combine"
for input_file in files:
    with open(os.path.join(data_dir, input_file), 'rb') as tsv:
        for line in tsv:
            #  Format of the line: Name\tStart\tEnd\tFlag\tDescription\n
            combined.append(line)
print "Starting to write"
with open(output_file, 'wb') as out:
    for line in combined:
        out.write(line)
