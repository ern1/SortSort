from collections import abc, Sequence

def sort_sort(seq: Sequence, fn1, fn2) -> list:
    assert isinstance(seq, (Sequence, abc.Iterable)), "(-__-)┌∩┐" # lol
    
    size = len(seq)
    l1, l2 = fn1(seq[:size]), fn2(seq[size:])
    return [fn2(l1), fn1(fn2([l2[1:], *l2[-size]]))]
