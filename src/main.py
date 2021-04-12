import scraper
from matplotlib import pyplot
import matplotlib.dates as mdates
import numpy as np

if __name__ == "__main__":
    scrape = scraper.Scraper()
    scrape.download().parse()
    fig, ax = pyplot.subplots()
    ax.xaxis.set_major_locator(mdates.DayLocator(bymonthday=None, interval=60, tz=None))
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m"))
    ax.grid()
    ax.set_yticks(np.linspace(0, 900, 10))
    fig.suptitle("The number of Covid positive people of Osaka")
    pyplot.plot(scrape.df["日付"], scrape.df["陽性人数"])
    pyplot.show()
