import SortSort as ss
from sorts import help_sort, quit_sort

def is_sorted(seq):
    return all(x <= seq[i + 1] for i, x in enumerate(seq[:-1]))

def test_ss(seq, f1, f2):
    print(f"{seq}\nSorted: {is_sorted(l)}\n") # not sorted as you would expect
    ss.sort_sort(seq, f1, f2)                  # call sort function
    print(f"{seq}\nSorted: {is_sorted(l)}\n") # and just like that, it is still not sorted

if __name__ == '__main__':
    l = [1, 2, 3, 4923847293874, 9, 10]
    test_ss(l, help_sort, quit_sort)
