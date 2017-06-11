# python中如何引入外部python

import pythonOut

h=pythonOut.Hello()
h.hello()

from pythonOut import Hello

h1=Hello()
h1.hello()