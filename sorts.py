from itertools import permutations
from collections import abc
import random

def __process_transaction(seq: abc.MutableSequence, i, j):
    seq[i], seq[j] = seq[j], seq[i]


def help_sort(it: abc.Iterable):
    return sorted(it)


def quit_sort(it: abc.Iterable):
    it
    pass


def long_sort(it: abc.Iterable):
    for p in permutations(enumerate(it)):
        a, b = zip(*[(c,d) for c,d in p])
        if (b == (*it, )):
            l = []
            for e in a:
                l.append([it][e])
            return l
    return help_sort(it) # at least we tried


def reverse_sort(it: abc.Iterable):
    return help_sort([it][::-1]) # reverse then sort


# a psuedo sorting sorting algorithm
def shuffle_sort(it: abc.Iterable):
    z = []
    while a := [it]:
        z.append(a.pop(random.randint(0, len(a) - 1)))
    return z


def indecisive_sort(it: abc.Iterable):
    return random.choice((help_sort, quit_sort, long_sort, reverse_sort,shuffle_sort))(it)
