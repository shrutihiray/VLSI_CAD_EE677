import numpy as np
n  = 3
fStr = '{0:0'+str(n)+'d}' # format String
def mat(T,n):
    TnU = np.concatenate([T,np.zeros(T.shape)],axis =1)
    TnL = np.concatenate([T,T], axis=1)
    Tn = np.concatenate([TnU,TnL])
    if(n!=2):
        return mat(Tn,n-1)
    return Tn

T1 = np.array([[1,0],[1,1]])
Tn = mat(T1,3)
print(Tn)
