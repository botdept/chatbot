#!/bin/env/python

import os

from subprocess import call


if __name__ == '__main__':
    dot_coverage_path = os.path.join(os.getcwd(), '.coverage')
    rc = call('coveralls')
    raise SystemExit(rc)
