from __future__ import print_function
from distutils import sysconfig
from os import path

prefix = sysconfig.get_config_var('PYTHONFRAMEWORKPREFIX')
ldlibrary = sysconfig.get_config_var('LDLIBRARY')
print(path.join(prefix,ldlibrary))
