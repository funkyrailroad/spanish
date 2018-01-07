#! /usr/bin/python
import sys

filename = sys.argv[1]
readfile = open(filename, 'r')

newname = filename.split('.')[0] + ".ank"
writefile = open(newname, 'w+')
line_list = ''

for line in readfile.readlines():
    # skip comment lines
    if line[0] == '#':
        continue
    # line breaks
    if line == "\n":
        line_list = line_list[:-1] + '\n'
        print repr(line_list)
        writefile.write(line_list)
        line_list = ''
        #exit()
        continue
    line = line.split("\n")[0]
    line_list += line
    line_list += '\t'

writefile.write('\n')

readfile.close()
writefile.close()
