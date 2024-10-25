import pandas as pd
from openspace import Openspace
# from utils.openspace import Openspace
import random
df = pd.read_excel('/home/betty/Desktop/bouman_8.xlsx', header = None)
names = df[0].tolist()
# print(names)
# print(len(names))
# print(random.randint(1,100))
op= Openspace(6)
op.organize(names)
op.display()
op.store()
