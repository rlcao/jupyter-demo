#!/usr/bin/env python
# coding: utf-8

#  # jupyter demo
# **This is a demostration of what jupyter notebook can do**
# 1. run live python code
# 2. insert markdown documentation
# 3. magic commands using percent(single/double) sign
# 4. jupyter extention, such as sql
# 5. better to record version information in the beginning
# 6. better to load ext and imports in the beginning
# 7. you can use hooks to do some additional things you want to do
# 
# # Issue to consider when working with jupyter
# 1. how to collaborative within team?
# 2. how to reliably capture and share it with team members?
# - save different format of the output, such as .py and .html
# 3. clearly deliver insights to other team members?
# 

# In[2]:


mystr = "Hello World!"


# In[3]:


print(mystr);


# In[9]:


with open("mytrain.dat",'w') as fh:
    for i in range(0,100,5):
        fh.write(" ".join([str(x) for x in range(i,i+5)]))
        fh.write("\n")


# In[10]:


get_ipython().system('cat mytrain.dat')


# In[12]:


recall 3


# In[13]:


print(mystr);


# In[14]:


pycat mytrain.dat


# In[15]:


get_ipython().run_line_magic('pinfo', 'mystr')


# In[16]:


get_ipython().system('echo $HOME')


# In[17]:


get_ipython().run_line_magic('lsmagic', '')


# In[18]:


get_ipython().run_line_magic('pwd', '')


# In[19]:


get_ipython().run_line_magic('ls', '')


# In[21]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[24]:


"""Simple demo of a scatter plot."""
import numpy as np
import matplotlib.pyplot as plt

N = 50
x = np.random.rand(N)
y = np.random.rand(N)
colors = np.random.rand(N)
area = np.pi * (15 * np.random.rand(N))**2 # 0 to 15 point radiuses

plt.scatter(x, y, s=area, c=colors, alpha=0.5)
plt.show()


# In[25]:


get_ipython().run_cell_magic('timeit', '', 'square_events = [n*n for n in range(1000)]')


# In[34]:


get_ipython().run_cell_magic('HTML', '', '<a href="https://github.com/jupyter/jupyter/wiki/A-gallery-of-interesting-Jupyter-Notebooks">A gallery of interesting Jupyter notebooks</a>')


# In[2]:


from IPython.display import IFrame


# In[4]:


IFrame("http://www.eia.gov/coal/data.cfm",width=700,height=350)


# In[ ]:


# %load mytrain.dat
0 1 2 3 4
5 6 7 8 9
10 11 12 13 14
15 16 17 18 19
20 21 22 23 24
25 26 27 28 29
30 31 32 33 34
35 36 37 38 39
40 41 42 43 44
45 46 47 48 49
50 51 52 53 54
55 56 57 58 59
60 61 62 63 64
65 66 67 68 69
70 71 72 73 74
75 76 77 78 79
80 81 82 83 84
85 86 87 88 89
90 91 92 93 94
95 96 97 98 99


# In[8]:


who


# In[2]:


get_ipython().run_line_magic('load_ext', 'sql')


# In[3]:





# In[4]:


import pandas as pd


# In[7]:


dct = {'one' : pd.Series([1., 2., 3.], index=['a', 'b', 'c']),
       'two' : pd.Series([1., 2., 3., 4.], index=['a', 'b', 'c', 'd'])}
df = pd.DataFrame(dct)


# In[8]:


get_ipython().run_cell_magic('sql', 'sqlite://', '    PERSIST df')


# In[10]:


get_ipython().run_line_magic('lsmagic', '')


# In[9]:


who


# In[11]:


get_ipython().run_cell_magic('sql', 'sqlite://', 'select * from df')


# In[12]:


df.head()


# In[13]:


dbtest = get_ipython().run_line_magic('sql', 'select * from df')


# In[19]:


type(dbtest)


# In[21]:


get_ipython().run_line_magic('load_ext', 'version_information')
get_ipython().run_line_magic('version_information', 'numpy,matplotlib,pandas')


# In[ ]:




