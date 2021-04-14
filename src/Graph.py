import Scraper
from matplotlib import pyplot
import matplotlib.dates as mdates
import numpy as np


class Graph:

    def __init__(self, fromDate=None, toDate=None):
        scraper = Scraper.Scraper()
        scraper.download().parse()
        self._scraper = scraper
        fig, ax = pyplot.subplots()
        ax.xaxis.set_major_locator(
            mdates.DayLocator(
                bymonthday=None,
                interval=60,
                tz=None))
        ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m"))
        ax.grid()
        ax.set_yticks(np.arange(0, 1200, 100))
        fig.suptitle("The number of Covid positive people of Osaka")
        if fromDate is None:
            pyplot.plot(self._scraper.df["日付"], self._scraper.df["陽性人数"])
        else:
            pyplot.plot(self._scraper.df[fromDate:toDate]["日付"], self._scraper.df[fromDate:toDate]["陽性人数"])

    def saveGraphAsPNG(self, savedTo=None):
        if savedTo is not None:
            customPath = savedTo + "OsakaCovidGraph"
            pyplot.savefig(customPath)
        else:
            pyplot.savefig("OsakaCovidGraph")

    def plot(self):
        pyplot.show()
