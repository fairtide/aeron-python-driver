# Copyright 2018 Fairtide Pte. Ltd.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import re
from glob import iglob
from setuptools import setup


# Should be one of:
# 'Development Status :: 3 - Alpha'
# 'Development Status :: 4 - Beta'
# 'Development Status :: 5 - Production/Stable'
release_status = 'Development Status :: 3 - Alpha'
dependencies = [
    'Cython',
    'pyjnius==1.1.3',
]

here, _ = os.path.split(__file__)

aeron_all_jar = None
for filename in iglob(os.path.join(here, '**/aeron-all-*.jar'), recursive=True):
    aeron_all_jar = filename
    break

if not aeron_all_jar:
    raise RuntimeError('cannot file aeron jar file.')

aeron_all_jar_pattern = '^.*aeron-all-(\d+\.?\d+\.\d+)\.jar$'
version_match = re.match(aeron_all_jar_pattern, aeron_all_jar)
if not version_match:
    raise RuntimeError('cannot extract version number.')

aeron_all_jar = os.path.relpath(aeron_all_jar, here)
__version__ = version_match[1]

setup(
    name='aeron_python_driver',
    version=__version__,
    description='Python wrapper for Aeron MediaDriver',
    author='Fairtide Pte.',
    license='Apache 2.0',
    classifiers=[
        release_status,
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Operating System :: OS Independent',
        'Topic :: Aeron',
        'Topic :: Fairtide',
        'Topic :: Messaging',
    ],
    platforms='Posix; MacOS X; Windows',
    packages=['aeronpy.driver'],
    data_files=[aeron_all_jar],
    install_requires=dependencies,
    include_package_data=True,
    zip_safe=False,
)