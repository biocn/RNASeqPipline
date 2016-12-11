# -*- coding:utf-8 -*-
#!/usr/bin/python
'''
Created on 2016��12��2��

@author: Administrator
'''
from svg2rlg import svg2rlg
from reportlab.graphics import renderPDF, renderPM


_barMaxWidth=20
_barMinWidth=20

_BasicColors=["#E64B35","#4DBBD5","#00A087","#3C5488","#F39B7F","#8491B4","#91D1C2","#DC0000","#7E6148"]

def svgConvert(inPathFileName,outPathFileName,JPG=True,PNG=None):
    drawing = svg2rlg(inPathFileName+'.svg')
    renderPDF.drawToFile(drawing, outPathFileName+".pdf")
    if JPG:
        renderPM.drawToFile(drawing, outPathFileName+".jpg",'JPG')
    if PNG:
        renderPM.drawToFile(drawing, outPathFileName+".png",'PNG')

if __name__ == '__main__':
    pass




