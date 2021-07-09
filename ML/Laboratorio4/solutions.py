import numpy as np

"""
Debería resolver esta práctica sin agregar más librerías externas
"""

def NotImplemented_message():
    print('###################################')
    print('Tienen que implementar esta función')
    print('###################################')
    return np.array([1, 1])

def densa_forward(X, W, b):
    return np.dot(X,W)+b

def MSE(X_pred, X_true):
    MSE=(((X_pred[0][0]-X_true[0][0])**2)+
        ((X_pred[0][1]-X_true[0][1])**2)+
        ((X_pred[0][2]-X_true[0][2])**2))/3
    return MSE

def MSE_grad(X_true, X_pred):
    MSE_grad=(sum(((X_pred-X_true))*X_pred.T)*2)/3
    return MSE_grad

def sigmoid(X):
    return 1/(1+(np.exp((-X))))

def sigmoid_jac(Xin):
    sigmoid = 1/(1+(np.exp((-Xin))))
    sigmoid_jac = sigmoid*(1-sigmoid)
    sigmoid_jac = np.diag(sigmoid_jac.reshape(-1))
    return sigmoid_jac

def softmax(z):
    a,b,c = np.split(z[0], 3)
    P_1= np.exp(a) / (np.exp(a) + np.exp(b) + np.exp(c))
    P_2= np.exp(b) / (np.exp(a) + np.exp(b) + np.exp(c))
    P_3= np.exp(c) / (np.exp(a) + np.exp(b) + np.exp(c))
    softmax= np.array([P_1,P_2,P_3]).T
    return softmax

def softmax_jac(Xin):
    # Primera matriz
    softmax_out = softmax(Xin)
    Primera_Matriz = np.diag(softmax_out.reshape(-1))
    # Segunda matriz
    Segunda_Matriz = softmax_out.T.dot(softmax_out)
    softmax_jac = Primera_Matriz - Segunda_Matriz
    return softmax_jac

def forward(X, P_true, weights):
    D1_out = np.dot(X,weights[0]) + weights[1]
    A1_out = 1/(1+(np.exp((-D1_out))))
    D2_out = np.dot(A1_out, weights[2]) + weights[3]
    A2_out = 1/(1+(np.exp((-D2_out))))
    D3_out = np.dot(A2_out, weights[4]) + weights[5]
    
    a,b,c = np.split(D3_out[0], 3)
    P_1= np.exp(a) / (np.exp(a) + np.exp(b) + np.exp(c))
    P_2= np.exp(b) / (np.exp(a) + np.exp(b) + np.exp(c))
    P_3= np.exp(c) / (np.exp(a) + np.exp(b) + np.exp(c))
    P_est= np.array([P_1,P_2,P_3]).T
    
    mse=(((P_est[0][0]-P_true[0][0])**2)+
         ((P_est[0][1]-P_true[0][1])**2)+
         ((P_est[0][2]-P_true[0][2])**2))/3

    return P_est, mse, X, A1_out, A2_out

def get_gradients(X, P_true, weights):
    error_D3 = softmax_jac.dot(MSE_grad)
    
    return NotImplemented_message()     ### este falta