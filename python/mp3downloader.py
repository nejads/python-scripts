import sys
import urllib2

def main():
    if len(sys.argv) != 3:
        print 'usage: python mp3_downloader name url'
        sys.exit(1)

    filename = sys.argv[1]
    url = sys.argv[2]
    mp3url = urllib2.urlopen(url)
    outputfile = open(filename + '.mp3', 'wb')
    outputfile.write(mp3url.read())
    outputfile.close()

if __name__ == '__main__':
    main()