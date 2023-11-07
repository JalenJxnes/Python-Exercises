import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("company_sales_data.csv")
monthlist = df ['month_number'].tolist()
facecreamdata = df ['facecream'].tolist()
facewashdata = df ['facewash'].tolist()
plt.bar([a-0.25 for a in monthlist], facecreamdata, width= 0.25, label = 'Face Cream', align='edge')
plt.bar([a+0.25 for a in monthlist], facewashdata, width= -0.25, label = 'Face Wash', align='edge')
plt.xlabel('Month')
plt.ylabel('Number of Sales')
plt.legend(loc='upper left')
plt.xticks(monthlist)
plt.grid(True, linewidth= 1, linestyle="--")
plt.title('Fulbright Cosmetics Sales Data')

plt.savefig("saleschart.png")