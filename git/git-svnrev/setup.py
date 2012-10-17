from setuptools import setup

setup(
        name='git svnrev',
        version='1.0',
        long_description=__doc__,
        packages=[
                    'git_svnrev',
                ],
        install_requires=[
                    'GitPython',
                ],
        entry_points = {
            'console_scripts': [
                'git-svnrev = git_svnrev.main:main',
            ],
        },
)
