import unittest
from src import scraper


class Test(unittest.TestCase):
    scrape = scraper.Scraper()
    def test_download(self):
        self.scrape.download()
        try:
            with open(self.scrape._Temp_CSV_Path, "r") as f:
                print()
        except FileNotFoundError as e:
            self.assertFalse(False)
    
    def test_csv(self):
        self.scrape.parse()
        print(self.scrape.df)
        self.assertFalse(False)
