import Firstmd as k
k.greeting('python')
#k.add(6,7)
#k.mult(5,3)
#import specific function from other module
from Firstmd import add , sub
add(4,6)
sub(4,7)

from Firstmd import add as a, sub as b
a(5,3)
b(6,7)

from Firstmd import *
add(3,4)
divi(5,4)

#import all fucntion from other modules

print(dir(k))
