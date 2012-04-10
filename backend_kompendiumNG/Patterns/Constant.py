#############################################################################################
#
# __init__.py
#
# Basic implementation for package listing.
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
## http://code.activestate.com/recipes/65207-constants-in-python/?in=user-97991
################################################################################

import Singleton

class __Constant(object):

    def __setattr__(self, name, value):
        if self.__dict__.has_key(name):
            raise self.ConstError, "Can't rebind constant value (%s)"  % name
        self.__dict__[name] = value

    class ConstError(TypeError):
        pass


import sys

##

sys.modules[__name__] = __Constant()
