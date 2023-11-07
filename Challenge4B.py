import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('thor_wwii.csv')

summed_df = df.groupby(['COUNTRY_FLYING_MISSION']).sum(numeric_only=True)
summed_df = summed_df / 1000
summed_df = summed_df.reset_index()

countries = summed_df['COUNTRY_FLYING_MISSION'].tolist()

fig, ax = plt.subplots()
ax.bar(countries, tons_he, label="High Explosive")
ax.bar(countries, tons_ic, label="Incendiary")
ax.bar(countries, tons_frag, label="Fragmentation")

ax.set_ylabel('Kilotons of Munitions')

ax.legend()
plt.yticks(fontsize ='xx-small')
plt.xticks(rotation=-90, fontsize='xx-small')