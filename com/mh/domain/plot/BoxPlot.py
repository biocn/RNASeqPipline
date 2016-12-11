# -*- coding:utf-8 -*-
#!/usr/bin/python
'''
Created on 2016��12��9��

@author: Administrator
'''
class BoxPlot(object):
    def __init__(self,dwg):
        self.dwg=dwg
    def getBoxPlot(self,x1,r,Q1,Q2,Q3,_min,_max,fillColor):
        g=self.dwg.g()
        g.add(self.dwg.polygon([(x1-r,Q2),(x1+r,Q2),(x1+r,Q1),(x1-r,Q1),(x1-r,Q2)],fill=fillColor,stroke='none'))
        g.add(self.dwg.polygon([(x1-r,Q2),(x1+r,Q2),(x1+r,Q3),(x1-r,Q3),(x1-r,Q2)],fill=fillColor,stroke='none'))
        g.add(self.dwg.line((x1,Q1),(x1,_min),stroke_width=1,stroke='#000'))
        g.add(self.dwg.line((x1,Q3),(x1,_max),stroke_width=1,stroke='#000'))
        g.add(self.dwg.line((x1-0.8*r,_min),(x1+0.8*r,_min),stroke_width=1,stroke='#000'))
        g.add(self.dwg.line((x1-0.8*r,_max),(x1+0.8*r,_max),stroke_width=1,stroke='#000'))
        g.add(self.dwg.line((x1-0.8*r,Q2),(x1+0.8*r,Q2),stroke_width=1,stroke='#990033'))
#         g.add(self.dwg.line((x1-0.8*r,_max),(x1+0.8*r,_max),stroke_width=1,stroke='#000'))
        
        return g
