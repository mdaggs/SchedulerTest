#!/usr/bin/env python
# coding: utf-8

# In[50]:


import pandas as pd
from datetime import datetime
import os
import numpy as np
import time


# In[51]:


filepath = 'SchedulerTest.csv'


# In[52]:

i = 0
while True:
    if os.path.isfile(filepath):
        print("File Exists, appending to old file")
        df = pd.read_csv(filepath, index_col=0)
        currentDate = datetime.now()
        print(currentDate)
        df = df.append({
            'Value': np.add(df['Value'].iloc[-1], 5),
            'Time': currentDate},
            ignore_index=True
        )
        print(df)
        df.to_csv(filepath)
    else:
        print("File Does not Exist, creating new file and appending")
        currentDate = datetime.now()
        print(currentDate)
        df = pd.DataFrame(
            columns=['Value', 'Time']
        )
        df = df.append({
            'Value': 5,
            'Time': currentDate},
            ignore_index=True
        )
        print(df)
        df.to_csv(filepath)
    i += 1
    if i == 5:
        print("Your Script Has Finished!!!!!")
        break
    time.sleep(5)
    

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




