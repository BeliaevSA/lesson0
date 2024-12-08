import time
from pprint import pprint

class Test:
    def __init__(self):
        self.name = 'name'
        self.age = 10

    def test(self):
        print('method')


    def test_2(self):
        print('method_2')


def introspection_info(obj):
    type_obj = type(obj).__name__
    attributes = [attr for attr in dir(obj) if not callable(getattr(obj, attr))]
    methods = [attr for attr in dir(obj) if callable(getattr(obj, attr))]
    module_obj = getattr(obj, '__module__', 'built-in')


    return {
        'type': type_obj,
        'attributes': attributes,
        'methods': methods,
        'module': module_obj
    }

test = Test()
pprint(introspection_info(15))
pprint(introspection_info(time))
pprint(introspection_info(test))