# coding=utf-8
import os
import re
import sys
import fnmatch


def main():
    if len(sys.argv) != 2:
        print 'usage: python DedrmAndSendToKindle.py /path/to/file.epub'
        sys.exit(1)
    # Local variables
    path_to_file = sys.argv[1]
    file_name = get_file_name(path_to_file)
    first_word = Unswedish(file_name.split(' ')[0])
    path_to_Dedrm_file = ""
    calibre_path = '/Path/to/Calibre/folder'
    kindle_path = 'Path/to/kindle/folder/on/the/local/dropbox'

    # print some info for user
    print_info(path_to_file, file_name, first_word)
    # DeDrm file using calibre dedrm plugin
    os.system('calibredb add ' + '"' + path_to_file + '"')
    # Find dedrmed file path in calibre folder
    path_to_Dedrm_file = do_script(calibre_path, first_word)
    # Convert epub to mobi and save it on kindle drive.
    os.system('ebook-convert ' + '"' + path_to_Dedrm_file + '"' + \
              kindle_path + first_word + '.mobi')


# Get file name from path
def get_file_name(path_to_file):
    matchobj = re.search(r'[^/]*(?=\.[^.]+($|\?))', path_to_file)
    if matchobj:
        return matchobj.group()
    else:
        print "not found"


# Replace special swedish character with a and o
def Unswedish(first_word):
    first_word = first_word.replace('Å', 'A')
    first_word = first_word.replace('å', 'a')
    first_word = first_word.replace('Ä', 'A')
    first_word = first_word.replace('ä', 'a')
    first_word = first_word.replace('Ö', 'O')
    first_word = first_word.replace('ö', 'o')
    return first_word


def do_script(calibre_path, first_word):
    # delete next line from th end
    return os.popen(
        'find ' + calibre_path + ' -name ' + first_word + '*.epub').read()[:-1]


# Unused method
def find_files(directory, pattern):
    for root, dirs, files in os.walk(directory):
        for basename in files:
            if fnmatch.fnmatch(basename, pattern):
                filename = os.path.join(root, basename)
                yield filename


def print_info(path_to_file, file_name, first_word):
    print "-------------------------------------------------------------------"
    print "___________________________  HAPPY DeDRMing!  _____________________"
    print "###################################################################"
    print "### This script will be Dedrm your *.epub file and convert epub to "
    print "### mobi which is compatible with Amazone Kindle and save it to a "
    print "### Dropbox folder connected to Amazone cloud. All you need is to "
    print "### install CALIBRE with DeDrm pluging in your machine and then "
    print "### run this script. "
    print '### path_to_file: ' + path_to_file
    print '### file_name: ' + file_name
    print '### first word in file name without swedish chars: ' + first_word
    print "###################################################################"
    print "-------------------------------------------------------------------"

# Standard boilerplate to call the main() function.
if __name__ == '__main__':
    main()
