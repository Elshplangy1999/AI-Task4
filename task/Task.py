
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 21 20:48:51 2021

@author: Emad Elshplangy
"""

#question 1 & 2


import numpy as np
import pandas as pd
dataset=pd.read_csv("Wuzzuf_Jobs.csv")
dataset.describe()




#question 3



import numpy as np
import pandas as pd
# making data frame from csv file
data = pd.read_csv("Wuzzuf_Jobs.csv")

# dropping ALL duplicate values
data.drop_duplicates(subset =None,
					keep = "first", inplace = True)

import numpy as np
import pandas as pd

dataset = pd.read_csv("Wuzzuf_Jobs.csv")
W = dataset.iloc[:, :-1].values
Z = dataset.iloc[:, 3].values
from sklearn.impute import SimpleImputer
imputer_mean = SimpleImputer(missing_values=np.nan, strategy='most_frequent')
imputer_mean = imputer_mean.fit(W[:, 0:3])
W[:, 0:3] = imputer_mean.transform(W[:, 0:3])

print(W)


#question 4 & 5



import matplotlib.pyplot as plt
import pandas as pd
# Importing the dataset
dataset = pd.read_csv('Wuzzuf_Jobs.csv')

w = dataset['Company'].value_counts()
plt.pie(w)
plt.show() 
print ('the most demanding companies for jobs are', w.index[0:5] )





#question 6 & 7




import matplotlib.pyplot as plt
import pandas as pd
# Importing the dataset
dataset = pd.read_csv('Wuzzuf_Jobs.csv')

b = dataset['Title'].value_counts()
print ('the Most popular jobs title are', b.index[0:5] )
fig = plt.figure(figsize = (10, 5))
plt.bar(b.index[0:5], b[0:5], color ='maroon',
		width = 0.4)

plt.xlabel("Most popular jobs title")
plt.ylabel("Number of popular jobs title")
plt.title("Popular jobs title")
plt.show()




#question 8 & 9


import matplotlib.pyplot as plt
import pandas as pd
# Importing the dataset
dataset = pd.read_csv('Wuzzuf_Jobs.csv')

a = dataset['Location'].value_counts()
print ('the Most popular areas are', a.index[0:5] )
fig = plt.figure(figsize = (10, 5))
plt.bar(a.index[0:5], a[0:5], color ='maroon',
		width = 0.4)

plt.xlabel("Most popular areas")
plt.ylabel("Number of popular areas")
plt.title("Popular areas")
plt.show()



#question 10


Dict=dict()
for skills in dataset['Skills']:
    for skill in skills.split(','):
        if skill in Dict.keys():
            Dict[skill]+=1
        else:
            Dict[skill]=1
from collections import Counter          
Max =Counter(Dict)
MaxFive= dict(Max.most_common(5))
print("Top 5 skills :-")
for skill,count in MaxFive.items():    
    print("%s : %d"%(skill,count))