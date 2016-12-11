# -*- coding:utf-8 -*-
'''
Created on 2016-8-16
采用svg绘图
@author: Administrator
'''
from svgpathtools.path import Path, Line
import svgwrite

from com.mh.domain.plot.Basic import svgConvert
from com.mh.domain.plot.BoxPlot import BoxPlot
import pandas as pd


def getData(_path):
    df = pd.read_table(_path) 
    return df
    
def plotBox(lData,title='Distribution of qualities',outPathName='test'):
    _width=1024
    dwg = svgwrite.Drawing(outPathName+'.svg',profile='tiny',size=(_width,520))
    bp=BoxPlot(dwg)
    g=dwg.g()
    boxW=960
    boxH=450
    box=getPlotBox(dwg, boxW,boxH,9,45, 8, lData.shape[0], 'Position along reads', 'Quality', title)
    box.translate(40,20)
    g.add(box)
    span=(boxW*1.0)/lData.shape[0]
    path=Path()
    for i in range(lData.shape[0]):
        if i>0:
            path.append(Line(complex(40+(i-0.5)*span,boxH-float(lData.iloc[i-1][5]*10)+20),complex(40+(0.5+i)*span,boxH-float(lData.iloc[i][5]*10)+20)))
        Q1=boxH-float(lData.iloc[i][0]*10)+20
        Q2=boxH-float(lData.iloc[i][1]*10)+20
        Q3=boxH-float(lData.iloc[i][2]*10)+20
        _min=boxH-float(lData.iloc[i][3]*10)+20
        _max=boxH-float(lData.iloc[i][4]*10)+20
        g.add(bp.getBoxPlot(40+(0.5+i)*span, 0.5*span,Q1,Q2,Q3,_min,_max, '#FF9933'))
    g.add(dwg.path(d=path.d(),stroke_width=0.5,fill='none',stroke='red'))
    dwg.add(g)
    dwg.save()
    svgConvert(outPathName, outPathName)

#绘制盒子坐标轴
def getPlotBox(dwg,boxW,boxH,HL,maxH,WL,maxW,xLabel,yLabel,title):
    g=dwg.g()
    g.add(dwg.rect((0,0),(boxW,boxH),stroke='#000',stroke_width=1,fill='none'))
    for i in range(HL+1):
        L=i*boxH*1.0/HL
        g.add(dwg.line((0,L),(0+5,L),stroke='#000',stroke_width=2))
        g.add(dwg.line((boxW,L),(boxW-5,L),stroke='#000',stroke_width=2))
        g.add(dwg.text(str(maxH-i*maxH/HL), insert=(-3,L+5),font_family='Times New Roman',font_size=8,text_anchor='end'))
        g.add(dwg.line((5,L),(boxW-5,L),stroke='#999',stroke_dasharray='3,3',stroke_width=1))
    for i in range(WL+1):
        L=i*boxW*1.0/WL
        g.add(dwg.line((L,boxH-5),(L,boxH),stroke='#000',stroke_width=2))
        g.add(dwg.line((L,0),(L,5),stroke='#000',stroke_width=2))
        g.add(dwg.line((L,5),(L,boxH-5),stroke='#999999',stroke_dasharray='3,3',stroke_width=1))
        g.add(dwg.text(str(i*maxW/WL), insert=(L,boxH+15),font_family='Times New Roman',font_size=8,text_anchor='middle'))
    g.add(dwg.text(xLabel, insert=(boxW/2.0,boxH+30),font_family='Times New Roman',font_size=10,text_anchor='middle'))
    g.add(dwg.text(title, insert=(boxW/2.0,-5),font_family='Times New Roman',font_size=15,text_anchor='middle'))
    txt=dwg.text(yLabel, insert=(-10, boxH/2.0),text_anchor='end',font_family='Times New Roman',font_size=10)
    txt.rotate(-90,(-20, boxH/2.0))
    g.add(txt)    
    return g

