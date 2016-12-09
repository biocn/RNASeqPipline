# -*- coding:utf-8 -*-
'''
Created on 2016-8-16

@author: Administrator
'''
import numpy as np
import matplotlib.pyplot as plt

import pandas as pd


def getData(_path):
    df = pd.read_table(_path) 
    return df


def boxData(q1,q2,q3,l,h):
    spread1 =[l]*10
    spread2 = [q1]*15
    spread3 = [q2]*25 
    spread4 = [q3]*25 
    spread5 = [h]*16  
    spread6 = [h+5]*9 
    data = np.concatenate((spread1,spread2,spread3,spread4,spread5,spread6), 0)
    return data
def plotBox(lData,xLabel=None):
    # basic plot
#     print np.random.rand(50)
    _list=[]
    for i in range(lData.shape[0]):
        _list.append(boxData(lData.iloc[i][0],lData.iloc[i][1],lData.iloc[i][2],lData.iloc[i][3],lData.iloc[i][4]))
#     plt.boxplot([boxData(31,31,34,27,34)],0,'')
    plt.boxplot(_list, 0, '')
    plt.show()
#     plt.boxplot(data)
    pass
def testPlot():
    N = 5
    menMeans = (20, 35, 30, 35, 27)
    menStd =   (2, 3, 4, 1, 2)
    
    ind = np.arange(N)  # the x locations for the groups
    width = 0.35       # the width of the bars
    
    fig, ax = plt.subplots()
    rects1 = ax.bar(ind, menMeans, width, color='r', yerr=menStd)
    
    womenMeans = (25, 32, 34, 20, 25)
    womenStd =   (3, 5, 2, 3, 3)
    rects2 = ax.bar(ind+width, womenMeans, width, color='y', yerr=womenStd)
    
    # add some
    ax.set_ylabel('Scores')
    ax.set_title('Scores by group and gender')
    ax.set_xticks(ind+width)
    ax.set_xticklabels( ('G1', 'G2', 'G3', 'G4', 'G5') )
    
    ax.legend( (rects1[0], rects2[0]), ('Men', 'Women') )
    
    def autolabel(rects):
        # attach some text labels
        for rect in rects:
            height = rect.get_height()
            ax.text(rect.get_x()+rect.get_width()/2., 1.05*height, '%d'%int(height),
                    ha='center', va='bottom')
    
    autolabel(rects1)
    autolabel(rects2)
    
    plt.show()
if __name__ == '__main__':
    folder='E:/Work/MH/RNASeq'
    df=getData(folder+'/SRR2040568_1.stats')
#     testPlot()
    plotBox(df[['Q1','med','Q3','lW','rW']])



