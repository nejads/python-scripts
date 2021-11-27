def frog_jump(x, y, d):
    jump = (y-x) / d
    if (y-x) % d == 0:
        return jump
    else:
        return jump + 1


def missing_element(mylist):
    if len(mylist) != 0:
        total = (len(mylist)+1) * (len(mylist)+2) / 2
        for item in mylist:
            total -= item
        return total
    else:
        return 1


def missing_element_xor(mylist):
    if len(mylist) != 0:
        result = 0
        for item in mylist:
            result ^= item
        return result
    else:
        return 1


def tape_equilibrium_n2(mylist):
    tape = [0] * len(mylist)
    for i in xrange(len(mylist)):
        tape[i] = abs(sum(mylist[:i]) - sum(mylist[i:]))
    return min(tape)


def tape_equilibrium(mylist):
    if len(mylist) == 0:
        return 0
    else:
        head = mylist[0]
        tail = sum(mylist[1:])
        min_diff = abs(head - tail)
        for index in xrange(1, len(mylist)):
            head += mylist[index]
            tail -= mylist[index]
            tmp_diff = abs(head - tail)
            if tmp_diff < min_diff:
                min_diff = tmp_diff
        return min_diff


# Provided simple test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))


def main():
    print('Frog jump')
    test(frog_jump(10, 70, 30), 2)
    test(frog_jump(10, 80, 30), 3)
    print('Missing element')
    test(missing_element([2, 3, 1, 5]), 4)
    test(missing_element([2, 3, 4]), 1)
    test(missing_element([]), 1)
    test(missing_element([2, 3, 1, 4]), 5)
    print('Missing element by xor')
    test(missing_element([2, 3, 1, 5]), 4)
    test(missing_element([2, 3, 4]), 1)
    test(missing_element([]), 1)
    test(missing_element([2, 3, 1, 4]), 5)
    print('Tape equilibrium')
    test(tape_equilibrium([3, 1, 2, 4, 3]), 1)
    test(tape_equilibrium([3, 3]), 0)
    test(tape_equilibrium([1]), 1)
    test(tape_equilibrium([]), 0)



# Standard boilerplate to call the main() function.
if __name__ == '__main__':
    main()
