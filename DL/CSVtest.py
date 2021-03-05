import pandas as pd 

data = pd.read_csv("OBJECTS.csv",delimiter=",")
print(data.head())
print(data.shape)