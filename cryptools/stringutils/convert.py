"""This module contains a few utility function that work around Python's
formatting of various types.
"""
import math


def htoi(n):
    """Convert a hexit to its integer value."""
    return eval(bin(ord(n)))


def itoh(i):
    """Convert integer to hexit of the form \x00."""
    return '\\' + hex(i)[1:]


def htoc(h):
    """Convert hexit to character."""
    return h[-2:].decode('hex')


def xor(str1, str2):
    """XOR two strings together. The shorter string will be padded with itself
    in order to match the length of the longer one.
    """
    # sort by length
    in1, in2 = sorted([str1, str2], key=len)

    # see how much padding is needed, extend beyond and then trim
    r = int(math.ceil(len(in2) / float(len(in1))))
    in1 = (in1 * r)[:len(in2)]

    # xor each character pairs in the two strings
    return ''.join([chr(htoi(c1) ^ htoi(c2)) for (c1, c2) in zip(in1, in2)])


def xor_hex(buff1, buff2):
    """Return the hex-encoded value of XOR-ing two (hex-encoded) buffers"""
    return xor(buff1.decode('hex'), buff2.decode('hex')).encode('hex')
