from inspect import *
from collections import defaultdict


_DICT_OF_TESTS = {(key,value) for (key,value) in globals().items() if key.startswith("is")}
    
class Meerkat():
    def __init__(self,main_library, depth_level=1, remove_underscore = True, remove_double_underscore=True) -> None:
        self.main_library = main_library
        self.depth_level = depth_level
        self.remove_underscore = remove_underscore
        self.remove_double_underscore = remove_double_underscore
    
    def look_in(self):
        names = dir(self.main_library)
        json_results = defaultdict(list)
        for attribute in names:
            try:
                attribute_value = getattr(self.main_library, attribute)
            except Exception as exc:
                pass
            for key,function in _DICT_OF_TESTS:
                if function(attribute_value):
                    json_results[attribute].append(key)
        return json_results

if __name__ == "__main__":
    import pandas as pd
    meer = Meerkat(pd)
    res = meer.look_in()
    print(res)
    
