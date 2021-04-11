# A Python client for Upgrade.Chat's API
[![PyPi](https://static.pepy.tech/personalized-badge/upgradeChat?period=total&units=international_system&left_color=grey&right_color=green&left_text=Downloads)](https://pypi.org/project/upgradeChat)
[![License](https://img.shields.io/pypi/l/upgradeChat?color=orange&style=flat-square)](https://github.com/nwithan8/upgradeChat/blob/master/LICENSE)

[![Open Issues](https://img.shields.io/github/issues-raw/nwithan8/upgradeChat?color=gold&style=flat-square)](https://github.com/nwithan8/upgradeChat/issues?q=is%3Aopen+is%3Aissue)
[![Closed Issues](https://img.shields.io/github/issues-closed-raw/nwithan8/upgradeChat?color=black&style=flat-square)](https://github.com/nwithan8/upgradeChat/issues?q=is%3Aissue+is%3Aclosed)
[![Latest Release](https://img.shields.io/github/v/release/nwithan8/upgradeChat?color=red&label=latest%20release&logo=github&style=flat-square)](https://github.com/nwithan8/upgradeChat/releases)

[![Discord](https://img.shields.io/discord/472537215457689601?color=blue&logo=discord&style=flat-square)](https://discord.gg/7jGbCJQ)
[![Twitter](https://img.shields.io/twitter/follow/nwithan8?label=%40nwithan8&logo=twitter&style=flat-square)](https://twitter.com/nwithan8)

Interact with Upgrade.Chat's API in Python

# Installation
From PyPi: ``python -m pip install upgradechat``

From GitHub ``python -m pip install git+https://github.com/nwithan8/upgradechat.git``

# Usage
Can retrieve data from Upgrade.Chat's API as raw JSON or pydantic objects

Import the ``upgradeChat`` package to initialize the API
Example:
```python
from upgradeChat import API

api = API(client_id="myclientid", client_secret="myclientsecret", raw=True)
```

Set ``raw=True`` to return JSON data, ``raw=False`` to return objects.

# Documentation

Documentation available on [ReadTheDocs](https://upgradeChat.readthedocs.io/en/latest/documentation.html)