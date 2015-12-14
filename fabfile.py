from __future__ import print_function, unicode_literals, absolute_import

from fabric.api import local


def test(verbose=False):
    verb = '-v' if verbose else ''
    local('python -m unittest discover -s tests'.format(verb))
