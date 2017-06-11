# python 中的面向对象 带参数类的定义 类的继承

class Hello:

    def __init__(self,name):
        self._name=name

    def Hello(self):
        print ("Hello {0}".format(self._name))

class Hi(Hello):

    def __init__(self,name):
        Hello.__init__(self,name)

    def Hi(self):
        print("Hi {0}".format(self._name))

h=Hello("Challenger")
h.Hello()
h1=Hi("CY")
h1.Hi()