import pandas as pd

df = pd.read_csv('./data/stock-data.csv')

df['new_Date'] = pd.to_datetime(df['Date'])

df = df.set_index('new_Date').sort_index()
df = df.drop('Date', axis=1)
print(df)

ts = df.head(10)
print(ts)



print("\n======== shitf ========\n")

print(ts.shift(1))
print(ts.shift(-2))

print(ts.shift(3, freq='D'))
print()

print(ts.asfreq('5D'))
print()

print(ts.asfreq('5D', method='bfill'))
print()



print("\n======== resample ========\n")

print(ts.resample('3B'))
print()

print("sum: \n", ts.resample('3B').sum())
print("\nmean: \n", ts.resample('3B').mean())
print("\nmedian: \n",ts.resample('3B').median())



print("\n======== rolling ========\n")

print("rolling(window=3): \n", ts.rolling(window=3).sum())
print("\nrolling(window=3D): \n", ts.rolling(window='3D').sum())


