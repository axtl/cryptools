# -*- coding: utf-8 -*-
"""This module contains a few conversion utility functions for that work
around Python's formatting and representation of various data types.
"""
import math


def htoi(h):
    """Convert a hexit to its integer value.

    >>> htoi('\\x74')
    116

    :param h: hexit to convert
    :return: integer value representation
    """
    return eval(bin(ord(h)))


def htoc(h):
    """Convert hexit to character.

    This function does not check if the character is printable or not.

    >>> htoc('\\\\x74')
    't'

    :param h: hexit to convert
    :return: character representation of the hexit
    """
    return h[-2:].decode('hex')


def itoh(i):
    """Convert integer to hexit of the form ``\\x00``.


    Normally, Python's built-in :func:`hex` function will return ``0x00``, even
    though that wouldn't work if we were directly trying to hex decode it.

    >>> itoh(116)
    '\\\\x74'

    :param i: integer value to convert
    :return: hexit of the form ``\\x00``
    """
    return '\\' + hex(i)[1:]


def xor(str1, str2):
    """XOR two strings.


    If the strings are not equal, the shorter one will be padded with itself,
    repeating, to match the length of the longer one.

    >>> xor('HAL', 'IBM')
    '\\x01\\x03\\x01'
    >>> xor('foo', 'foobar')
    '\\x00\\x00\\x00\\x04\\x0e\\x1d'

    :param str1: first string to use as input
    :param str2: second string to use as input
    :return: a string resulting from XOR-ing the two input parameters
    """
    # sort by length
    in1, in2 = sorted([str1, str2], key=len)

    # see how much padding is needed, extend beyond and then trim
    r = int(math.ceil(len(in2) / float(len(in1))))
    in1 = (in1 * r)[:len(in2)]

    # xor each character pairs in the two strings
    return ''.join([chr(htoi(c1) ^ htoi(c2)) for (c1, c2) in zip(in1, in2)])


def xor_hex(buff1, buff2):
    """Return the hex-encoded value of XOR-ing two (hex-encoded) buffers.

    The buffers are hex-decoded, passed to :func:`xor`, and the result is
    hex-encoded before being returned.

    >>> h1 = "686974207468652062756c6c277320657965"
    >>> h2 = "746865206b696420646f6e277420706c6179"
    >>> xor_hex(h1, h2)
    '1c0111001f010100061a024b53535009181c'

    :param buff1: first hex-encoded buffer
    :param buff2: second hex-encoded buffer
    :return: a hex-encoded string resulting from XOR-ing the two buffers
    """
    return xor(buff1.decode('hex'), buff2.decode('hex')).encode('hex')
