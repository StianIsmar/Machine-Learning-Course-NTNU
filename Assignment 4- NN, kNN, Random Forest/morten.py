#Set initial guess
W1 = np.random.randn(nodes, X.shape[1])
b1 = np.zeros((nodes,1))
W2 = np.random.randn(1, nodes)
b2 = np.zeros((1, X.shape[0]))
alpha = 0.1

for j in range(iterations):

    for i in range(X.shape[0]):
        x = np.array([X[i]])
        y = np.array([Y[i]])
        x = x.T

        #Forward Propagation
        #Layer 1
        z1 = np.dot(W1, x)
        a1 = sigmoid(z1)
        #Layer 2
        z2 = np.dot(W2, a1)
        a2 = sigmoid(z2)

        #Back Propagation
        #Layer 2
        dz2 = np.multiply(-(y-a2), np.multiply((1-a2), a2))
        dW2 = np.dot(dz2, a1.T)
        #Layer 1
        dz1 = np.multiply(np.dot(W2.T, dz2), np.multiply((1-a1), a1))
        dW1 = np.dot(dz1, x.T)

        #Update W
        W2 = W2 - alpha*dW2
        W1 = W1 - alpha*dW1

        #Loss
        L = np.square(a2-y)/2
        if (j == iterations-1):
            print(a2, y, "\n", L, "\n")


'''
print("L: ", L)
print("dz1 is: \n", dz1, "\nshape of dz1: ", dz1.shape, "\n")
print("dW1 is: \n", dW1, "\nshape of dW1: ", dW1.shape, "\n")
print("dz2 is: \n", dz2, "\nshape of dz2: ", dz2.shape, "\n")
print("dW2 is: \n", dW2, "\nshape of dW2: ", dW2.shape, "\n")
print("W2 is: \n", W2, "\nshape of W2: ", W2.shape, "\n")
print("z1 is: \n", z1, "\nshape of z1: ", z1.shape, "\n")
print("a1 is: \n", a1, "\nshape of a1: ", a1.shape, "\n")
print("z2 is: \n", z2, "\nshape of z2: ", z2.shape, "\n")
print("a2 is: \n", a2, "\nshape of a2: ", a2.shape, "\n")
print("x is: \n", x, "\nshape of x: ", x.shape, "\n")
print("y is: \n", y, "\nshape of y: ", y.shape, "\n")
print("W1 is: \n", W1, "\nshape of W1: ", W1.shape, "\n")
'''
