from distutils.core import setup

import sys

if sys.version_info < (3, 6):
    sys.exit("Python 3.6+ is required.")

setup(
    name="timethese",
    version="0.0.1",
    python_requires=">=3.6",
    install_requires=[],
    license="Do What The F*ck You Want To Public License",
    long_description=open("README.md").read(),
)
