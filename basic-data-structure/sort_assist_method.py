def less(x, y):
    return x < y


def exch(alist, i, j):
    alist[i], alist[j] = alist[j], alist[i]


def show(alist):
    for i in range(len(alist)):
        print(alist[i] + " ", end='')


def is_sorted(alist):
    return all(alist[i] < alist[i+1] for i in range(len(alist)-1))


