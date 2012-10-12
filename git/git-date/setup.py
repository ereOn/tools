from setuptools import setup

setup(
        name='Git date',
        version='1.0',
        long_description=__doc__,
        packages=[
                    'git_date',
                ],
        install_requires=[
                ],
        entry_points = {
            'console_scripts': [
                'git-date = git_date.main:main',
            ],
        },
)
