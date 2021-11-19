def stupid_merge(*iterables):
    """Simple and ineffective realization."""
    merged = []

    for i in iterables:
        merged.extend(i)

    merged.sort()

    for el in merged:
        yield el


def my_merge(*iterables):
    """Works only with iterators because of next()."""
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


def generate_iterables(*lists):
    """Creating list of iterators for tests."""
    prepared1, prepared2 = [], []

    for list in lists:
        def _it():
            for el in list:
                yield el

        prepared1.append(_it())
        prepared2.append(_it())

    return prepared1, prepared2