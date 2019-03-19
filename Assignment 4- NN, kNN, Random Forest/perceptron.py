import numpy as np
class perceptron:
    def __init__(self, x=0, y=0):
        print("constructor")

    def do_something(self):
        print("Doing something")
        return 2
p1 = perceptron()
a = p1.do_something()
print(a)


class nn:
    input_nodes = 0
    hidden_nodes = 0
    output_nodes = 0
    def __init__(self, input_nodes, hidden_nodes, output_nodes):
        self.input_nodes = input_nodes # The number of features!
        self.hidden_nodes = hidden_nodes
        self.output_nodes = output_nodes

        self.weights_ih = np.random.rand(self.hidden_nodes, self.input_nodes + 1)
        self.weights_ho = np.random.rand(self.output_nodes, self.hidden_nodes + 1)

        self.bias_h = np.empty([self.hidden_nodes, 1])
        print("bias_h",self.bias_h)
        self.bias_o = np.empty([self.output_nodes, 1])
        # np.random.randint(low=1, high=100, size=4)


    def sigmoid(self,x):
        res = 1 / (1 + np.exp(-x))

    def feedforward(self, input_sample):
        hidden = np.dot(self.weights_ih, input_sample)
        print("dot:",hidden)

        hidden = np.add(hidden.T,self.bias_h)
        print(hidden)

        sig = lambda t: self.sigmoid(t)
        sig(hidden)

        return 0
            # return code

n1 = nn(2,2,1)
n1.feedforward([1,2,3])

# Store the weights in a matrix:
