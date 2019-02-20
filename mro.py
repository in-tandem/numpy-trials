class A:

    def __init__(self):
        pass

    def printing(self):
        print('im inside class A ')

class A1(A):
    pass
    # def printing(self):
    #     print('im inside class A1 ')

class B(object):

    def print(self):
        print('im inside class B ')

class B1(B):

    def print(self):
        print('im inside class b1 ')

class C(A1,B1):
    def print(self):
        print('im inside class c')
        super().printing()

    @staticmethod
    def statictrial():
        pass


c = C()
c.printing()
c.statictrial()
print(C.__mro__)

import functools

def my_decorator_lalalalalala(surname):

    def outer(func):
        
        @functools.wraps(func)
        def func_wrapper(*args,**kwargs):
            
            print('im inside func wraper with surname:', surname)

            return func(kwargs.get('name'))

        return func_wrapper

    return outer


@my_decorator_lalalalalala(surname='blaaa')
def get_text(name):
    
    print('im inside get tezt:',name)
    return name 

print(get_text(name='somak'))


class TryingProperty:

    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        print('i may want to reformat or recalculate before sending you')
        return self._name

    @name.setter
    def name(self, value):
        print('inside setter method of name. i may want to recalculate or refomrmat before setting')
        self._name = value

prop = TryingProperty('somaktryingproperty')
print(prop.name)
prop.name = 'somaknowtrynigtosetproperty'