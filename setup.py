#!/usr/bin/env python3

import os
import re
import sys

from setuptools import find_packages, setup


if sys.hexversion < 0x3040000:
  print("Python version %s is unsupported, >= 3.4.0 is needed" % (".".join(map(str, sys.version_info[:3]))))
  exit(1)

with open(os.path.join("web_cache", "__init__.py"), "rt") as f:
  version = re.search("__version__ = \"([^\"]+)\"", f.read()).group(1)

with open("README.md", "rt") as f:
  readme = f.read()

setup(name="web_cache",
      version=version,
      author="desbma",
      packages=find_packages(exclude=("tests",)),
      test_suite="tests",
      description="Simple persistent cache storage, with different cache eviction strategies, and optional compression",
      long_description=readme,
      long_description_content_type="text/markdown",
      url="https://github.com/desbma/web_cache",
      download_url="https://github.com/desbma/web_cache/archive/%s.tar.gz" % (version),
      keywords=["cache", "sqlite3", "key-value", "persistent"],
      classifiers=["Development Status :: 5 - Production/Stable",
                   "Intended Audience :: Developers",
                   "License :: OSI Approved :: GNU Lesser General Public License v2 or later (LGPLv2+)",
                   "Operating System :: OS Independent",
                   "Programming Language :: Python",
                   "Programming Language :: Python :: 3",
                   "Programming Language :: Python :: 3 :: Only",
                   "Programming Language :: Python :: 3.4",
                   "Programming Language :: Python :: 3.5",
                   "Programming Language :: Python :: 3.6",
                   "Programming Language :: Python :: 3.7",
                   "Programming Language :: Python :: 3.8",
                   "Topic :: Database",
                   "Topic :: Software Development :: Libraries :: Python Modules"])
