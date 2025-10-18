#reference https://github.com/shayanthrn/NeuroEvolutionGamer also check this amazing game :D 
import numpy as np

# architecture:
#input : 81 neuron for board context, 4 neuron for 1 hot encoding of active table in total 85
#output : 9 neurons 1 hot encoded for choosing cell in active board

#layer_sizes = [85, 20, 1]
#input_neurons=np.array([[input1],[input2],[input3],[input4],[input5]])
# result=self.nn.forward(input_neurons)
class NeuralNetwork():

    def __init__(self, layer_sizes):
        self.layer1_weights = np.random.normal(size=(layer_sizes[1],layer_sizes[0])) #weights of layer 1 with normal initialization
        self.layer2_weights = np.random.normal(size=(layer_sizes[2],layer_sizes[1])) #weights of layer 2 with normal initialization
        self.biases1 = np.zeros((layer_sizes[1],1))
        self.biases2 = np.zeros((layer_sizes[2],1))


    def activation(self, x):  #sigmoid as activation function
        return 1 / (1 + np.exp(-x))

    def forward(self, input_neurons):  #feedforwarding
        hiddenlayer_neurons = self.activation(np.matmul(self.layer1_weights,input_neurons)+self.biases1)
        output_neurons = self.activation(np.matmul(self.layer2_weights,hiddenlayer_neurons)+self.biases2)
        return output_neurons