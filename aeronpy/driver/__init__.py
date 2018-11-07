import os
import sys
import subprocess

__version__ = '1.11.2'

if 'JAVA_HOME' not in os.environ:
    if sys.platform == 'darwin':
        java_home = subprocess.check_output(['/usr/libexec/java_home'])
        if java_home:
            java_home = java_home.decode('ascii').rstrip()
            os.environ.setdefault('JAVA_HOME', java_home)
        else:
            raise RuntimeError(f'/usr/libexec/java_home failed with - {java_home}')
    elif sys.platform == 'linux':
        java_home = subprocess.check_output([
            'jrunscript',
            '-e',
            'java.lang.System.out.println(java.lang.System.getProperty(\'java.home\'));'])
        if java_home:
            java_home = java_home.decode('ascii').rstrip()
            os.environ.setdefault('JAVA_HOME', java_home)
        else:
            raise RuntimeError(f'jrunscript failed with - {java_home}')

    else:
        raise NotImplemented('Not supported on this platform')

import jnius_config

here, _= os.path.split(__file__)
aeron_all_jar = os.path.join(here, f'aeron-all-{__version__}.jar')

jnius_config.set_classpath(aeron_all_jar)
import jnius



