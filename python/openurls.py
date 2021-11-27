import webbrowser
import time


def openurl():
    nodes = []
    file = open('ip_addr.txt', 'r')
    for line in file:
        line = line.rstrip()
        line = ''.join(('http://', line, ':63111'))
        nodes.append(line)

    for node in nodes:
        webbrowser.open(node)
        time.sleep(0.5)


if __name__ == '__main__':
    openurl()
