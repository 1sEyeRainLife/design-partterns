# -*- coding:utf-8 -*-
import functools

known = {0:0, 1:1}
known_sum = {0: 0}


def memoize(fn):
    known = dict()

    @functools.wraps(fn)
    def memoizer(*args):
        if args not in known:
            known[args] = fn(*args)
        return known[args]
    return memoizer


@memoize
def fib(n):
    assert (n >= 0), 'n must be >= 0'
    return n if n in (0, 1) else fib(n - 1) + fib(n - 2)
    # if n in known:
    #     return known[n]
    # res = fib(n-1) + fib(n-2)
    # known[n] = res
    # return res


@memoize
def nsum(n):
    assert(n >= 0), 'n must be >= 0'
    return 0 if n == 0 else n + nsum(n-1)
    # if n in known_sum:
    #     return known_sum[n]
    # res = n + nsum(n-1)
    # known_sum[n] = res
    # return res

if __name__ == '__main__':
    from timeit import Timer
    t = Timer('fib(8)', 'from __main__ import fib')
    print t.timeit()

