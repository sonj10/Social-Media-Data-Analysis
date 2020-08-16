import tweepy
import networkx as nx
import matplotlib.pyplot as mp
import csv
import pdb 
import numpy as np 
import time


def main():
    auth = tweepy.OAuthHandler("AMJiUvTP15ypCPx2mvdVSFZRh", "AOJCcZp0R7t3B9Yys5pZ9AS69PCJ0BSKeRbFgkeMYE9UMYehhi")
    auth.set_access_token("1166906393728712704-Ol0xJUULYcuL2Ua9WlhaFQhFEcRkxm", "qkPZ4nFQny7QBKWxF5SwFSyZtYcQlA7EP4A9l3FxgUzSs")
    
    # If we are getting a rate limit error, we can use the Access tokens provided below instead,    
    # just un-comment the below 2 lines and comment the above 2 lines

    # auth = tweepy.OAuthHandler("7afPiWMqu4I7XWnuTc60CSDRd", "t2PXm2NuKJxTtbBPHxWkVD5vZ6EqdsfyzRQ7fXqNX0MJPkiKGc")
    # auth.set_access_token("808769725891166208-YGkneXPAzpWE80VkPGxtdTuHgOjB5iq", "68YIizAoaj2bNSfzI8kvyyFsMhs8X4mpuGH5at9LqZ8vl")
    
    api = tweepy.API(auth)

    G_symmetric = nx.DiGraph()

    with open('node_relations.csv', 'w', newline= '') as writeFile11:
        writeFile11.truncate()
    writeFile11.close()

    with open('nodes.csv', 'w', newline= '') as writeFile12:
        writeFile12.truncate()
    writeFile12.close()

    # This is the parent node, the first user is being assigned
    id = 'sonj_10'      
    nodesCount = 0
    nodesList = []
    uniqueNodes = []
    i = 0

    # Step 2 of project: Data Collection
    while(nodesCount < 150):
        addFollowers(id,api,G_symmetric)
        with open('node_relations.csv', newline='') as readFile2:
            data = list(csv.reader(readFile2))
        for row in data:
            nodesList.append(row[1])
        uniqueNodes = unique(nodesList)       
        nodesCount = len(uniqueNodes)
        id=uniqueNodes[i]
        i += 1
    
    # Printing all the nodes in the nodes.csv file
    with open('nodes.csv', 'a', newline= '') as writeFile2:
        writer = csv.writer(writeFile2)
        for x in zip(uniqueNodes):
            writer.writerow(x)
    writeFile2.close()

    # Step 3 of project: Data Visualization
    # Creating edges between the nodes using the information present in the node_relations.csv file
    addEdges(G_symmetric)
    # Displaying the graph
    printGraph(G_symmetric)

    # Step 4 of project: Network Measures Calculation
    print("\n Output:")
    print("\n Avg Clustering coefficient: ",nx.average_clustering(G_symmetric))
    print("\n Closeness Centrality of all the nodes: \n", nx.closeness_centrality(G_symmetric))
    print("\n \n Page rank of all the nodes: \n",nx.pagerank(G_symmetric))
    plot_degree_dist(G_symmetric)
    
   
def unique(list1): 
  
    # intilize a null list 
    unique_list = [] 
      
    # traverse for all elements 
    for x in list1: 
        # check if exists in unique_list or not 
        if x not in unique_list: 
            unique_list.append(x) 
    # return list
    return unique_list 
    

def printGraph(G):
    nx.draw(G, with_labels=True)
    mp.draw()
    mp.show()


def addEdges(G):
    with open('node_relations.csv', newline='') as readFile:
        data = list(csv.reader(readFile))

    for i in data:
        # Adding directed edges between followers and followees
        if (len(i) == 2):
            G.add_edge(i[1],i[0]) 


def addFollowers(usr,api,G):
    try:
        user = api.get_user(usr,api)
        # Adding all the followers of the user to the list
        for friend in user.followers():
            l1 = [[usr,friend.screen_name]]

            # Printing the information between followees and their respective followers in the node_relations.csv file
            with open('node_relations.csv', 'a', newline= '') as writeFile:
                writer = csv.writer(writeFile)
                writer.writerows(l1)
            writeFile.close() 
    except:
        print('Rate limit error, Waiting for 60s') 
        time.sleep(60)


def plot_degree_dist(G):   
    # To get the degree distribution
    degrees = [G.degree(n) for n in G.nodes()]
    # To plot the histogram
    mp.hist(degrees)
    
    mp.title("Degree Distribution")
    mp.ylabel("Count")
    mp.xlabel("Degree")
    mp.show()
           

if __name__ == "__main__":
    main()
    pass


 
