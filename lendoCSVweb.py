# Import packages
# LendoCSVweb

# Import package

#import matplotlib.pyplot as plt
import pandas as pd

# Assign url of file: url
url = 'https://raw.githubusercontent.com/luasampaio/datasets/main/customers.csv'

# Read file into a DataFrame: df
df = pd.read_csv(url, sep=',', header=0)

# Print the head of the DataFrame
print(df.head())


"""""
# Plot first column of df
pd.DataFrame.hist(df.ix[:, 0:1])
plt.xlabel('fixed acidity (g(tartaric acid)/dm$^3$)')
plt.ylabel('count')
plt.show()

"""


