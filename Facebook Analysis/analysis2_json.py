import pickle
import pandas as pd
import numpy as np
import string
from operator import itemgetter
from datetime import datetime
from time import strptime
import json
from dateutil.parser import parser
import matplotlib.pyplot as plt

#loading the data from pkl file
loaded_data = pickle.load(file=open('test.pkl'))
# print (type (loaded_data[0]))

# coverting the data into dataframe and then normalizing it
df2 = pd.io.json.json_normalize(data=loaded_data)
time = df2['created_time']
posts=[]

for row in time:

    # row = row.strip('+0000')
    row = row[0:19]
    # t = datetime.fromtimestamp(row)
    # posts.append(t.strftime('%H:%M:%S'))
    # created_time = parser.parse(row)
    # posts.append(created_time.strftime('%H:%M:%S'))
    t = datetime(*strptime(row, "%Y-%m-%dT%H:%M:%S")[0:6])
    # t = datetime(*strptime(row, "%H:%M:%S")[0:6])
    posts.append(t.hour)
    # print my_hours
    # posts.append(str(t).split(' ')[1])
    # print t
#     for my_time in t.hour:
#         posts.append(my_time)
print posts

#     posts = [t.time() for time in time]
# print posts

    # data = np.asarray(my_hours)
    # print data

# bins = np.arange(-100, 100, 5)

#Creating a histogram showing the time of of all my facebook posts
nums = [x for x in range(0,24)]
plt.xticks(nums)
plt.hist(posts)
plt.show()
