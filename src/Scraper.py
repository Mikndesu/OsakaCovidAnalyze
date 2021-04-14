import requests
import pandas as pd
import matplotlib.dates as mdates


class Scraper:

    _Temp_CSV_Path = "/tmp/summary.csv"

    df = None

    def download(self):
        osakaCovidDataCSVLink = "https://covid19-osaka.info/data/summary.csv"
        response = requests.get(osakaCovidDataCSVLink)
        with open(self._Temp_CSV_Path, 'wb') as saveFile:
            saveFile.write(response.content)
        return self

    def parse(self):
        self.df = pd.read_csv(self._Temp_CSV_Path, encoding='shift-jis')
        self.df = self.df.set_index('日付', drop=False)
        self.df["日付"] = mdates.date2num(self.df["日付"])
