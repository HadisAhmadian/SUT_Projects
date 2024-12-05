import numpy as np
from module import Module


class SoftmaxCrossentropy(Module):
    def __init__(self, name):
        super(SoftmaxCrossentropy, self).__init__(name)

    def forward(self, x, **kwargs):
        y = kwargs.pop('y', None)
        probs=[]
        for r in x:
            probs.append(np.exp(r-max(r))/sum(np.exp(r - max(r))))
        probs=np.array(probs)
        
        loss=0
        for i in range(len(y)):
            loss-=np.log(probs[i][y[i]])
        loss=loss/len(x)
        
        self.cache=probs,y

        # todo: implement the forward propagation for probs and compute cross entropy loss
        # NOTE: implement a numerically stable version.If you are not careful here
        # it is easy to run into numeric instability!
   
        return loss, probs

    def backward(self, dout=0):
        dx = self.cache[0]
        y=self.cache[1]
        y_one_hot = np.zeros((y.size, len(dx[0])))
        y_one_hot[np.arange(y.size),y] = 1

        dx-=y_one_hot
        dx/=len(y)
        
        return dx
