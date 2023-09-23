import pandas as pd
from meerkat import Meerkat

meer = Meerkat(pd)
res = meer.look_in()
print(res)
