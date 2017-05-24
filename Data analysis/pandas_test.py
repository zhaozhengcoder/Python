import pandas as pd
#import numpy as np
import matplotlib.pyplot as plt


path="1.xls"
df=pd.read_excel(path)
print (df.head())

#print (df['speed'])

plt.plot(df['time'],df['vol'])
plt.show()

#print (df['vol'])

"""
print (df['speed'][1])

print (type(df['speed'][1]))
print (type (df['vol'][1]))

x=[]
y=[]
for i in range(0,10):
    x.append(df['vol'][i])
    y.append(df['speed'][i])
plt.plot(x,y)
plt.show()
"""




