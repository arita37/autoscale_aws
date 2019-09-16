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



setup(
    name='autoscaleaws',
    version='11.0.2',
    description='Auto scale AWS by spot instances to launch tasks',
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    license = "BSD",
    # The project's main homepage.
    url='https://github.com/arita37/cli_code/tree/dev',
    # Author(s) details
    author='arita37, Kevin Noel (Nono)',
    classifiers=[
        "Development Status :: 3 - Alpha",
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Software Development :: Libraries :: Python Modules',
        "License :: OSI Approved :: BSD License",
    ],
    packages=find_packages(where="src", exclude=[]),
    package_dir={'': 'src'},
    install_requires=required,
    python_requires='>=3.5',
    entry_points={
        'console_scripts': [
            'autoscale = autoscale_aws.batch_daemon_autoscale_cli:autoscale_main'
        ]
    }
)

