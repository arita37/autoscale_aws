"""A setup module for autoscaleaws."""


# setuptools for distribution
from setuptools import find_packages, setup
import os


with open('requirements.txt') as f:
    required = f.read().splitlines()


LONG_DESCRIPTION = """
 Autoscale AWS allows to scale up virtual machines by invoking spot requests as per
 start and stop rules.
"""

# from m2r import convert
# rst = convert('# Title\n\nSentence.')


with open("readme.md", mode="r", encoding='utf-8') as f :
   md = " ".join(f.readlines())
   LONG_DESCRIPTION = md
   # convert(md)

packages = find_packages(where="src", exclude=[])


entry_points = {
 'console_scripts': [  'aws_run=autoscale_aws.cli:run_cli'


  ]
}

setup(
    name                          = 'autoscaleaws',
    version                       = '11.0.2',
    description                   = 'Auto scale AWS by spot instances to launch tasks',
    long_description              = LONG_DESCRIPTION,
    long_description_content_type = 'text/markdown',
    license                       = "BSD",
    url                           = 'https://github.com/arita37/cli_code/tree/dev',
    author                        = 'arita37, Kevin Noel (Nono)',
    classifiers                   = [
        "Development Status :: 3 - Alpha",
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Software Development :: Libraries :: Python Modules',
        "License :: OSI Approved :: BSD License",
    ],
    packages                      = packages,
    package_dir                   = {'': 'src'},
    install_requires              = required,
    python_requires               = '>=3.6',
    entry_points                  = entry_points
)

