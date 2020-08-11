# ****************************************************************************
# * txt2html.py
# * Change mulitple line textfile into small web page
#
# This script takes (multiple) txt files consisting of 8 lines
# and creates an html file.
# Source and Object reside in the same (current) directory
#
# usage:
# python txt2html.py [options]
# use option -h or --help for instructions
#
# release info
# 1.0 first release 10-08-20 Paul Merkx
# ****************************************************************************
import os
import sys
import argparse
import time
import math


RELEASE = '1.0 - 10-8-2020'

def rename(name):
    newname = name.replace("3", "NwHavens3",1)
    newname = newname.replace("_00_", "_BG_")
    newname = newname.replace("_01_", "_1e_")
    return newname

def to_html(filename, extension):
    # to do: add some checking here!
    try:
        with open(filename, 'r') as infile:
            lines = []
            for line in infile:
                lines.append(line)
            infile.close()
    except IOError:
        print("FATAL: Unable to read", filename)
        sys.exit()
    size = len(lines)
    if size != 0:
        html_output = \
"""<html><head><title>%s</title></head>
<body bgcolor="#ffffff" leftmargin=5 topmargin=5 rightmargin=5 bottommargin=5>
<font size=7 color="#000000" face="Times New Roman">
<div><b>%s</b></div>""" % (filename, lines[0].rstrip()) 
        for i in range(1, size):
            html_output = html_output + "<div>" + lines[i].rstrip() + "</div>\r\n"
        html_output += "</font></body></html>" 
    else:
        html_output = \
"""<html><head><title>%s</title></head>
<body bgcolor="#ffffff" leftmargin=5 topmargin=5 rightmargin=5 bottommargin=5>
<font size=7 color="#000000" face="Times New Roman">
<div>Geen gegevens</div>""" % (filename)
    # convert filename

    try:
        with open(rename(filename.replace(extension, ".html")), 'w') as outfile:
            outfile.write(html_output)
            outfile.close()
    except IOError:
        print("FATAL: Unable to write", rename(filename.replace(extension, ".html")), "(probably in use)")
        sys.exit()
    return

    
# ***************************************************************
# *** Main program ***
# ***************************************************************
start = time.time()

print('txt2html ' + RELEASE + ' by (c) Simac Healthcare.')
print('Disclaimer: ')
print('USE THIS SOFTWARE AT YOUR OWN RISK')
print(' ')

# *** Read arguments passed on commandline
parser = argparse.ArgumentParser()
parser.add_argument("-d", "--destination", nargs=1, help="\
                    specify destination directory (default current dir)")
parser.add_argument("-s", "--source", nargs=1, help="\
                    specify source directory (default current dir)")
parser.add_argument("-e", "--extension", nargs=1, help="\
                    specify source extension (default .txt)")

args = parser.parse_args()

# *** Check validity of the arguments
if (args.source)is None:
    print("Files are read from current directory")
    source_dir = '.'
else:
    if os.path.isdir(args.source[0]):
        source_dir = args.source[0]
        print("Files are read from ", source_dir)
    else:
        print("Unable to locate source directory ", args.source)
        sys.exit()
        
if (args.extension) is None:
    print("Source files extension .txt is assumed")
    source_ext = ".txt"
else:
    print("Only processing ", args.extension[0], " files")
    source_ext = args.extension[0]

if (args.destination)is None:
    print("HTML files are written to current directory")
    dest_dir = '.'
else:
    if os.path.isdir(args.destination[0]):
        dest_dir = args.destination[0]
        print("HTML files are written to ", dest_dir)
    else:
        print("Unable to locate destination directory ", args.destination[0])
        sys.exit()

print('Start creating HTML files')

nr_of_files = 0
files = [f for f in os.listdir(source_dir) if os.path.isfile(os.path.join(source_dir, f))]
for f in files:
    # add pathname to file
    f = os.path.join(source_dir, f)
    # check proper extension
    if f.endswith(source_ext):
        print("Converting: ", f, "to", rename(f.replace(source_ext, ".html")))
        to_html(f, source_ext)
        nr_of_files += 1
print("")
end = time.time()
exectime = round(1000*(end-start))
print("Converted", nr_of_files, "files in", exectime, "milliseconds.")
