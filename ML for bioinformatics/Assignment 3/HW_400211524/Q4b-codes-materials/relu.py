import numpy as np
from module import Module


class ReLU(Module):
    def __init__(self, name):
        super(ReLU, self).__init__(name)

    def forward(self, x, **kwargs):
        out=[[0]*len(x[0]) for i in range(len(x))]
        for i in range(len(out)):
            for j in range(len(out[i])):
                out[i][j]=max(0,x[i][j])
        out=np.array(out)
        self.cache=x
        return out

    def backward(self, dout):
        """
        dout: gradients of Loss w.r.t. this layer's output.
        dx: gradients of Loss w.r.t. this layer's input.
        """
        dx = self.cache
        for i in range(len(dx)):
            for j in range(len(dx[0])):
                if dx[i][j]>0:
                    dx[i][j]=1
                else:
                    dx[i][j]=0
        # todo: implement the backward propagation for ReLU module.
        dx=dx*dout
        return dx
