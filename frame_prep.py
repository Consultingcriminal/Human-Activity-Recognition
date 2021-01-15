import numpy as np
import pandas as pd 
import scipy.stats as stats

def get_frames(df,frame_size,hop_size):
    N_FEATURES=3
    
    frames=[]
    labels=[]
    
    for i in range(0,len(df)-frame_size,hop_size):
        x=df['X'].values[i:i+frame_size]
        y=df['Y'].values[i:i+frame_size]
        z=df['Z'].values[i:i+frame_size]
        
        label=stats.mode(df['label'][i:i+frame_size])[0][0]
        frames.append([x,y,z])
        labels.append(label)
    frames=np.asarray(frames).reshape(-1,frame_size,N_FEATURES)
    labels=np.asarray(labels)
    
    return frames,labels






