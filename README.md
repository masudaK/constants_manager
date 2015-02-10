# constants manager
This library is for management of constants.
This helps you to create an application which have the environments like dev, stg, prd.


## Installation
```
$pip install constants_manager
```

## Usage
Setup "constants.ini".

```
[DEFAULT]
flag = False
val_only_default = val_only_default

[dev]
flag = True
val_only_dev = val_only_dev

```

you write a code like below.



```
!/usr/bin/env python
from constants_manager import constants_manager

consts = constants_manager.ConstantsManager()
print(consts.get('val_only_default'))
```

if you want to use some constants which differed under environments, set the environments values like this.

```
ENV=dev python sample.py
```

So you can access the value of "dev" section for using the environments value.

If you do not set any environments value, you can access the default value.
So if you used those "constatns.ini" and use "flag" constant, it returns "False", not return 'True'.


## Misc
There is the similar library which called "[constants](https://pypi.python.org/pypi/constants)".
The differences is that using default key if you set the constants not existed, this means that "constants" raises error, but "constants manager" do not raise error. It returns default value.



## Contribute
- Issue
- Fork and pull requests. 
- contact @masudaK

