# -*- coding: utf-8 -*-
"""
Created on Sat Jun 24 13:14:07 2023

@author: Murat
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np 


data=pd.read_csv("customers.csv")

x=data.iloc[:,3:]
print(data.iloc[:,3:])


from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=3,init="k-means++")
kmeans.fit(x)


print(kmeans.cluster_centers_)
#print(kmeans.cluster_centers_,"It shows in which coordinates the centers are formed")
print(kmeans.inertia_)


y_kmeans = kmeans.predict(x)
plt.scatter(x.iloc[:,0], x.iloc[:,1], c=y_kmeans,s=10,cmap="viridis")
plt.scatter(kmeans.cluster_centers_[:,0],kmeans.cluster_centers_[:,1] ,c="black",s=200,alpha=0.5)
plt.show()
                                
results = []

for i in range (1,11):
    kmeans = KMeans(n_clusters=i,init="k-means++",random_state=(123))
    kmeans.fit(x)
    results.append(kmeans.inertia_)
    #results.append(kmeans.inertia_"#wcss Values)
plt.plot(range(1,11),results)
plt.show()





