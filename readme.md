# Update

Compatible with Python 3.x to support Unicode File name on Windows platform

Remove GUI

# About Dupelicate Files.
This script will scan a directory tree looking for duplicate files, it uses a two stage approach of comparing file sizes and then hashs of file contents to find duplicates.

## Running Duplicate files.
An example of running this script to just list all the duplicate files would be:
    python DuplicateFiles.py /Users/Daniel/Documents
    
An example of running this script to list and delete all the duplicate files would be:
        python DuplicateFiles.py /Users/Daniel/Documents -remove
