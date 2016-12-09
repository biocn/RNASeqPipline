'''
Created on 2016-7-4

@author: Administrator
'''
def readGtf(_path):
    f=open(_path,'r')
    line=f.readline()
    while line:
        if line.find('#')!=0:
            cols=line.rstrip().lstrip('\n')
            
        line=f.readline()
    f.close()


if __name__ == '__main__':
    folder='E:/Work/MH/MH-B16061603/GDR0697-4'