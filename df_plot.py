# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 16:27:25 2017

@author: dream_rab04is
"""

# Import Pyplot as plt from matplotlib
import matplotlib.pyplot as plt


# Create a DataFrame from the results: df
df = pd.DataFrame(results)

# Set Column names
df.columns = results[0].keys()

# Print the DataFrame
print(df)

# Plot the DataFrame
df.plot.bar()
plt.show()