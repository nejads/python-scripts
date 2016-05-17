import sys
import re
import subprocess
import webbrowser


def check(youtube):
    print "Hej again"
    yt_id = youtube.split('https://www.youtube.com/watch?v=')[1].split('&')[0]
    peggo_url = 'http://peggo.co/dvr/' + yt_id + '#rv'
    write_to_clipboard(peggo_url)
    webbrowser.open(peggo_url)
    print peggo_url
    # match = re.search(r'https://www.youtube.com/watch\?v=', youtube)
    # if match:
    #     found = match.group()
    #     print found
    # else:
    #     print 'Not found''

def write_to_clipboard(output):
    process = subprocess.Popen(
        'pbcopy', env={'LANG': 'en_US.UTF-8'}, stdin=subprocess.PIPE)
    process.communicate(output.encode('utf-8'))

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print 'usage ./MakeUrl.py INPUT'
        sys.exit(1)
    check(sys.argv[1])
