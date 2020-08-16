# Social-Media-Data-Analysis
Visualized a network containing 200 Twitter users in the form of a graph and examined various network measures like degree distribution, page rank and clustering coefficients

## Contents

I [Platform](#i-platform)\
II [Data Collection](#ii-data-collection)\
III [Data Visualization](#iii-data-visualization)\
IV [Network Measures](#iv-network-measures)\
V [References](#v-references)


## I Platform

We have chosen Twitter as our social media platform and have scrapped data from it
using APIs.

## II Data Collection


To collect data from Twitter, we completed the following steps:

1. Create a developer account on twitter.
2. Obtain 4 pieces of information: API key, API secret, Access token and Access token
    secret.
3. Use tweepy library in python to access twitter data with the help of authentication
    details we obtained in the last step.
4. To collect the data in the csv file, run the python file named main.py in the terminal.
5. Now, the node_relations.csv file consists of a list of followees and their respective
    followers while the nodes.csv file consists only the list of all nodes present in the
    graph.


## III Data Visualization

1. We used the package ’networkx’ to visualize the graph.
2. We added the directed edges between the nodes using the data present in the csv
    file.
3. The directed graph will be displayed when main.py is run in the terminal.


![fig1](/images/Figure_1.png)
```
Figure 1: Visualization of the data in the form of a directed graph
```

## IV Network Measures

We have calculated various network measures:

* Degree Distribution
* Average Clustering Coefficient
* Closeness Centrality
* Page Rank


![fig1](/images/Figure_2.png)
```
Figure 2: Degree Distribution Histogram
```

## V References

1. An Introduction to Text Mining using Twitter Streaming API and Python - Adil
    Moujahid,
    Available: [http://adilmoujahid.com/posts/2014/07/twitter-analytics/](http://adilmoujahid.com/posts/2014/07/twitter-analytics/)
2. Social Network Analysis in Python - Amita Kapoor,
    Available: https://www.datacamp.com/community/tutorials/social-network-analysis-
    python
3. Tweepy Documentation,
    Available: https://tweepy.readthedocs.io/en/latest/
4. Networkx Documentation,
    Available: https://networkx.github.io/documentation/stable/reference/algorithms/centrality.html


