import types

from inspect import ismodule, isclass, ismethod, isfunction,\
                    isgeneratorfunction,isgenerator, istraceback,\
                    isframe, iscode, isbuiltin,isroutine, ismethoddescriptor


print(globals())
_DICT_OF_TESTS = {(key,value) for (key,value) in globals().items() if key.startswith("is")}


    
class Meerkat():
    def __init__(self,main_library) -> None:
        self.main_library = main_library
        print(self.main_library)
    
    def look_in(self):
        names = dir(self.main_library)


        for attribute in names:
            obj = None
            try:
                attribute_value = getattr(self.main_library, attribute)
            except Exception as exc:
                pass
            if isinstance(attribute_value, (staticmethod, types.BuiltinMethodType)):
                kind = "static method"
                obj = attribute_value
            elif isinstance(attribute_value, (classmethod, types.ClassMethodDescriptorType)):
                kind = "class method"
                obj = attribute_value
            elif isinstance(attribute_value, property):
                kind = "property"
                obj = attribute_value
            elif isroutine(obj):
                kind = "method"
            else:
                kind = "data"
            print(attribute + " ",kind)

if __name__ == "__main__":
    import pandas as pd
    meer = Meerkat(pd)
    meer.look_in()