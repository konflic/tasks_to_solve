#!/usr/bin/python3
from os import path, getcwd
import subprocess


def parse_results(results):
    """Parsing raw string output"""
    res = []
    for line in results.strip().split("\n"):
        if "=" in line:
            dices, score = line.split("=")
            dices = tuple(dices.strip().split(" "))
            res.append((dices, score.strip()))
    return res


def count_scores(throw_result):
    """Verification of counting scores."""
    throw_result = [int(el) for el in throw_result]

    if sorted(throw_result) == [1, 2, 3, 4, 5]:
        return 150
    else:
        return throw_result.count(1) * 10 + throw_result.count(5) * 5


def _my_cool_soft(path_to_soft):
    """Wrap around binary files to run tests against."""
    full_path = f"{path_to_soft}"

    def wrapper(throws, min_d, max_d):
        try:
            res = subprocess.check_output([full_path, str(throws), str(min_d), str(max_d)])
            raw_results = res.decode("utf-8")
            return parse_results(raw_results)
        except subprocess.CalledProcessError:
            return "Error"

    return wrapper
