# -*- coding: utf-8 -*-
"""MAREPALLI VISHNU VARDHAN_21BEC2508_HITWICKET.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1o4Fhwn_1SokEvWslOCOo8-xDItMboafJ
"""

import numpy as np

import pandas as pd

"""PROBLEM 1: Write the syntax to create the following DataFrame"""

data = {
    'Class':[4,4,5,1,1,2,5,2], 'Gender': ['Female','Male','Male','Female','Male','Female','Female','Male'],
    'Values':[10,3,1,5,7,2,5,10]
}
dataframe = pd.DataFrame(data)
print(dataframe)

"""Problem 2
Write the syntax to sort this DataFrame by Class (ascending order) followed by Values (descending)

"""

df = dataframe.sort_values(['Class','Values'], ascending=[True,False])
df

"""Problem 3
Write the syntax to group this DataFrame by Class, Gender and count the number of unique values

"""

gr_df = df.groupby(['Class','Gender'])['Values'].nunique().reset_index()
gr_df

"""Problem 4
Write the syntax to visualize the Data in a Scatter Plot in Python (Class on the X-axis, Values in Y), with color differentiation based on Gender.

"""

from matplotlib import pyplot as plt
import seaborn as sns
sns.scatterplot(x=df['Class'],y=df['Values'],hue=df['Gender'])
plt.title('Class VS Values based on Gender')
plt.xlabel('Class')
plt.ylabel('Values')

# Displaying the plot
plt.show()

"""Problem 5
Write the syntax to reshape/summarize the table above, to display the following output

"""

new_df = df.pivot_table(index='Class', columns='Gender', values='Values', aggfunc='sum', fill_value=0).reset_index()
new_df.columns.name = None
new_df = new_df[['Class', 'Female', 'Male']]
print(new_df)

"""For Problems 6-7, assume you have a dataframe called table_to_plot which contains 3 columns: Category, where values range from 1-9, x_variable and y_variable, where values range from 800-2000. A glimpse of the first few rows of the data frame is attached:

Problem 6
Use R or Python to plot all of the following graphs at once, in one window, for easier comparison of categories

"""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
# Sample DataFrame (replace this with your actual DataFrame)
data = {
    'Category': np.repeat(np.arange(1, 10), 10),
    'x_variable': np.random.randint(800, 2000, 90),
    'y_variable': np.random.randint(800, 2000, 90)
}
table_to_plot = pd.DataFrame(data)
# Set up the figure and axes for subplots
num_categories = table_to_plot['Category'].nunique()
fig, axes = plt.subplots(num_categories, 1, figsize=(4, 2 * num_categories), sharex=True, sharey=True)

for i, category in enumerate(sorted(table_to_plot['Category'].unique())):
    ax = axes[i] if num_categories > 1 else axes
    subset = table_to_plot[table_to_plot['Category'] == category]
    sns.regplot(data=subset, x='x_variable', y='y_variable', ax=ax, scatter_kws={'s': 50}, line_kws={"color": "red"})
    ax.set_title(f'Category {category}')
    ax.set_xlabel('x_variable')
    ax.set_ylabel('y_variable')
plt.tight_layout()
plt.show()

"""Problem 7:Create two additional columns in the dataframe table_to_plot, one corresponding to x_variable and one corresponding to y_variable, such that the values of the two existing columns are assigned labels based on what range they are located in, if we were to divide these columns into 3 equally sized intervals. Your result table might look something like this:

"""

data = {
    'Category': [1, 1, 2],
    'x_variable': [1900, 1590, 995],
    'y_variable': [1875, 1770, 1205]
}
table_to_plot = pd.DataFrame(data)

# Define the ranges for x_variable and y_variable using pd.cut
x_bins = [800, 1200, 1600, 2000]  # Define the bin edges
y_bins = [800, 1200, 1600, 2000]

# Create the x_range and y_range columns
table_to_plot['x_range'] = pd.cut(table_to_plot['x_variable'], bins=x_bins)
table_to_plot['y_range'] = pd.cut(table_to_plot['y_variable'], bins=y_bins)

# Display the resulting DataFrame
print(table_to_plot)

