import numpy as np
import matplotlib.pyplot as plt


class PoissonStream:
    def __init__(self, intensity, time):
        self.data = np.random.poisson(intensity, time)

    def plot(self):
        plt.figure()
        plt.hist(self.data, 100, normed=False)
        plt.grid()
        plt.hold()
        plt.xlabel("Number of call in time period")
        plt.ylabel("Count")
        plt.title("Poisson traffic stream")
        plt.show()

