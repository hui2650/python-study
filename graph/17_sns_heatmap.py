import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

titanic = sns.load_dataset('titanic')

sns.set_style('darkgrid')


table = titanic.pivot_table(titanic,
                      index=['sex'],    
                      columns=['class'],    
                      aggfunc='size',   
                      observed=True)

sns.heatmap(table, annot=True, fmt='d', cmap='YlGnBu', linewidth=0.5, cbar=True)

plt.show()