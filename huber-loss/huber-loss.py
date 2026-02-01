import numpy as np

def huber_loss(y_true, y_pred, delta=1.0):
    """
    Compute Huber Loss for regression.
    """
    # Write code here
    l=[]
    e = (np.array(y_pred) - np.array(y_true)).tolist()
    for i in range(len(y_pred)):
        if(np.abs(e[i])<=delta):
            l.append(0.5*e[i]**2)
        else:
            l.append(delta*(np.abs(e[i]) - 0.5*delta))
    fe = sum(l)/len(l)
    return fe 