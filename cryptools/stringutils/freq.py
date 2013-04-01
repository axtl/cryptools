# -*- coding: utf-8 -*-
import string
from collections import defaultdict, Counter


def char_count(text):
    """Counts occurrences of each character in the input.

    The count is case-sensitive and only takes into account letters,
    digits, and whitespace.

    >>> char_count("to be or not to be.")
    Counter({' ': 5, 'o': 4, 't': 3, 'b': 2, 'e': 2, 'n': 1, 'r': 1, '.': 1})

    :param text: the text to analyze
    :return: a ``collections.Counter`` with the counts for each character
    """
    freqs = Counter()
    freqs.update(text)
    # trim to useful characters
    for ch in freqs.keys():
        if ch not in (string.letters + string.digits + string.whitespace):
            freqs.pop(ch)
    return freqs


# total numbers
def get_freqs(counter):
    """Computes the relative frequencies for elements in the provided counter.

    >>> get_freqs(Counter('test'))
    defaultdict(<type 'int'>, {'s': 0.25, 'e': 0.25, 't': 0.5})

    :param counter: the input counter to compute frequencies for
    :return: a ``collections.defaultdict`` with the appropriate frequencies
    """
    elems = float(sum(counter.values()))
    nfreqs = defaultdict(int)
    for el in counter:
        nfreqs[el] = counter[el] / elems
    return nfreqs
