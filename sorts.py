from itertools import permutations
from collections import abc

def swat(seq: abc.MutableSequence, i, j):
    seq[i], seq[j] = seq[j], seq[i]

def help_sort(it: abc.Iterable):
    return sorted(it)

def quit_sort(it: abc.Iterable):
    return it

# TODO: implementera
def long_sort(it: abc.Iterable):
    for p in permutations(enumerate(it)):
        if (x for _, x in p) == (*it,):
        # TODO: spara p[0] för att använda nedan när jag skapar sorterad lista?
            break
        
    # for i, _ in s:
    #     new_it = 