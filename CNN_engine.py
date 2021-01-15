from pre_process import pre_process,const_df
from data_prep import data_const
from frame_prep import get_frames
from CNNmodel import CNN_input,model
from performance import performance_metrics
import os
import tensorflow as tf


if __name__=='__main__':
    fs=20
    frame_size=fs*4
    hop_size=fs*2
    epochs=150


    os.environ['TF_FORCE_GPU_ALLOW_GROWTH'] = 'true'

    preprocessed_list=pre_process()
    df=const_df(preprocessed_list)
    scaled_X=data_const(df)
    X,y=get_frames(scaled_X,frame_size,hop_size)
    print(X.shape)
    X_train,X_test,y_train,y_test=CNN_input(X,y)
    history,model=model(X_train,X_test,y_train,y_test,epochs)
    performance_metrics(model,history,epochs,X_test,y_test)
