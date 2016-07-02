import sys
from distutils.core import setup

setup(name='Job',
      version='0.1.1',
      packages = ['job'],
      entry_points='''
        [console_scripts]
        jobpy=job.jobcmd:main
      ''',

      )
