###
# how can I detect a link and put it into <a> tag. This is the question:
# I have a text which could be html or plain text, and i would like to linkify
# it.

# Example 1: input 'www.walla.com'
# output: '<a href="http://www.walla.com" rel="nofollow">www.walla.com</a>'

# Example 2: input: '<a href="http://www.walla.com" rel="nofollow">www.walla.
# com</a>'
# output: '<a href="http://www.walla.com" rel="nofollow">www.walla.com</a>'

# Example 3:
# input: '<html>www.walla.com</html>'
# output: '<html><a href="http://www.walla.com" rel="nofollow">www.walla.com
# </a></html>'
###

import sys
import re


def check(input):
    match = re.search(r'\w{3}\.\w+\.(com|org|se)', input)
    if match:
        part1 = '<a href="'
        part2 = '" rel="nofollow">'
        part3 = '</a>'
        found = match.group()
        print part1 + found + part2 + found + part3
    else:
        print 'Did not found'


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print 'usage: ./regex.py INPUT'
        sys.exit(1)
    check(sys.argv[1])
