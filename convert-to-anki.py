#! /usr/bin/python
import sys

filename = sys.argv[1]
readfile = open(filename, 'r')

newname = filename.split('.')[0] + ".ank"
writefile = open(newname, 'w')

for line in readfile.readlines():
    # skip comment lines
    if line[0] == '#':
        continue

    # line breaks
    if line == "\n":
        writefile.write("\n")
        continue
    line = line.split("\n")[0]
    writefile.write(line)
    writefile.write('\t')

writefile.write('\n')

readfile.close()
writefile.close()
