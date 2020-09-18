# pyfs-application

Feishu Application Module for Python.

# Installation

```shell
pip install pyfs-application
```

# Usage

```python
from pyfs_application import Application, is_user_admin
```

# Method

```python
class MarketCode(BaseToken):
    def __init__(self, appid=None, secret=None, token=None, storage=None):
        super(MarketCode, self).__init__(appid=appid, secret=secret, token=token, storage=storage)

    def is_user_admin(self, open_id=None, employee_id=None, appid=None, secret=None, ticket=None, token=None, storage=None):
```
