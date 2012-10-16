"""
The Git date script entry point.
"""

import os
import sys

from datetime import datetime, timedelta
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

    return datetime.fromtimestamp(time.mktime(time.struct_time(result)))

def main():

    try:
        repo = Repo()

        parser = ArgumentParser(prog='git date')

        parser.add_argument('since', type=repo.commit, default='HEAD', nargs='?', help='The commit to start at.')
        parser.add_argument('until', type=repo.commit, default='HEAD', nargs='?', help='The commit to stop at.')
        parser.add_argument('fromdate', metavar='from', type=parse_date, help='The date to start at.')
        parser.add_argument('todate', metavar='to', type=parse_date, default=None, nargs='?', help='The date to stop at.')
        parser.add_argument('-j', '--jitter', action='store_true', help='If set, will add some random jitter to the commit dates.')

        args = parser.parse_args()

        if (args.since != args.until) and not args.since in args.until.iter_parents():
            sys.stderr.write('%s..%s is not a valid commit range.\n' % (args.since.hexsha, args.until.hexsha))

            return -3

        commits = [args.until]

        while commits[-1] != args.since:
            commits.append(commits[-1].parents[0])

        if (len(commits) > 1) and args.todate:
            step = (args.todate - args.fromdate) / (len(commits) - 1)

        else:
            step = timedelta()

        start_date = args.fromdate

        for commit in commits:
            env_filter = '''
            '
            if [ $GIT_COMMIT = %(sha)s ]
            then
                export GIT_AUTHOR_DATE="%(date)s"
                export GIT_COMMITTER_DATE="%(date)s"
            fi
            '
            ''' % {
                'sha': commit.hexsha,
                'date': start_date.ctime(),
            }

            repo.git.filter_branch(
                '--env-filter',
                env_filter
            )

            start_date = start_date + step

    except InvalidGitRepositoryError, ex:
        sys.stderr.write('%s is not a valid git repository.\n' % ex.message)

        return -1

    except BadObject, ex:
        sys.stderr.write('%s is not a valid commit identifier.\n' % ex.message)

        return -2
