import numpy as np
from module import Module


class Sigmoid(Module):
    def __init__(self, name):
        super(Sigmoid, self).__init__(name)

    def forward(self, x, **kwargs):
        out=[[0]*len(x[0]) for i in range(len(x))]
        for i in range(len(out)):
            for j in range(len(out[i])):
                out[i][j]=1/(1+np.exp(-x[i][j]))
        out=np.array(out)
        self.cache=x
        return out
        # todo: implement the forward propagation for Sigmoid module.
 

    def backward(self, dout):
        """
        dout: gradients of Loss w.r.t. this layer's output.
        dx: gradients of Loss w.r.t. this layer's input.
        """
        dx = self.cache
        for i in range(len(dx)):
            for j in range(len(dx[0])):
                e=np.exp(dx[i][j])
                dx[i][j]=e/((1+e)**2)
        # todo: implement the backward propagation for Sigmoid module.
        dx=dx*dout
        return dx
