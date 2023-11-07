import matplotlib.pyplot as plt
import pandas as pd
import requests

df = pd.read_csv('thor_wwii.csv')

print(df.columns.tolist())

sample = df.sample(50)
print("Sample DataFrame:")
print(sample)

aircraft = sample['AC_ATTACKING'].tolist()
print("Aircraft List:")
print(aircraft)
plt.grid(True, linewidth=1, linestyle="--")