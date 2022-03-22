import pandas as pd
from datetime import datetime
import os
import numpy as np
import time

dirPath = os.getcwd()
print(dirPath)
filepath = dirPath + '/SchedulerTest.csv'


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
