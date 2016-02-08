#!/usr/bin/env python3
from __future__ import print_function
import re

#library functions go here
def pls2m3u(infile, srt=True):
    m_title = re.compile("^\s*Title(\d+)\s*=(.*)$")
    m_file = re.compile("^\s*File(\d+)\s*=(.*)$")
    m_length = re.compile("^\s*Length(\d+)\s*=(.*)$")
    entries = {}
        #read all entries
    for line in infile:
        m = m_file.match(line)
            #set file
        if m:
            if not m.group(1) in entries:
                entries[m.group(1)] = ["", "", ""]
            entries[m.group(1)][1] = m.group(2)
        else:
            m = m_title.match(line)
                #set title
            if m:
                if not m.group(1) in entries:
                    entries[m.group(1)] = ["", "", ""]
                entries[m.group(1)][0] = m.group(2)
            else:
                m = m_length.match(line)
                    #set length
                if m:
                    if not m.group(1) in entries:
                        entries[m.group(1)] = ["", "", ""]
                    entries[m.group(1)][2] = m.group(2)
    ents = list(entries.keys())
    
        #sort entries pertaining to title, if enabled
    if srt:
        ents = [[entries[i][0], i] for i in ents]
        ents.sort()
        ents = [i[1] for i in ents]
        
        #print all entries
    for entry in ents:
        print("#EXTINF:" + entries[entry][2] + "," + entries[entry][0])
        print(entries[entry][1])
        
def m3uPreamble():
    print("#EXTM3U")

#main definition for callable scripts
def main():
    import argparse
    import sys
    parser = argparse.ArgumentParser(description="Generates .m3u entries from other formats (currently only from .pls).")
    parser.add_argument("-new", action="store_true", default=False,
                        help="Generate new .m3u preamble")
    parser.add_argument("-s", action="store_false", default=True,
                         help="Turn off sorting of playlist")
    parser.add_argument("files", nargs="*", metavar="FILE",
                        help="Files for input")
    arguments = parser.parse_args(sys.argv[1:])
    files = arguments.files
        #print .m3u preamble if specified
    if arguments.new:
        m3uPreamble()
        #use stdin if no supplied files
    if len(arguments.files) == 0:
        files = [sys.stdin]
    for f in files:
        infile = f
            #open file for reading if path to file specified
        if isinstance(f, type("")):
            infile = open(f, 'r')
        pls2m3u(infile, srt=arguments.s)
        infile.close()

    #if called from command line
if __name__ == '__main__':
    main()
