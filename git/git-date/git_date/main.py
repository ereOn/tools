"""
The Git date script entry point.
"""

import os
import sys

import datetime
import time

from argparse import ArgumentParser

from git import *
from git.exc import InvalidGitRepositoryError
from gitdb.exc import BadObject

from parsedatetime.parsedatetime import Calendar

def parse_date(s):
    """
    Parse a human date and gives a datetime object.
    """

    cal = Calendar()

    result, what = cal.parse(s)

    if not what:
        raise ValueError('%s is not a valid date/time value.' % s)

    return datetime.datetime.fromtimestamp(time.mktime(time.struct_time(result)))

def main():

    try:
        repo = Repo()

        parser = ArgumentParser()

        parser.add_argument('since', type=repo.commit, help='The commit to start at.')
        parser.add_argument('until', type=repo.commit, help='The commit to stop at.')
        parser.add_argument('from', type=parse_date, help='The date to start at.')
        parser.add_argument('to', type=parse_date, help='The date to stop at.')
        parser.add_argument('-j', '--jitter', action='store_true', help='If set, will add some random jitter to the commit dates.')

        args = parser.parse_args()

        print args

    except InvalidGitRepositoryError, ex:
        sys.stderr.write('%s is not a valid git repository.\n' % ex.message)

        return -1

    except BadObject, ex:
        sys.stderr.write('%s is not a valid commit identifier.\n' % ex.message)

        return -2
