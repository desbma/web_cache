Web cache
=========

[![Latest Version](https://img.shields.io/pypi/v/web_cache.svg?style=flat)](https://pypi.python.org/pypi/web_cache/)
[![Tests Status](https://img.shields.io/travis/desbma/web_cache/master.svg?label=tests&style=flat)](https://travis-ci.org/desbma/web_cache)
[![Coverage](https://img.shields.io/coveralls/desbma/web_cache/master.svg?style=flat)](https://coveralls.io/github/desbma/web_cache?branch=master)
[![Supported Python versions](https://img.shields.io/pypi/pyversions/web_cache.svg?style=flat)](https://pypi.python.org/pypi/web_cache/)
[![License](https://img.shields.io/github/license/desbma/web_cache.svg?style=flat)](https://pypi.python.org/pypi/web_cache/)

Python module for simple key-value storage backed up by sqlite3 database.
The typical use case is a URL to HTTP data cache, but it can also be used fo non web ressources.


## Features

* Simple `dict` interface allows natural usage (`if key in cache`, `value = cache[key]`, etc.)
* Optional Zlib, BZIP2 or LZMA compression
* FIFO or LRU cache evicton strategies
* Optional thread safe interface to work around Python Sqlite3 'same thread' limitation
* Provides cache hit rate statistics


## Installation (from PyPI, with PIP)

web_cache requires [Python](https://www.python.org/downloads/) >= 3.3.

1. If you don't already have it, [install pip](http://www.pip-installer.org/en/latest/installing.html) for Python 3 (not needed if you are using Python >= 3.4)
2. Install web_cache: `pip3 install web_cache`


## License

[LGPLv2.1](https://www.gnu.org/licenses/old-licenses/lgpl-2.1.html)
