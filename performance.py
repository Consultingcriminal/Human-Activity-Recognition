#from mlxtend.plotting import plot_confusion_matrix
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
import numpy as np


def performance_metrics(model,history,epochs,X_test,y_test):
    epoch_range=range(1,epochs+1)
    plt.plot(epoch_range,history.history['accuracy'])
    plt.plot(epoch_range,history.history['val_accuracy'])
    plt.title('Model Accuracy')
    plt.ylabel('Accuracy')
    plt.xlabel('Epochs')
    plt.legend(['Train','Val'],loc='upper left')
    plt.show()
    
    plt.plot(epoch_range,history.history['loss'])
    plt.plot(epoch_range,history.history['val_loss'])
    plt.title('Model Loss')
    plt.ylabel('Loss')
    plt.xlabel('Epochs')
    plt.legend(['Train','Val'],loc='upper left')
    plt.show()
    
    
    #y_pred=np.argmax(model.predict_classes(X_test))
    #mat=confusion_matrix(y_test,y_pred)
    #plot_confusion_matrix(conf_mat=mat,class_names=['Downstairs','Jogging','Sitting','Standing','Upstairs','Walking'],show_normed=True,figsize=(7,7))

if __name__=='__main__':
    performance_metrics(model,history,epochs,X_test,y_test)
    