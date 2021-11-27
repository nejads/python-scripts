# This is training of algorithms and data structures in python.
def binary_search(myitem, mylist):
    found = False
    cost = 0
    bottom = 0
    top = len(mylist)-1
    while bottom <= top and not found:
        cost += 1
        mid = (bottom+top)//2
        if myitem == mylist[mid]:
            found = True
        elif myitem < mylist[mid]:
            top = mid - 1
        else:
            bottom = mid + 1
    return found, cost


#################################
# Helper function to chunk a list
#################################
def chunks(mylist, nr_chunks):
    l1 = mylist[0:(len(mylist)/2)-1]
    l2 = mylist[(len(mylist)/2):len(mylist)]
    return l1, l2


if __name__ == '__main__':
    mylist = input('Insert your list: ')
    myitem = input('Item you looking for: ')
    i = binary_search(myitem, mylist)
    print('Found: ' + str(i[0]))
    print('Cost of the searching: ' + str(i[1]))
