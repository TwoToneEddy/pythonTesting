import numpy as np
import matplotlib.pyplot as plt
import os


class DataHelper:
    def __init__(self, dataFileName):
        # Derive absolute path
        self.filePath = f"{os.path.dirname(__file__)}/{dataFileName}"

        # Read CSV
        self.data = np.genfromtxt(self.filePath, dtype=float, delimiter=",", names=True)
        self.avgMass = None
        self.medianMass = None

    def calc_average_mass(self):
        self.avgMass = np.average(self.data["masses_kDa"])
        return self.avgMass

    def calc_median_mass(self):
        self.medianMass = np.median(self.data["masses_kDa"])
        return self.medianMass

    def plot_histogram(self, png_filename):
        if not self.avgMass:
            self.calc_average_mass()

        if not self.medianMass:
            self.calc_median_mass()

        plt.hist(self.data["masses_kDa"], color="c")
        plt.axvline(x=self.avgMass, color="r", linestyle=":")
        plt.axvline(x=self.medianMass, color="g", linestyle=":")
        plt.legend(["Average", "Median"])
        plt.xlabel("masses_kDa")
        plt.savefig(png_filename)
        print("here")


d = DataHelper("eventsFitted.csv")
mass = d.calc_average_mass()
med = d.calc_median_mass()
print(mass)
print(med)
d.plot_histogram("image.png")
