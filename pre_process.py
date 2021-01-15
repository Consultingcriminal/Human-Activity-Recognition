import numpy as np
import pandas as pd

#Importing a preprocessing a file

def pre_process():
    file=open('WISDM_ar_v1.1_raw.txt')
    lines=file.readlines()

    processedList= []

    for i,line in enumerate(lines):
        try:
            line=line.split(',')
            last=line[5].split(';')[0]
            last=last.strip()
    
            if last=='':
                break
            temp=[line[0],line[1],line[2],line[3],line[4],last]
            processedList.append(temp)
        except:
            print('Error in line:{}'.format(i))
    return processedList


def const_df(processedList):
    columns=['user','Activity','time','X','Y','Z']
    data=pd.DataFrame(processedList,columns=columns)
    data['X']=data['X'].astype('float')
    data['Y']=data['Y'].astype('float')
    data['Z']=data['Z'].astype('float')
    return data    
