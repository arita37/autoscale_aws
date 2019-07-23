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

setup(
    name='autoscaleaws',
    version='0.0.1',
    description='Auto scale AWS by spot instances.",
    long_description=LONG_DESCRIPTION,
    license = "BSD",
    # The project's main homepage.
    url='https://github.com/ajeybk/autoscaleaws',
    # Author(s) details
    author='Yaki Noe/Ajey Khanapuri',
    author_email='kbajey@gmail.com',
    classifiers=[
        "Development Status :: 3 - Alpha",
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Software Development :: Libraries :: Python Modules',
        "License :: OSI Approved :: BSD License",
    ],
    packages=find_packages(where="src", exclude=[]),
    package_dir={'': 'src'},
    install_requires=required,
    python_requires='>=3.0',
    entry_points={
        'console_scripts': [
            'autoscale = autoscale.batch_daemon_autoscale_cli:autoscale_main'
        ]
    }
)

