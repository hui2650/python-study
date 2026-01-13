import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('default')

df = pd.read_csv('./data/auto-mpg.csv', header=None)

df.columns = ['mpg','cylinders','displacement','horsepower','weight',
              'acceleration','model year','origin','name']

# count 컬럼 추가
df['count'] = 1
print(df)

df_origin = df.groupby('origin').sum(numeric_only=True)
print(df_origin)
print()

df_origin.index = ['USA', 'EU', 'JAPAN']
print(df_origin)
print()

df_origin['count'].plot(kind='pie', figsize=(7, 5),
                        autopct='%1.1f%%', # % 포맷팅
                        startangle=90,
                        textprops={'fontsize':14},
                        colors=['chocolate', 'bisque', 'cadetblue']
                        )
plt.title('Model Origin', size=20)
plt.axis('equal')
plt.legend(labels=df_origin.index)
plt.show()