import csv
import re


with open('instances.txt', 'r') as in_file:
    stripped = (line.strip() for line in in_file)
    lines = (re.split(' |,',line) for line in stripped if line)
    with open('sample_test/'+'instances.csv', 'w') as out_file:
        writer = csv.writer(out_file)
        # writer.writerow(('title', 'intro'))
        writer.writerows(lines)