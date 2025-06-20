import os
import inspect

DATA_PATH = os.path.join(os.path.dirname(inspect.getfile(inspect.currentframe())), "data{}".format(os.sep))
# print(DATA_PATH)