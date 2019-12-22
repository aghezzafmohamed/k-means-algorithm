# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 19:09:01 2019

@author: Aghezzaf mohamed
"""

import math
def Kmeans(E,k):
    M=[]
    Clusters={}
    #initialization of mi centers and clusters
    for i in range(k):
        var1,var2=E[i]
        M.append([var1,var2])
        Clusters[i]=[[var1,var2]]    
    
    while True:
        out=True
        for i in range(len(E)):
            distances=[]
            #Euclidean distance
            for j in range(k):
                d=math.sqrt(pow((M[j][0]-E[i][0]),2)+pow((M[j][1]-E[i][1]),2))
                distances.append(d)
            min=distances[0]
            indice=0
            for j in range(k):
                if(distances[j]<min):
                    min=distances[j]
                    indice=j
            #Assignment of each point to its cluster
            if(E[i] not in Clusters[1] and E[i] not in Clusters[0]):
                Clusters[indice].append(E[i])
        #Recalculate mi centers
        for j in range(k):
            m1=0
            m2=0
            for f in range(len(Clusters[j])):
                m1+=Clusters[j][f][0]
                m2+=Clusters[j][f][1]
            m1=m1/len(Clusters[j])
            m2=m2/len(Clusters[j])
            #If the centers are stable out = True "End of the algorithm"
            if(M[j][0]!=m1 and M[j][1]!=m2):
                out=False
            M[j][0]=m1
            M[j][1]=m2
        #Stop condition
        if(out):
            break
    print("Clusters",Clusters)
    
E=[[1,1],[4.5,5],[3,4],[5,7],[3.5,5],[3.5,4.5],[1.5,2]]
k=2
Kmeans(E,k)