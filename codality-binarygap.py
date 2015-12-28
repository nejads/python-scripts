def binary_gap(N):
    max_zero = 0
    nr_zero = 0
    first_one = False
    binary = '{0:b}'.format(N)
    for char in binary:
        if int(char) == 1:
            first_one = True
            if max_zero < nr_zero:
                max_zero = nr_zero
                nr_zero = 0
            else:
                nr_zero = 0
        elif int(char) == 0:
            if first_one:
                nr_zero += 1
        else:
            print 'Something bad happend'
        binary = int(binary) >> 1
    return max_zero


# Find unpaired element in an array.
# Time complixity O(n^2)
def find_unpaired_n2(A):
    result = -1
    for item in A:
        count = A.count(item)
        if count % 2 != 0:
            unpaired = item
    return result


# Find unpaired element in an array.
# Time complixity O(n)
def find_unpaired_n1(A):
    result = 0
    for number in A:
        result ^= number
    return result


# Provided simple test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))


def main():
    print('Binary gap')
    test(binary_gap(1041), 5)
    test(binary_gap(20), 1)
    test(binary_gap(529), 4)
    print('Find unpaired_n2')
    test(find_unpaired_n2([9, 3, 9, 3, 7, 9, 9]), 7)
    test(find_unpaired_n2([1, 2, 3, 4, 5, 6, 7, 8, 9]), 9)
    test(find_unpaired_n2([]), -1)
    test(find_unpaired_n2([1]), 1)
    test(find_unpaired_n2([42]), 42)
    test(find_unpaired_n2([1, 3, 1]), 3)
    test(find_unpaired_n2([1, 2, 1]), 2)
    print('Find unpaired_n1')
    test(find_unpaired_n1([9, 3, 9, 3, 7, 9, 9]), 7)
    test(find_unpaired_n1([1, 2, 3, 4, 5, 6, 7, 8, 9]), 9)
    test(find_unpaired_n1([]), -1)
    test(find_unpaired_n1([1]), 1)
    test(find_unpaired_n1([42]), 42)
    test(find_unpaired_n1([1, 3, 1]), 3)
    test(find_unpaired_n1([1, 2, 1]), 2)


# Standard boilerplate to call the main() function.
if __name__ == '__main__':
    main()
