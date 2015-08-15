"""Find duplicate files inside a directory tree."""

import os
from os import walk, remove, stat
from os.path import join as joinpath
#from md5 import md5
import hashlib

def find_duplicates( rootdir ):
    """Find duplicate files in directory tree."""
    filesizes = {}
    # Build up dict with key as filesize and value is list of filenames.
    for path, dirs, files in walk( rootdir ):
        for filename in files:
            try:
                filepath = joinpath( path, filename )
                filesize = stat( filepath ).st_size
                filesizes.setdefault( filesize, [] ).append( filepath )
            except:
                print("can not handle:"+filepath)
    unique = set()
    uniquefile = {}
    duplicates = set()
    # We are only interested in lists with more than one entry.
    for files in [ flist for flist in filesizes.values() if len(flist)>1 ]:
        print(files)
        for filepath in files:
            print(filepath)
            with open( filepath , "rb") as openfile:
                content = openfile.read()
                filehash = hashlib.md5(content).hexdigest()
                print(filehash)
                if filehash not in unique:
                    unique.add( filehash )
                    uniquefile[filehash] = []
                else:
                    duplicates.add( filehash )
                uniquefile[filehash].append(filepath)
    return duplicates, uniquefile

if __name__ == '__main__':
    from argparse import ArgumentParser
    PARSER = ArgumentParser( description='Finds duplicate files.' )
    PARSER.add_argument( '-root', metavar='<path>', default = '', help='Dir to search.' )
    PARSER.add_argument( '-remove', action='store_true', 
                         help='Delete duplicate files.' )
    ARGS = PARSER.parse_args()

    if ARGS.root == '':
        PARSER.print_help()
    else:
        DUPS, FILES= find_duplicates( ARGS.root )
        print ('%d Duplicate files found.' % len(DUPS))
        for f in sorted(DUPS):
            if ARGS.remove == True:
                print("----------------------")
                for i in range(1, len(FILES[f])):
                    print('\tDeleted '+ FILES[f][i])    
                    os.remove(FILES[f][i])                   
            else:
                print ("----------------------")
                for name in FILES[f]:
                    print(name)

