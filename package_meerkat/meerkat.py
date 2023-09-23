from inspect import *
import re
from collections import defaultdict
from pyvis.network import Network
from d3graph import d3graph, vec2adjmat, adjmat2vec
from d3blocks import D3Blocks
import matplotlib.pyplot as plt
from matplotlib.cm import viridis
from matplotlib.colors import rgb2hex
import pydot


_DICT_OF_TESTS = {(key,value) for (key,value) in globals().items() if key.startswith("is")}

num_categories = len(_DICT_OF_TESTS)
_DICT_OF_COLORS = dict({(key,rgb2hex(viridis(float(i)/num_categories) ) ) for i,(key,value) in enumerate(_DICT_OF_TESTS)})
print(_DICT_OF_COLORS)
class Meerkat():
    def __init__(self,main_library, depth_level=1, remove_underscore = True, remove_double_underscore=True) -> None:
        self.main_library = main_library
        self.main_library_name = main_library.__name__
        self.depth_level = depth_level
        self.remove_underscore = remove_underscore
        self.remove_double_underscore = remove_double_underscore
        self.network = Network(height=500,width=500,notebook=False)
        self.network.add_node(0,str(main_library),color='#0000ff')
        self.graph = d3graph()
        self.pydot_graph = pydot.Dot(graph_type='digraph', rankdir='LR')
        self.json_results = defaultdict(list)

    def look_in(self):
        names = dir(self.main_library)
        if self.remove_underscore:
            names = list(filter(lambda x: not re.match("^_[a-zA-Z]" ,x) ,names))
        if self.remove_double_underscore:
            names = list(filter(lambda x: not re.match("^__[a-zA-Z]" ,x) ,names))
        for id,attribute in enumerate(names):
            try:
                attribute_value = getattr(self.main_library, attribute)
            except Exception as exc:
                pass
            for key,function in _DICT_OF_TESTS :
                if function(attribute_value) and function is not isroutine:
                    self.json_results[attribute].append(key)
                    self.network.add_node(id + 1,attribute + " " + key)
                    self.pydot_graph.add_edge(pydot.Edge(self.main_library_name,attribute))
 
    
    def generate_graph(self):
        self.network.barnes_hut()
        self.network.toggle_hide_edges_on_drag(False)
        self.network.show("nodes.html",notebook=False)
        
    def generate_graph2(self):
        target = list(self.json_results.keys())
        source = [str(self.main_library.__name__)] * len(target)
        weight = [1] * len(target)
        adjmat = vec2adjmat(source=source,target=target,weight=weight)
        print("adj ",adjmat)
        vector = adjmat2vec(adjmat)
        vector["cluster"] = vector["target"].apply(lambda x: self.json_results.get(x)[0])
        vector["cluster_color"] = vector["cluster"].apply(lambda x: _DICT_OF_COLORS.get(x))
        root_elements = list(set(vector.cluster))
        vector["weight"] = vector["cluster"].apply(lambda x: root_elements.index(x)+1)        
        print(vector)
        print(vector["weight"])
        print(len(vector["weight"]))
        vector = vector.sort_values(by="cluster_color")
        d3 = D3Blocks()
        d3.d3graph(vector, showfig=False)
        print("len", len(list(vector["cluster_color"])))
        d3.D3graph.set_node_properties(color=["#4ac16d"] +list(vector["cluster_color"]))
        d3.D3graph.show()
    
    def generate_graph3(self):
        self.pydot_graph.write_png(r"C:\Users\FRAG-PC\projects\package_meerkat\test.png")

if __name__ == "__main__":
    import numpy as pd
    meer = Meerkat(pd)
    meer.look_in()
    print(meer.json_results)
    meer.generate_graph3()
    
