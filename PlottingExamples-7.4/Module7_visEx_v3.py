#!/usr/bin/env python
# coding: utf-8

# ## Visualization examples
# 
# Examples taken from the World Happiness Report via Kaggle.  Note:  billed as "Suicide" data which is sort of the converse of happiness.

# In[9]:


import os.path
import matplotlib.pyplot as plt
import numpy as np

import pandas as pd


pd.set_option("display.max_rows", 5)


# In[10]:


# stub for world happiness report... (SUICIDED DATA SET)

DATAPATH = '/Users/ergonyc/Projects/Insight/Data'
DATA_DIR = DATAPATH + '/world-happiness-report'

YEAR015_FILE = os.path.join(DATA_DIR, '2015.csv')
YEAR016_FILE = os.path.join(DATA_DIR, '2016.csv')
YEAR017_FILE = os.path.join(DATA_DIR, '2017.csv')


# Lets start with just 2017 data to start wiith and explore the dataset.  Second step will be to check on how similar the three years data fields are.  

# In[13]:


# Load suicide data.
year17 = pd.read_csv(YEAR017_FILE, sep=',')

year17.head()
#suicides = pd.concat([year15, year16, year17])


# In[14]:


year17.describe()


# In[ ]:


# Load suicide data.
year15 = pd.read_csv(YEAR015_FILE, sep=',')
year16 = pd.read_csv(YEAR016_FILE, sep=',')
year17 = pd.read_csv(YEAR017_FILE, sep=',')

year15.head()
year16.head()
year17.head()


# ## questions
# 
# correlation between wealth and hapiness
# 
# family and happiness

# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

# Generate 1000 random values.
x = np.random.normal(10, 5, 1000)
y = np.random.normal(11,10,1000)
# Plot them as a histogram.
plt.hist(x) 
plt.show()# Same data, this time normed, using density.
plt.hist(x, density=True, color='blue', bins=np.arange(-10, 40), alpha=.5) 
plt.hist(y, density=True, color='red', bins=np.arange(-10, 40), alpha=.5)
plt.title('Normed histograms')
plt.xlabel('Random Values')

plt.show()


# In[ ]:





# In[ ]:


# Set the random seed to keep the example consistent.
np.random.seed(111)

# Sample data.
x = np.random.normal(10, 5, 1000)

# Generate and display the box plot.
plt.boxplot(x)
plt.show()

