def SortSort(data, fn1, fn2):
    # if not type(data):
    #     return hehe("-_-") # lol
    size = len(data)
    l1, l2 = fn1(data[:size]), fn2(data[size:])
    return [fn2(l1), fn1(fn2([l2[1:], l2[-size]]))]
