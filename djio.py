#!usr/bin/env python3
# coding: utf-8
"""This module contains functions of input and output utilities."""

import codecs


def read_file(path, char_set='utf-8'):
    """The basic function of reading files.

    :param path: the path of the file to read.
    :param char_set: the character set of the file, default 'utf-8'.
    :return: returns all lines as a list.
    """
    with codecs.open(path, 'r+', encoding=char_set) as f:
        return f.readlines()


def yield_file(path, char_set='utf-8'):
    """ The function to read large files.

    :param path: the path of the file to read.
    :param char_set: the character set of the file, default 'utf-8'.
    :return: returns a generator of the file.
    """
    with codecs.open(path, 'r+', encoding=char_set) as f:
        for line in f.readlines():
            yield line


def write_file(to_write, path, mode='append', char_set='utf-8'):
    """The function to write in a file.

    :param to_write: string or a list of string to be write.
    :param path: the file to write in.
    :param mode: write mode, can be 'append' or 'overwrite', default 'append'.
    :param char_set: the character set of the string, default 'utf-8'.
    """
    if mode == 'append':
        write_mode = 'a+'
    elif mode == 'overwrite':
        write_mode = 'w+'
    else:
        raise ValueError('Invalid write mode `%s`, only `append` and `overwrite` are acceptable.' % mode)
    with codecs.open(path, write_mode, encoding=char_set) as f:
        if isinstance(to_write, str):
            f.write(to_write + '\n')
        elif isinstance(to_write, list):
            for line in to_write:
                f.write(line + '\n')
        else:
            raise ValueError('Cannot write object of type `%s`.' % type(to_write))
