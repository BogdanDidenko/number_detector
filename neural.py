# import matplotlib.pyplot as plt
# import mpl_toolkits.mplot3d as p3
import numpy as np
import json, codecs
file_path = "net.npy"
res = np.load(file_path)
import sys

input = sys.argv[1]
#input = '{"data":[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,50,50,50,50,0,50,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,50,0,0,0,0,0,0,50,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,50,0,0,0,0,0,0,0,50,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,50,0,0,0,0,0,0,0,0,0,50,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,50,0,0,0,0,0,0,0,0,0,0,50,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,50,50,0,0,0,0,0,0,0,0,50,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,50,50,0,0,0,0,0,0,0,0,0,50,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,50,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,50,50,50,50,50,50,50,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]}'
#input = json.dumps(input)

input = json.loads(input)
#import tensorflow as tf
# from tensorflow.examples.tutorials.mnist import input_data
# mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)


def sigmoid(sum):
    return 1 / (1 + np.exp(-sum))

def sigmoid_derivate(sum):
    return sigmoid(sum) * (1 - sigmoid(sum))

def summator(y_hat, y):
    return 0.5 * np.mean((y_hat-y)**2)

def summator_derivate(y_hat, y):
    return y_hat - y

class Network:
    def __init__(self, shape, rate, batch_size):
        self.rate = rate
        self.l_count = l = len(shape)
        self.W, self.z , self.a, self.errors, self.b = [None] * l, [None] * l, [None] * l, [None] * l, [None] * l
        for l in range(0, self.l_count):
            self.W[l] = np.random.uniform(0, 0.01, shape[l])
            self.b[l] = np.random.uniform(0, 0.01, (shape[l][0], 1))

            self.z[l] = np.zeros((batch_size, shape[l][0]))
            self.a[l] = np.zeros((batch_size, shape[l][0]))
            self.errors[l] = np.zeros((batch_size, shape[l][0]))

    def activation(self, sum):
        return sigmoid(sum)

    def summatorL(self, x, W, b):
        return x.dot(W.T) + b.T

    def forwardL(self, x, l):
        self.z[l] = self.summatorL(x, self.W[l], self.b[l])
        self.a[l] = self.activation(self.z[l])
        return self.a[l]

    def forwardProp(self, x):
        _x = x
        for l in range(0, self.l_count):
            _x = self.forwardL(_x, l)
        return _x

    def J(self, x, y):
        _y = self.forwardProp(x)
        return summator(_y, y), _y, y

    def updateW(self, l, outputs):
        self.W[l] -= (self.rate * (self.errors[l].T.dot(outputs))) / 100
        self.b[l] -= self.rate * np.reshape(np.mean(self.errors[l], axis=0), (-1, 1))

    def SGD(self, x, y):
        l = self.l_count - 1
        self.errors[l] = summator_derivate(self.a[l], y) * sigmoid_derivate(self.z[l])
        for l in range(self.l_count -1, 0, -1):
            self.errors[l - 1] = self.errors[l].dot(self.W[l]) * sigmoid_derivate(self.z[l - 1])
            self.updateW(l, self.a[l-1])
        self.updateW(0, x)

np.random.seed(42)
batch_size = 100
#print( np.reshape(np.mean( [[1, 2],[2, 3],[3, 4]], axis=0), (-1, 1) ))
shape = [[42, 784],[10, 42]]
net = Network(shape, 0.5, batch_size)
net.W = res[0]
net.b = res[1]
x = np.array([input['data']]);

res = net.forwardProp(x)
res = json.dumps(res.tolist())
print(res)
# for _ in range(11500):
#     batch_xs, batch_ys = mnist.train.next_batch(batch_size)
#     res, _y, y = net.J(batch_xs, batch_ys)
#     net.SGD(batch_xs, batch_ys)
#     #print(res)
#
# file_path = "net" ## your path variable
# np.save(file_path, [net.W, net.b])
#json.dump(np.array([net.W, net.b]).tolist(), codecs.open(file_path, 'w', encoding='utf-8'), separators=(',', ':'), sort_keys=True, indent=4)
# batch_xs, batch_ys = mnist.validation.next_batch(batch_size)
# for _ in range(100):
#     res, _y, y = net.J(np.reshape(batch_xs[_], (1, -1)), np.reshape(batch_ys[_], (1, -1)))
#     print('_y = ', _y )
#     print(' y = ', y)
#     print('----------')


# shape = [[2,2], [1,2]]
# x = np.array([[[1],[1]], [[1],[0]], [[0],[1]], [[0],[0]]])
# y = np.array([[0], [1], [1], [0]])
# net = Network(shape, 10)
# error = 0
# for i in range(0, 1000):
#     for l in range(0, x.shape[0]):
#         error += net.J(x[l], y[l])
#         net.SGD(x[l], y[l])
#     #print(error)
#     error = 0
#print(net.W)