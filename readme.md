# cd

### To run this script follow as below:

## Usage


#### To run testcases
```bash
# python cd.py test
```
#### output:
```bash
Testcase: cd / abc      --> /abc
Testcase: cd /abc/def ghi       --> /abc/def/ghi
Testcase: cd /abc/def ..        --> /abc
Testcase: cd /abc/def /abc      --> /abc
Testcase: cd /abc/def /abc/klm  --> /abc/klm
Testcase: cd /abc/def ../..     --> /
Testcase: cd /abc/def ../../..  --> /
Testcase: cd /abc/def .         --> /abc/def
Testcase: cd /abc/def ..klm     --> ..klm: No such file or directory
Testcase: cd /abc/def //////    --> /
Testcase: cd /abc/def ......    --> ......: No such file or directory
Testcase: cd /abc/def ../gh///../klm/.  --> /abc/klm
```

#### To run cd with path and newPath
```bash
# python cd.py /abc/def /abc
/abc

# python cd.py /abc/def ..klm
..klm: No such file or directory
```
