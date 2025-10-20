import numpy as np


class NeuralNetwork():

    def __init__(self):
        self.layer1_weights = np.random.normal(size=(20,90)) #weights of layer 1 with normal initialization
        self.layer2_weights = np.random.normal(size=(9,20)) #weights of layer 2 with normal initialization
        self.biases1 = np.zeros((20,1))
        self.biases2 = np.zeros((9,1))

    def activation(self, x):  #sigmoid as activation function
        return 1 / (1 + np.exp(-x))

    def forward(self, input_neurons):  #feedforwarding
        hiddenlayer_neurons = self.activation(self.layer1_weights@input_neurons+self.biases1)
        output_neurons = self.activation(self.layer2_weights@hiddenlayer_neurons+self.biases2)
        return output_neurons