from SortSort import sort_sort
import sorts as s


def is_sorted(seq):
    return all(x <= seq[i + 1] for i, x in enumerate(seq[:-1]))


def test_ss(seq, f1, f2):
    print(f"{seq}\nSorted: {is_sorted(seq)}\n")       # not sorted as you would expect
    seq_ss = sort_sort(seq, f1, f2)                # call sort function
    print(f"{seq_ss}\nSorted: {is_sorted(seq_ss)}\n") # and just like that, it is still not sorted


if __name__ == '__main__':
    l = [1, 2, 3, 4923847293874, 9, 10]
    test_ss(l, s.help_sort, s.quit_sort)
    # test_ss(l, s.long_sort, s.indecisive_sort)
    