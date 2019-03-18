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
    def __init__(self, numI, numH, numO):
        self.input_nodes = numI # The number of features!
        self.hiddes_nodes = numH
        self.output_nodes = numO
n1 = nn(3,2,1)
