#!/bin/env/python

import os

from subprocess import call


if __name__ == '__main__':
    dot_coverage_path = os.path.join(os.getcwd(), '.coverage')
    if os.path.isfile(dot_coverage_path):
        os.remove('.coverage')

    # create a report from the coverage data
    if 'TRAVIS' in os.environ:
        rc = call('coveralls')
        raise SystemExit(rc)
    else:
        rc = call(['coverage', 'report'])
        raise SystemExit(rc)