# K-Means_Clustering_with_Data_visualization
To process the learning data, the K-means algorithm in data mining starts with a first group of randomly selected centroids, which are used as the beginning points for every cluster, and then performs iterative (repetitive) calculations to optimize the positions of the centroids

It halts creating and optimizing clusters when either:

The centroids have stabilized — there is no change in their values because the clustering has been successful.
The defined number of iterations has been achieved.


1.Specify number of clusters K.

2.Initialize centroids by first shuffling the dataset and then randomly selecting K data points for the centroids without replacement.

3.Keep iterating until there is no change to the centroids. i.e assignment of data points to clusters isn’t changing.

# FORMULA
![indir](https://github.com/muratgorgl/K-Means_Clustering_with_Data_visualization/assets/105209043/dc674a74-1575-4860-91f8-a7611ac1075b)

# The Libraries
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np 
from sklearn.cluster import KMeans

# Purpose
We have a file of customers' data in a mall. We analyze data using their age, gender, shopping volume and salaries. First, we pull their shopping volume and salaries from the data file.

We visualize them. We cluster similar datapoints. Thus, when a new customer arrives, we discard which cluster this customer belongs to.

![Figure 2023-06-25 114229](https://github.com/muratgorgl/K-Means_Clustering_with_Data_visualization/assets/105209043/7ebca9d8-ecf8-4491-aee7-8e4c2de90f72)

Finally, we look at the WCSS (Within-Cluster Sums of Squares) value. By taking these values, we combine the datapoints by obtaining a linear graph in the x-y graph.

![Figure 2023-06-25 114244](https://github.com/muratgorgl/K-Means_Clustering_with_Data_visualization/assets/105209043/b7a54cb3-5dfa-4632-8b92-b5e04ebfb9a6)

As seen in the graph, which is the most successful of the datapoints here, we can call it the elbow point.



