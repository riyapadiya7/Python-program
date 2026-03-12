import file

print(file.add(5,3))

from file import sub
print(sub(10,4))

from file import *
print(mul(2,3))

import file as m
print(m.div(8,2))
