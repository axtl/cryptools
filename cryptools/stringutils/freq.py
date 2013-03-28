# -*- coding: utf-8 -*-
import string
from collections import defaultdict, Counter


def char_count(text):
    freqs = Counter()
    freqs.update(text)
    # trim to useful characters
    for ch in freqs.keys():
        if ch not in (string.letters + string.digits + string.whitespace):
            freqs.pop(ch)
    return freqs


# total numbers
def get_freqs(counter):
    elems = float(sum(counter.values()))
    nfreqs = defaultdict(int)
    for el in counter:
        nfreqs[el] = counter[el] / elems
    return nfreqs
