import pandas as pd
import numpy as np

exam_data={'name':['anastasia','dima','katherine','james','laura'],
           'socre':[12.5,9,16.5,np.nan,10],
           'attempts':[1,3,2,3,2],
           'qualify':['yes','no','yes','no','no']}
labels = ['a', 'b', 'c', 'd', 'e']
df = pd.DataFrame(exam_data , index=labels)
print("First three rows of the data frame:")
print(df.iloc[:3])
