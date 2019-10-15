__author__ = 'Rahul'
import numpy
import matplotlib.pyplot as plt
import random as rnd
from sklearn import cluster
import pandas
from pandas.tools.plotting import parallel_coordinates
import csv
import matplotlib as mpl

def sigmoid(z):
        """The sigmoid function."""
        return 1.0/(1.0+numpy.exp(-z))

def generator(dimension=2,size=1000,centroids=None):
    ctr=0;lst=[None]*dimension;temp=None;lst1=[None]*dimension
    for x in range(0,dimension):
        lst[x]=[]


    temp=numpy.transpose(centroids).astype(float)
    label=[]
    ctl=0
    while ctr<size:
        if ctr % 2==0:
            rn=rnd.randint(1,2)
            #rn1 =rnd.uniform(0.9,1.2)
        '''
        elif ctr % 3==0:
            rn = rnd.randint(1,7)
            #rn1 = rnd.uniform(0.9, 1.2)
        elif ctr % 4==0:
            rn = rnd.randint(1,4)
            #rn1 = rnd.uniform(1, 2.3)
        elif ctr % 31==0 or ctr % 61==0 or ctr % 23==0 or ctr % 17==0 or ctr % 11==0:
            rn = rnd.randint(1,2)
            #rn1 = rnd.uniform(1.7, 3)
        else:
            rn = rnd.randint(1, 7)
            #rn1 = rnd.uniform(0.9, 1.4)
        '''

        rn1=1
        for i in range(0, dimension):
            for dp in range(0,len(temp[i])):
                if ctr % 2 == 0:
                    lst[i].append(((rnd.random()-rnd.uniform(-5,10))/rn*rn1+temp[i][dp]))
                else:
                    lst[i].append(((rnd.random() - rnd.uniform(-2, 10)) / rn * rn1 + temp[i][dp]))
                #ctl+=1
                #label.append(divmod(ctl,centroids.shape[0]))
        for j in range(0,centroids.shape[0]):
            label.append(j+1)
        ctr+=1
    '''
    #t1=numpy.asarray(lst)
    t1=numpy.asarray(lst)
    t2= numpy.transpose(t1)
    k_mean=cluster.KMeans(centroids.shape[0],max_iter=1000)
    k_mean.fit(t2)
    dx=k_mean.predict(t2)
    d=dx.tolist()
    tx=[]
    tx.append(dx)
    for x in t1:
        tx.append((x-x.min())/(numpy.ptp(x)))#normalizing between [0,1]
    tx=numpy.asarray(tx)
    #t1=numpy.transpose(tx)
    lst1=tx.tolist()
    lst2=tx[1:].tolist()
    lst3=[]
    lstx=[]
    #highest value acceptable by the dimension
    for y1 in range(0,dimension):
        value=1
        lst2[y1]=[value]+lst2[y1]



    #label generation
    for y in range(0,dimension+1):
        if y==0:
            lst3.append('label')
        else:
            str= 'dim%x'%y
            lst3.append(str)

    #t20=numpy.asarray(lst3)
    lstx.append(lst3)
    t2=numpy.transpose(numpy.asarray(lst1))
    #numpy.savetxt("t13WL.csv",t20,delimiter=',')
    with open('t13WL.csv','w') as fd:

        a=csv.writer(fd,delimiter=',')
        a.writerows(lstx)
        a.writerows(t2)
    t3=numpy.transpose(numpy.asarray(lst2))
    numpy.savetxt("t13WL.csv",t2,delimiter=',')
    numpy.savetxt("t13data.csv",t3,delimiter=',')
    d1=pandas.read_csv('../RAN/t13.csv')
    parallel_coordinates(d1,'label')
    plt.show()
    plt.plot(tx[0],tx[1], 'ro')
    plt.show()
    '''
    #normalizing between 0 n 1
    lst=numpy.asarray(lst)
    for i in range(0,lst.shape[0]):
        temp[i] = numpy.divide((temp[i] - lst[i].min()), (lst[i].max() - lst[i].min()))
        lst[i]=numpy.divide((lst[i]-lst[i].min()),(lst[i].max()-lst[i].min()))

    data=numpy.asarray(lst.tolist()+[label]).transpose()
    pdata=pandas.DataFrame(data,columns=['Dimension-x','Dimension-y','labels'])
    fif,ax=plt.subplots()
    ax.set_ylim(-0.2, 1.2)
    ax.set_xlim(-0.2, 1.2)
    pdata.plot(ax=ax,kind='scatter',x='Dimension-x',y='Dimension-y',c='labels',colormap='gist_rainbow')
    print 'x'

c=numpy.asarray([[0,60],[5,0],[110,10],[50,35],[90,70]])
c1=numpy.asarray([[32,97],[28,83],[21,83],[17,58],[14,44],[11,31],[10,25],[10,14],[21,10],[32,14],[52,23],[59,29],[74,39],[88,54],[92,69],[98,88]])
c2=numpy.asarray([[25,98],[20,78],[18,59],[13,37],[5,17],[23,4],[45,10],[63,17],[83,42],[88,61],[95,83]])
c3=numpy.asarray([[41,97],[25,84],[8,76],[3,41],[13,26],[16,8],[50,26],[66,36],[73,52],[83,83],[66,96],[98,89]])
c4=numpy.asarray([[25,84],[8,76],[13,26],[16,8],[50,26],[66,36],[73,52],[83,83],[66,96],[98,89]])
c5=numpy.asarray([[16,90],[32,90],[48,90],[60,65],[50,54],[39, 41],[42,11],[58,10],[75,9]])
c6=numpy.asarray([[41,97],[25,84],[8,76],[3,41],[13,26],[16,8],[43,48],[57,54],[71,43]])
c7=numpy.asarray([[0,0],[0,20],[90,90],[0,90],[90,0]])
c8=numpy.asarray([[0,70],[90,90]])
generator(dimension=2,size=200,centroids=c7)
print "x"

