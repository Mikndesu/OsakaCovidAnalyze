import requests


class Scraper:

    _Temp_CSV_Path = "/tmp/summary.csv"

    def download(self):
        osakaCovidDataCSVLink = "https://covid19-osaka.info/data/summary.csv"
        response = requests.get(osakaCovidDataCSVLink)
        with open(self._Temp_CSV_Path, 'wb') as saveFile:
            saveFile.write(response.content)
