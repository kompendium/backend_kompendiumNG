#############################################################################################
#
# __init__.py
#
# Basic implementation for Event systems.
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
## http://www.voidspace.org.uk/python/weblog/arch_d7_2007_02_03.shtml#e616
################################################################################


class EventHook(object):

    def __init__(self):
        self.__handlers = [self.___handlerStub]

    def __iadd__(self, handler):
        if self.__handlers.count(handler):
            return self
        self.__handlers.append(handler)
        return self

    def __isub__(self, handler):
        if self.__handlers.count(handler):
            self.__handlers.remove(handler)
        return self

    def __call__(self, src, args):
        for handler in self.__handlers:
            handler(src, args)


