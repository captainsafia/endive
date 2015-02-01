try:
    from setuptools import setuo
except ImportError:
    from distutils.core import setup

from endive import __version__
dependencies = []

setup(
    name = "Endive",
    version = ".".join(str(x) for x in __version__),
    description = "Rare event prediction library for Python",
    url = "http://www.github.com/zafia/endive",
    license = "MIT License",
    author_email = "safia@safia.rocks",
    install_require = dependecies,
    packages = ["endive"]
)
