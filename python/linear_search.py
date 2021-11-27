# This is training of algorithms and data structures in python.
def linear_search(myitem, mylist):
    i = 0
    for item in mylist:
        if item == myitem:
            i += 1
            return i, mylist
        i += 1
    mylist.append(myitem)
    return i, mylist

if __name__ == '__main__':
    mylist = input('Insert your list: ')
    myitem = input('Item you looking for: ')
    i = linear_search(myitem, mylist)
    print('Cost of the searching: ' + str(i[0]))
    print('my list is: ' + str(i[1]))
