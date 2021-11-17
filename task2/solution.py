def stupid_merge(*iterables):
    merged = []

    for i in iterables:
        merged.extend(i)

    merged.sort()

    for el in merged:
        yield el


def merge(*iterables):
    iterables = list(iterables)

    while True:
        if not iterables:
            return StopIteration

        res = []
        for i, iterable in enumerate(iterables):
            try:
                res.append(next(iterable))
            except StopIteration:
                del iterables[i]

        res.sort()

        for el in res:
            yield el


if __name__ == "__main__":

    def it1():
        for el in [1, 5, 9, 100]:
            yield el


    def it2():
        for el in [200, 500]:
            yield el


    def it3():
        for el in [1, 6, 10, 11, 20]:
            yield el


    i1 = it1()
    i2 = it2()
    i3 = it3()

    for el in stupid_merge(i1, i2, i3):
        print(el, end=" ")
