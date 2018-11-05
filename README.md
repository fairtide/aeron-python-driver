[![image](https://img.shields.io/pypi/v/aeron-python-driver.svg)](https://pypi.org/project/aeron-python-driver/)
[![image](https://img.shields.io/pypi/l/aeron-python-driver.svg)](https://pypi.org/project/aeron-python-driver/)

### Introduction

This repository provides unofficial Python wrapper for [Aeron Media Driver](https://github.com/real-logic/aeron) simplifying process of integration of media driver into python.

### Usage

For installation with pip:
```
$ python3.6 -m pip install aeron-python-driver
```

To manage Aeron media driver through Python resource manager:
```
from aeronpy.driver import media_driver

[...]

with media_driver.launch(aeron_directory_name=custom_aeron_dir):
    ...
    # interact with Aeron here       
```

### Troubleshooting

* **`You need Cython to compile Pyjnius.`**

    Sometimes pip fails to resolve and install Cython as a dependency, in such case the above message will be displayed as an error during installation. To fix it install cython with pip:
    ```
    $ pip install Cython
    ```
    and retry pip installation.
    
    Project has been tested against Cython 0.29. 
    
* **Java not found**
    
    This project heavily depends on Java. Java 1.8 or newer should be installed in the system and ideally **JAVA_HOME** should point to JDK home. On OS X and Linux library will attempt to locate java even if **JAVA_HOME** is not set. If java is not present in the system, install Oracle HotSpot JDK and setup **JAVA_HOME** for your installation.     
        

### License

Copyright 2018 Fairtide Pte. Ltd.

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.


