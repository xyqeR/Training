import numpy as np

def sigmoid(x):
    return 1 / (1+np.exp(-x))

training_inputs = np.array([ [0,0,1],
                             [1,1,1],
                             [1,0,1],
                             [0,1,1]])

training_outputs = np.array([[0,1,1,0]]).T

np.random.seed(1)

synaptic_weight = 2 * np.random.random((3,1)) - 1

print("Random init weights:")
print(synaptic_weight)
for i in range(400000):
    input_layer = training_inputs
    outputs = sigmoid( np.dot(input_layer, synaptic_weight))

    err = training_outputs - outputs
    adjustment = np.dot(input_layer.T, err * (outputs * (1 - outputs)))

    synaptic_weight += adjustment

print("Weight after learn:")
print(synaptic_weight)

print("Result:")
print(outputs)
