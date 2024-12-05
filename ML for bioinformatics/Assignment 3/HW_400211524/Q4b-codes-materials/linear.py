import numpy as np
from module import Module


class Linear(Module):
    def __init__(self, name, input_dim, output_dim, l2_coef=.0):
        super(Linear, self).__init__(name)

        self.l2_coef = l2_coef  # coefficient of l2 regularization.

        self.W = np.random.randn(input_dim, output_dim)  # weights of the layer.
        self.b = np.random.randn(output_dim, )  # biases of the layer.
        self.dW = None  # gradients of loss w.r.t. the weights.
        self.db = None  # gradients of loss w.r.t. the biases.

    def forward(self, x, **kwargs):
        
        out = np.dot(x,self.W)+self.b
        # todo: implement the forward propagation for Linear module.
        self.cache=x
        return out

    def backward(self, dout):
        """
        dout: gradients of Loss w.r.t. this layer's output.
        dx: gradients of Loss w.r.t. this layer's input.
        """
        self.db=sum(dout)
        self.dW=np.dot(self.cache.T,dout)+2*self.l2_coef*self.W
        dx = np.dot(dout,self.W.T)
        # todo: implement the backward propagation for Linear module.
        # don't forget to update self.dW and self.db.
      
        return dx
