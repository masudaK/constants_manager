[![Build Status](https://travis-ci.org/masudaK/constants_manager.svg)](https://travis-ci.org/masudaK/constants_manager)


# constants manager
This library is for management of constants.
This helps you to create an application which have the environments like dev, stg, prd.


## Installation
```
$ pip install constants_manager
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
!#/usr/bin/env python
from constants_manager import constants_manager

consts = constants_manager.ConstantsManager()
print(consts.get('val_only_default'))
```

if you want to use some constants which differed under environments, set the environments variables like this.

```
ENV=dev python sample.py
```

So you can access the value of "dev" section for using the environments variables.

If you do not set any environments variables, you can access the default value.
So if you used those "constatns.ini" and use "flag" constant, it returns "False", not return 'True'.


## Misc
There is the similar library which called "[constants](https://pypi.python.org/pypi/constants)".
The differences is that "constants_manager" is case-sensitivity. It distinguish on case of key.


## Contribute
- Issue
- Fork and pull requests. 
- automatic test execution
- if you had some trouble, contact @masudaK


## Contributor
- [Satoshi SUZUKI](https://github.com/studio3104)


## Test Flow
- run nosetests to the test file
- various version tests with using tox
- CI with travis

## License
MIT


[![Bitdeli Badge](https://d2weczhvl823v0.cloudfront.net/masudaK/constants_manager/trend.png)](https://bitdeli.com/free "Bitdeli Badge")

