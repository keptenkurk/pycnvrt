This utility is a customer specific version of a converter utility
which converts text files found in a directory to html files.
Also the filename will be renamed.

This project can be used and reworked for other purposes where
all files found in the source directory with matching extension 
need to be processed line by line and output is written to a new
file.

Specifics for this implementation:
usage:
txt2html [-s source dir] [-d destination dir] [-e source extension][-h help]
    optional source dir: directory to search for input files [default: current dir]
    optional destination directory to write results to [default: current dir]
    optional source extension [default: .txt]
    
This generates a html file per text file following a given html template
for easy viewing on a smartphone.

The dist folder contains a windows executable of the shown script using
Pyinstaller (https://datatofish.com/executable-pyinstaller/)

    

    
    