'''
Yet another collection of seemingly essential Python features and utilities for
building non-trivial applications

'''
VERSION = (0, 1, 0)


def get_version():
    return '.'.join(map(str, VERSION))

__version__ = get_version()
