#!/usr/bin/python3
"""MODULE 0"""


class LockedClass:
    """__slots helps to restrcit assignments to Objects\
by disabling __dict__. only things seclared in slots are usable"""
    __slots__ = "first_name"
