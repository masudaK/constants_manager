#!/usr/bin/env python
from constants_manager import constants_manager

consts = constants_manager.ConstantsManager()
print(consts.get('val_only_dev'))
