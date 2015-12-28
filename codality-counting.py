

# Worst-case senario of this algorithm is O(N^2) becouse we go through the
# possitions list to find -1. This iteration can repleace with a variable named
# uncovered that have X value and each time we found a way decrement once.
# Once the uncovered variable become zero we find out all positions has covered
# so we can return the time of that which is index of the item in the list.
def frog_jump_n2(X, A):
    positions = [-1] * X
    for i in A:
        if i-1 < X and positions[i-1] == -1:
            positions[i-1] = i
        if -1 not in positions:
            return A.index(i)
    else:
        return -1


# So we can improve the algorithm as following:
def frog_jump(X, A):
    positions = [-1] * X
    uncovered = X
    for i in A:
        if i-1 < X and positions[i-1] == -1:
            positions[i-1] = i
            uncovered -= 1
        if uncovered == 0:
            return A.index(i)
    else:
        return -1


# Same technique can be used to find a list is a permutation
def perm_check(A):
    com = [-1] * len(A)
    uncovered = len(A)
    for item in A:
        if item > len(A):
            return 0
        if com[item-1] == -1:
            com[item-1] = item
            uncovered -= 1
        if com[item-1] == item:
            return 0
    if uncovered == 0:
        return 1
    else:
        return 0


def missing_element(A):
    if len(A) == 0:
        return 0

    else:
        seen = [False] * len(A)
        for item in A:
            if 0 < item <= len(A):
                seen[item-1] = True
        for s in seen:
            if s is False:
                return seen.index(s)+1
        return 0


def remove_duplicate(l):
    return list(set(l))


def max_counter(N, A):
    counters = [0] * N
    max_val = 0
    for item in A:
        if 0 < item <= N:
            counters[item-1] += 1
            if max_val < counters[item-1]:
                max_val = counters[item-1]
        elif item == N+1:
            counters = [max_val] * N
        else:
            return -1
    return counters


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
    test(frog_jump(5, [1, 3, 1, 4, 2, 3, 5, 4]), 6)
    test(frog_jump(7, [1, 7, 3]), -1)
    test(frog_jump(6, [1, 7, 3]), -1)
    test(frog_jump(7, []), -1)
    test(frog_jump(2, [2, 2, 2, 2, 2]), -1)
    print('Missing element')
    test(missing_element([1, 3, 6, 4, 1, 2]), 5)
    print('Max counter')
    test(max_counter(5, [3, 4, 4, 6, 1, 4, 4]), [3, 2, 2, 4, 2])


# Standard boilerplate to call the main() function.
if __name__ == '__main__':
    main()
