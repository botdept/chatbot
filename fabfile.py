from __future__ import print_function, unicode_literals, absolute_import

from fabric.api import local


def test(verbose=False, args=''):
    verb = '-v' if verbose else ''
    local('python -m unittest {} tests {}'.format(verb, args))
