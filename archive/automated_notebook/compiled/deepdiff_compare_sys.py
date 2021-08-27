import sys
from copy import copy
from deepdiff import DeepDiff
from pprint import pp

a = copy(sys.modules)
import function_0001

b = copy(sys.modules)

dd = DeepDiff(a, b, ignore_order=True)
pp(dd)

function_0001.function_0001()

c = copy(sys.modules)

dd2 = DeepDiff(b, c, ignore_order=True)
pp(dd2)
