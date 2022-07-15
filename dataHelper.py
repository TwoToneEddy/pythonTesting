import numpy as np
import matplotlib.pyplot as plt
import os
import math


class DataHelper:
    def __init__(self, dataFileName: str):
        """ Class to help with data analysis on mass photometery csv data set

        Args:
            dataFileName(str): Filename of csv data file. CSV must have header row
                and one header must be "masses_kDa"

        """
        # Derive absolute path
        self.filePath = f"{os.path.dirname(__file__)}/{dataFileName}"
        # Read CSV
        self.data = np.genfromtxt(self.filePath, dtype=float, delimiter=",", names=True)
        self.avgMass = None
        self.medianMass = None

    def calc_average_mass(self) -> float:
        """ Method to calculate average mass

        Returns:
            float: Float value representing the mean mass
        """
        self.avgMass = np.average(self.data["masses_kDa"])

        if math.isnan(self.avgMass):
            raise ValueError("NaN present in masses_kDa")

        return self.avgMass

    def calc_median_mass(self) -> float:
        """Method to calculate median mass

        Returns:
            float: Float value representing the median mass
        """
        self.medianMass = np.median(self.data["masses_kDa"])

        if math.isnan(self.medianMass):
            raise ValueError("NaN present in masses_kDa")

        return self.medianMass

    def plot_histogram(self, png_filename: str):
        """Method to plot histogram and save to png file

            Args:
                png_filename(str): Target filename 
        """
        if not self.avgMass:
            self.calc_average_mass()

        if not self.medianMass:
            self.calc_median_mass()

        plt.hist(self.data["masses_kDa"], color="c",bins=20)
        plt.axvline(x=self.avgMass, color="r", linestyle=":")
        plt.axvline(x=self.medianMass, color="g", linestyle=":")
        plt.legend(["Average", "Median"])
        plt.xlabel("masses_kDa")
        plt.savefig(png_filename)

