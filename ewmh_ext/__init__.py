#!/usr/bin/env python3

from ewmh import *

def getWmName(self, win):
    """
    Get the property _NET_WM_NAME for the given window as a string.

    :param win: the window object
    :return: str
    """
    return self._getProperty('_NET_WM_NAME', win).decode()

EWMH.getWmName = getWmName

