import unittest
from src import Scraper


class Test(unittest.TestCase):
    scraper = Scraper.Scraper()

    def test_download(self):
        self.scraper.download()
        try:
            with open(self.scraper._Temp_CSV_Path, "r"):
                print()
        except FileNotFoundError:
            self.assertFalse(False)

    def test_csv(self):
        self.scraper.parse()
        print(self.scraper.df["2021-04-10":"2021-04-13"]["陽性人数"])
        self.assertFalse(False)
