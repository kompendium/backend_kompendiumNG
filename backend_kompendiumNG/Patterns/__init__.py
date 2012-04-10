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

import os

__all__ = []

for dir_content in os.listdir(os.path.dirname(__file__)):
    if os.path.isfile(dir_content):
        file = str(dir_content)
        if not file.endswith('.py'):
            continue
        python_filename = file[0:-3]
        __all__.append(python_filename)
        module = __import__(python_filename)
        reload(module)
    if os.path.isdir(dir_content):
        __all__.append(dir_content)
