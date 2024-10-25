import pandas as pd
from utils.openspace import Openspace

df = pd.read_excel('/home/betty/Desktop/bouman_8.xlsx', header = None)
names = df[0].tolist()

op= Openspace(6)
op.organize(names)
op.display()
op.store()
