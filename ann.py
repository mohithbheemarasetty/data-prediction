inputs = [1, 1, 1, 0, 0, 0, 0], [1, 0, 0, 1, 0, 1, 1], [1, 1, 0, 0, 0, 1, 0], \
         [1, 1, 0, 1, 0, 1, 0], [1, 0, 1, 0, 0, 1, 1], [1, 1, 1, 0, 0, 1, 0], [1, 1, 1, 1, 0, 0, 0], \
         [1, 0, 1, 0, 1, 0, 1], [1, 1, 1, 1, 1, 0, 0], [1, 0, 1, 0, 1, 1, 1]
bias = int(input("enter a bias"))
weights = [bias, -3, 5, 1, 2, -6, 3]
v, y, e, final = 0, 0, 0, 0
chan = 0
loop = 1
no = 0
desired = [1, -1, -1, -1, 1, -1, 1, 1, 1, -1]
while loop == 1:
    accurate = 10
    for i in range(len(inputs)):
        x = inputs[i]
        for z in range(len(weights)):
            v += x[z]*weights[z]
        if v >= 0:
            y = 1
        else:
            y = -1
        if y != desired[i]:
            e = desired[i] - y
        empty = []
        if e != 0:
            accurate -= 1
            for lol in range(1, len(weights)):
                chan = x[lol]*e
                empty.append(weights[lol]+chan)
            weights = empty
            weights.insert(0, bias)
        y = 0
        e = 0
        v = 0
    print((accurate / len(inputs)) * 100)
    no += 1
    if ((accurate/len(inputs))*100) >= 95:
        print(weights)
        print(no*len(inputs))
        disp = str(input("do you want to give a new input? - 1 for yes anything else for no"))
        if disp == "1":
            data = list(input("enter the data of length : " + str(len(weights)-1) + "\n"))
            newd = list()
            for lmao in range(len(data)):
                newd.append(int(data.pop(0)))
            newd.insert(0, 1)
            for lenth in range(len(newd)):
                final += weights[lenth]*newd[lenth]
            if final >= 0:
                print("it's on the positive side of the activation function")
            else:
                print("it's on the negative side of the activation function")
        break

