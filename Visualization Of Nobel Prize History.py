#!/usr/bin/env python
# coding: utf-8

# # Visualization Of Nobel Prize History

# The "Visualization of Nobel Prize Datasets" project aims to create interactive and informative visualizations based on the extensive Nobel Prize datasets. The Nobel Prize is a prestigious international award given annually in various categories, including Physics, Chemistry, Medicine, Literature, Peace, and Economic Sciences. This project seeks to analyze and present the historical data related to Nobel laureates, their achievements, and the overall trends in Nobel Prize recognition.

# # Importing Librarie

# These are just a few examples of popular Python libraries. You can import any other library using the same import statement followed by the library name or alias:
# 
# NumPy: for numerical operations and array manipulation
# 
# Pandas: for data manipulation and analysis
# 
# Matplotlib: for creating visualizations
# 
# Scikit-learn: for machine learning algorithms

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

get_ipython().run_line_magic('matplotlib', 'inline')


# # Importing Dataset

# In[2]:


dataframe = pd.read_csv('nobel.csv')


# # Data Visualization

# Data visualization is the graphical representation of information and data, designed to make complex datasets more accessible, understandable, and interpretable. It involves the use of visual elements such as charts, graphs, maps, and infographics to present data and patterns in a visual format. Data visualization plays a crucial role in data analysis, as it enables users to identify trends, correlations, and insights that might not be immediately evident in raw data.

# In[3]:


dataframe.head()


# # Country With Most Nobel Prize 

# From the output we can see that American have most nobel prize around the world followed by the United Kingdom.We can also see that out of total 911 nobel prizes males won more than the womens.

# In[5]:


from IPython.display import display
display(len(dataframe["prize"]))

display(dataframe["sex"].value_counts())

dataframe["birth_country"].value_counts().head(10)


# # USA Dominance 

# Since, USA has more nobel prize tha other country lets see the dominance of use in nobel prize history, this output will show the winners that are likely to born in different interval of the decade , it shoes that the chances are likely less than 50% 

# In[9]:


dataframe['usa_born_winner'] = dataframe["birth_country"] == "United States of America"
dataframe['decade'] = (np.floor(dataframe['year'] / 10) * 10).astype(int)
usa_winners = dataframe.groupby("decade", as_index=False)["usa_born_winner"].mean()

display(usa_winners)


# # Visualizing USA Dominance 

# In[10]:


plt.rcParams['figure.figsize'] = [11, 7]
 
ax = sns.lineplot(data=usa_winners, x="decade", y="usa_born_winner")

from matplotlib.ticker import PercentFormatter
ax.yaxis.set_major_formatter(PercentFormatter(1.0))


# # Nobel Prize In Different Field By Women

# From the diagram below we can see that the most nobel prize won by women is in peace sector.

# In[11]:


dataframe['female_winner'] = dataframe["sex"] == "Female"
female_winners = dataframe.groupby(["decade", "category"], as_index=False)["female_winner"].mean()

sns.set()
plt.rcParams["figure.figsize"] = [11, 7]
ax = sns.lineplot(data=female_winners, x="decade", y="female_winner", hue="category")

ax.yaxis.set_major_formatter(PercentFormatter(1.0))


# # First Women To Win The Nobel Prize

# In[12]:


dataframe.loc[dataframe["sex"] == "Female"].nsmallest(1, "year")


# # Age At Which You Get Nobel Prize

# As we can see most people got their nobel prize when they are around the age of 60-70

# In[14]:


dataframe['birth_date'] = pd.to_datetime(dataframe["birth_date"], utc=True)

dataframe['age'] = dataframe["year"] - dataframe["birth_date"].dt.year

sns.lmplot(x="year", y="age", data=dataframe, lowess=True, aspect=2, line_kws={"color":'black'})


# The above daigram shows us a lot, so lets divide the them in their respective field.

# In[15]:


sns.lmplot(x="year", y="age", data=dataframe, row="category", lowess=True, aspect=2, line_kws={"color":'black'})


# # Oldest And Youngest Nobel Prize Winner 

# In[17]:


dataframe.nsmallest(1, "age")


# In[18]:


dataframe.nlargest(1, "age")


# # Thanks
