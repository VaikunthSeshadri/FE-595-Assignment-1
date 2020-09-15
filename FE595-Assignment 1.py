#!/usr/bin/env python
# coding: utf-8

# In[3]:


import matplotlib.pyplot as plt
import numpy as np


# In[15]:


x = np.arange(0, 2*np.pi, 0.01)
y = np.sin(x)
z = np.cos(x)


# In[17]:


plt.plot(x, y, x, z)
plt.xlabel('X-values from 0 to 2 pi')
plt.ylabel('sin(x), cos(x)')
plt.legend(['sin(x)', 'cos(x)'])
plt.title('Plot of sin(x) and cos(x) for one period')
plt.show()

