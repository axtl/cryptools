# -*- coding: utf-8 -*-
import math
import string

from stringutils import convert, freq


def brute_xor(cyphertext, st_freqs):
    """Bruteforce a given single-character XOR-encrypted cyphertext.

    Statistical information is used to choose which character is the most
    likely key.

    :param cyphertext: the cyphertext to crack
    :param st_freqs: a Counter of standard frequencies in the target language
    :return: ``(key, message, score)``
    """
    # standard frequency counts
    st_keys = st_freqs.keys()
    st_len = len(st_keys)

    # store a map of each candidate and a simple frequency score
    topchoice = None
    lowdist = float('inf')
    key = None

    # bruteforce for each character
    for test in (string.letters + string.digits):
        dec = convert.xor(test, cyphertext)
        cand_freqs = freq.get_freqs(freq.char_count(dec.lower()))
        cand_keys = cand_freqs.keys()
        score = 0.0
        for c in cand_freqs:
            # scoring
            try:
                st_in = st_keys.index(c)
            except ValueError:
                st_in = st_len

            # find better scoring functions
            score += abs(cand_keys.index(c) - st_in)
            score += abs(st_freqs[c] - cand_freqs[c]) * 100

        if lowdist > score:
            lowdist = score
            topchoice = dec
            key = test

    return key, topchoice, lowdist
