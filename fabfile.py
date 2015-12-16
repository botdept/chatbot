from __future__ import print_function, unicode_literals, absolute_import

from fabric.api import local


def test():
    local('coverage run -m unittest discover -s tests')
