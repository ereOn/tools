"""
The Git svnrev script entry point.
"""

import os
import sys
import re

from argparse import ArgumentParser

from git import *
from git.exc import InvalidGitRepositoryError
from gitdb.exc import BadObject

def command_get(args):

    repo = Repo()

    commits = repo.iter_commits()

    def extract_revision(s):
        """
        Extract a svn revision for a commit message.
        """

        match = re.search(r'^git-svn-id: [^@]*@(\d+) .*$', s, re.MULTILINE)

        if match:
            return int(match.group(1))

    result = None

    if args.strict:

        for commit in commits:

            revision = extract_revision(commit.message)

            if not (revision is None) and (revision == args.revision):

                result = {
                    'commit': commit,
                    'revision': revision,
                }

                break

    else:

        for commit in commits:

            revision = extract_revision(commit.message)

            if not (revision is None) and (revision <= args.revision):

                result = {
                    'commit': commit,
                    'revision': revision,
                }

                break

    if result:
        if args.verbose and (result['revision'] != args.revision):
            sys.stderr.write('No exact match was found. Showing result for revision %s.\n' % result['revision'])

        sys.stdout.write('%s\n' % result['commit'].hexsha)

    else:
        sys.stderr.write('Revision %s does not exist in the current branch.\n' % args.revision)

    if result:
        return 0
    else:
        return 100

def main():

    # Create an argument parser
    parser = ArgumentParser(prog='git svnrev')

    command_parser = parser.add_subparsers()

    # The get parser
    get_parser = command_parser.add_parser('get', help='Get a commit id from a svn revision number.')
    get_parser.add_argument('revision', type=int, help='The svn revision number.')
    get_parser.add_argument('-s', '--strict', action='store_true', help='Enables strict mode where the exact svn revision number must exist in the current branch.')
    get_parser.add_argument('-v', '--verbose', action='store_true', help='Enables verbose mode.')
    get_parser.set_defaults(func=command_get)

    # Parse the arguments
    args = parser.parse_args()

    try:
        return args.func(args)

    except InvalidGitRepositoryError, ex:
        sys.stderr.write('%s is not a valid git repository.\n' % ex.message)

        return 1

    except BadObject, ex:
        sys.stderr.write('%s is not a valid commit identifier.\n' % ex.message)

        return 2

    except Exception, ex:
        sys.stderr.write('Error: %s\n' % ex.message)
