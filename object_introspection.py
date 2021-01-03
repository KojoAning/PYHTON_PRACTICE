from setters_and_property_decoretors import Youtuer
myth_pad = Youtuer('Mithilesh','Comedy')
# print(myth_pad.email)
# print(type(myth_pad))
# print(id(myth_pad))
# print(dir(myth_pad)) # returns all the arrtibutes and methods defined in it
# p = 'this is a string'
# print('----------------------------',dir(p)) # returns all the thing which we can do with it

import inspect
print(inspect.getmembers(myth_pad))