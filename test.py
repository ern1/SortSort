import SortSort
from sorts import help_sort, quit_sort
#from itertools import count

def is_sorted(l):
    return all(x <= l[i + 1] for i, x in enumerate(l[:-1]))

if __name__ == '__main__':
    l = [1, 2, 3, 4923847293874, 9, 10]
    
    print(f"{l}\nSorted: {is_sorted(l)}\n") # not sorted as you would expect   
    SortSort(l, heepsort, heepsort)         # call sort function
    print(f"{l}\nSorted: {is_sorted(l)}\n") # and just like that, it is still not sorted