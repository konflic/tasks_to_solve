import re


def time_converter(s: str) -> int:
    pattern = re.compile(r"^([0-9]*[.]?[0-9]+[smdh]){1}$")

    values = {
        "s": 1,
        "m": 60,
        "h": 60 * 60,
        "d": 60 * 60 * 24
    }

    if not len(s):
        raise ValueError

    try:
        return int(s)
    except ValueError:
        if s.isalpha() and len(s) == 1 and s in values.keys():
            return values[s]
        else:
            if re.match(pattern=pattern, string=s):
                return float(s[:-1]) * values[s[-1]]

    raise ValueError
