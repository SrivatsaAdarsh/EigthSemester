def xorneuron():
    X1 = [0, 0, 1, 1]
    X2 = [0, 1, 0, 1]
    Z = [0, 1, 1, 0]  # desired output
    W = [0.2, 0.3]  # Initial Weights
    r = 0.3   # learning rate
    b = 0.1  # bias
    lb = 0.05  # learning bias (Adaptive rate)
    epochs = 25 # No of iterations

    print('x y z  w1  w2 Y d w\'   w\"', end='\n')
    print('============================', end='\n')

    for iter in range(epochs):
        for i in range(4):
            print(X1[i], X2[i], Z[i], W[0], W[1], end=' ')
            Y = W[0]*X1[i] + W[1]*X2[i] + b
            if (Y >= 0.5 and Y <= 1.5):   # Output HIGH for 0.5 < f(x,y) < 1.5
                Y = 1
            else:
                Y = 0
            deltW = Z[i] - Y
            print(Y, deltW, end=' ')

            if (deltW > 1):  # Adaptive Learning Rate
                r = r + lb
            else:
                r = r - lb

            W[0] = round(W[0] + deltW * r * X1[i], 1)  # Weight Updation
            W[1] = round(W[1] + deltW * r * X2[i], 1)

            print(W[0], W[1], end='\n')


xorneuron()
