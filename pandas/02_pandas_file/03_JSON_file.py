import pandas as pd

df = pd.read_json('./data/read_json_sample.json')

print(df)
print()

print(df.index)
print()

df2 = pd.read_json('./data/read_json_sample.json', orient = 'index')
print(df2)
print()

df3 = pd.read_json('./data/read_json_sample.json', orient = 'columns')
print(df3)
print()
print(df3.T)