def plotBasePercentageLine(data,title='Base percentage composition along reads',outPathName='test'):
    _width=1024
    startX=40
    startY=20
    boxW=960
    boxH=400
    _list=data[0]
    print data[1]
    _max=100
    sc=boxH/_max
    dwg = svgwrite.Drawing(outPathName+'.svg',profile='tiny',size=(_width,460))
    boxG=getPlotBox(dwg, boxW, boxH, 8, _max, 8, len(_list),'Position along reads', 'Percent(%)', title)
    boxG.translate(startX,startY)
    g=dwg.g()
    g.add(boxG)
    pathA=Path()
    pathT=Path()
    pathC=Path()
    pathG=Path()
    pathN=Path()
    span=(boxW*1.0)/len(_list)
    for i in range(1,len(_list)):
        x0=(i-1)*span+startX
        x1=(i)*span+startX
        pathA.append(Line(complex(x0,startY+boxH-sc*_list[i-1][0]),complex(x1,startY+boxH-sc*_list[i][0])))
        pathT.append(Line(complex(x0,startY+boxH-sc*_list[i-1][1]),complex(x1,startY+boxH-sc*_list[i][1])))
        pathC.append(Line(complex(x0,startY+boxH-sc*_list[i-1][2]),complex(x1,startY+boxH-sc*_list[i][2])))
        pathG.append(Line(complex(x0,startY+boxH-sc*_list[i-1][3]),complex(x1,startY+boxH-sc*_list[i][3])))
        pathN.append(Line(complex(x0,startY+boxH-sc*_list[i-1][4]),complex(x1,startY+boxH-sc*_list[i][4])))
    g.add(dwg.path(d=pathA.d(),stroke_width=1.5,fill='none',stroke='red'))
    g.add(dwg.path(d=pathT.d(),stroke_width=1.5,fill='none',stroke='green'))
    g.add(dwg.path(d=pathC.d(),stroke_width=1.5,fill='none',stroke='#660099'))
    g.add(dwg.path(d=pathG.d(),stroke_width=1.5,fill='none',stroke='blue'))
    g.add(dwg.path(d=pathN.d(),stroke_width=1.5,fill='none',stroke='yellow'))
    g.add(dwg.line((startX+boxW-50,startY+20),(startX+boxW-10,startY+20),stroke_width=2,fill='none',stroke='red'))
    g.add(dwg.text('A', insert=(startX+boxW-55,startY+25),font_family='Times New Roman',font_size=15,text_anchor='end'))
    g.add(dwg.text('T', insert=(startX+boxW-55,startY+45),font_family='Times New Roman',font_size=15,text_anchor='end'))
    g.add(dwg.text('C', insert=(startX+boxW-55,startY+65),font_family='Times New Roman',font_size=15,text_anchor='end'))
    g.add(dwg.text('G', insert=(startX+boxW-55,startY+85),font_family='Times New Roman',font_size=15,text_anchor='end'))
    g.add(dwg.text('N', insert=(startX+boxW-55,startY+105),font_family='Times New Roman',font_size=15,text_anchor='end'))
    g.add(dwg.line((startX+boxW-50,startY+40),(startX+boxW-10,startY+40),stroke_width=2,fill='none',stroke='green'))
    g.add(dwg.line((startX+boxW-50,startY+60),(startX+boxW-10,startY+60),stroke_width=2,fill='none',stroke='#660099'))
    g.add(dwg.line((startX+boxW-50,startY+80),(startX+boxW-10,startY+80),stroke_width=2,fill='none',stroke='blue'))
    g.add(dwg.line((startX+boxW-50,startY+100),(startX+boxW-10,startY+100),stroke_width=2,fill='none',stroke='yellow'))
    
    dwg.add(g)
    dwg.save()
    svgConvert(outPathName, outPathName)
def getBasePercent(data1):
    header=['A_Count','C_Count','G_Count','T_Count','N_Count','Max_count']
    base1=data1[header]
    _dt=[]
    _max=0
    for i in range(base1.shape[0]):
        _A=int(base1.iloc[i][0])
        _C=int(base1.iloc[i][1])
        _G=int(base1.iloc[i][2])
        _T=int(base1.iloc[i][3])
        _N=int(base1.iloc[i][4])
        num=(_A+_T+_C+_G+_N)/100.0
        _ls=[_A/num,_T/num,_C/num,_G/num,_N/num]
        if _max<max(_ls):
            _max=max(_ls)
        _dt.append((_A/num,_T/num,_C/num,_G/num,_N/num))
    return (_dt,_max)

def getBoxData(data):
    return data[['Q1','med','Q3','lW','rW','mean']]

def plotQCSummary(path1,path2,outPath):
    df1=getData(path1)
    if path2:
        df2=getData(path2)
        df=pd.concat([df1,df2])
    else:
        df=df1
    plotBox(getBoxData(df),'Distribution of qualities',outPath+'_qual')
    plotBasePercentageLine(getBasePercent(df),'Base percentage composition along reads',outPath+'_base')

if __name__ == '__main__':
    folder='E:/Work/MH/RNASeq'
    plotQCSummary(folder+'/SRR2040568_1.stats',folder+'/SRR2040568_2.stats', folder+'/SRR2040568')

