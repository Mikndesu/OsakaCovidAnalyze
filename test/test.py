import unittest
from src import scraper


class Test(unittest.TestCase):
    def test_download(self):
        scrape = scraper.Scraper()
        scrape.download()
        try:
            with open(scrape._Temp_CSV_Path, "r") as f:
                print()
        except FileNotFoundError as e:
            self.assertFalse(False)
