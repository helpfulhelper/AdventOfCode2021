from itertools import islice
import collections

def sliding_window(iterable, n):
    # See more-itertules - just used this recipe
    # sliding_window('ABCDEFG', 4) -> ABCD BCDE CDEF DEFG
    it = iter(iterable)
    window = collections.deque(islice(it, n), maxlen=n)
    if len(window) == n:
        yield tuple(window)
    for x in it:
        window.append(x)
        yield tuple(window)


def counter( data ):
    total = 0
    window = list(sliding_window(data, 3))
    for c, n in zip(window, window[1:]):
        total += sum(c) < sum(n)
    return total

def main():
    with open("input") as f:
        data = [int(i) for i in f.readlines()]
    #print(len(data))
    print( counter(data) )
    #print(list(sliding_window(data, 3)))

if __name__ == "__main__":
    main()

