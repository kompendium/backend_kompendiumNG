#############################################################################################
#
# Enum.py
#
# Basic implementation for all enumerations.
#
# Author: C. Igel
#
# Date: 2012/04/20 / 20:21 CEST
#
# License: Apache License 2.0
#
#############################################################################################

################################################################################
## inspired by an implementation from
## http://stackoverflow.com/questions/36932/whats-the-best-way-to-implement-an-enum-in-python
################################################################################

import __Constant

def makeenum(**enums):
    return type('Enum', (), enums)

class EnumBase (object):

    self.__Constants = __Constant()

    def __init__(self, values):
        self.__Constants.EnumValues = makeenum(values)
        setattr(self, "EnumValues", self.__Constants.EnumValues)
        for number, name in enumerate(values):
            self.__Constants.__setattr__(name, number)
            setattr(self, name, number)