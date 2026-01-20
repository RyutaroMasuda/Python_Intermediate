import random
from nn_utils import transpose,matmul,add_bias,relu

class Module:
    """
    Base class for all neural network modules
    
    child class: Linear,ReLU
    """

    def __init__(self):
        self._modules = {}

    def forward(self, x):
        raise NotImplementedError

    def __call__(self, x):
        return self.forward(x)

    def add_module(self, name, module):
        self._modules[name] = module
        setattr(self, name, module)

class Linear(Module):
    """
    Applies an affine linear transformation to the incoming data: math : "y = xW^T + b" 
    args:
        y = x @ W^T + b
        x: (batch, in_dim)
        W: (out_dim, in_dim)
        b: (out_dim,)
    """
    def __init__(self, in_dim, out_dim, scale=0.1):
        super().__init__()
        self.in_dim = in_dim
        self.out_dim = out_dim
        self.scale = scale
        self.weight, self.bias = self.init_linear()

    def init_linear(self):
        # W: (out,in), b: (out,)
        W = [[random.uniform(-self.scale, self.scale) for _ in range(self.in_dim)]
            for _ in range(self.out_dim)]
        b = [random.uniform(-self.scale, self.scale) for _ in range(self.out_dim)]
        return W, b

    def forward(self, x):
        WT = transpose(self.weight)  # (in,out)
        y = matmul(x, WT)               # (batch,out)
        y = add_bias(y, self.bias)
        return y

class ReLU(Module):
    """
    ReLu Layer which is a activation function.
    """
    def forward(self, x):
        return relu(x)

class Sequential(Module):
    """
    A container module that applies layers sequentially.

    Example:
        model = Sequential(
            Linear(3,4),
            Relu(),
            Linear(4,2)
        )
        y = model(x)
        
        Input shape:
        x: (batch, in_dim) as list[list[float]]
        Output shape:
        y: (batch, out_dim) as list[list[float]]
    """
    def __init__(self, *layers):
        super().__init__()
        self.layers = list(layers)
        for i, layer in enumerate(layers):
            self.add_module(str(i), layer)

    def forward(self, x):
        for layer in self.layers:
            x = layer(x)
        return x

def main():
    random.seed(0)

    x = [
        [1.0,  2.0, -1.0],
        [0.5, -0.5,  3.0],
    ]

    model = Sequential(
        Linear(3, 4),
        ReLU(),
        Linear(4, 2),
    )

    y = model(x)
    print("y =", y)

if __name__ == "__main__":
    main()