from keras import layers
from keras import Model

class NeuralNetwork(Model):
    def __init__(self):
        super().__init__()
        self.fc1 = layers.Dense(20, activation='relu', kernel_initializer='he_normal')
        self.fc2 = layers.Dense(9, activation='relu', kernel_initializer='he_normal')

    def forward(self, x):
        print(f"input: {x}")
        x = self.fc1(x)
        x = self.fc2(x)
        print(f"output: {x}")
        return x