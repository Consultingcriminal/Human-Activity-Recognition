import pandas as pd 
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler

def data_const(df):
    df1=df.drop(['user','time'],axis=1).copy()
    walking=df1[df1['Activity']=='Walking'].head(3555*5).copy()
    jogging=df1[df1['Activity']=='Jogging'].head(3555*5).copy()
    upstairs=df1[df1['Activity']=='Upstairs'].head(3555*5).copy()
    downstairs=df1[df1['Activity']=='Downstairs'].head(3555*5).copy()
    sitting=df1[df1['Activity']=='Sitting'].head(4599).copy()
    standing=df1[df1['Activity']=='Standing'].head(3555).copy()
    balanced_data=pd.DataFrame()
    balanced_data=balanced_data.append([walking,jogging,upstairs,downstairs,sitting,standing])
    
    #label_encoding the target

    lb=LabelEncoder()
    balanced_data['label']=lb.fit_transform(balanced_data['Activity'])

    #Standardizing the Data

    X=balanced_data[['X','Y','Z']]
    y=balanced_data[['label']]
    sc=StandardScaler()
    X=sc.fit_transform(X)
    scaled_X=pd.DataFrame(data=X,columns=['X','Y','Z'])
    scaled_X['label']=y.values
    return scaled_X



