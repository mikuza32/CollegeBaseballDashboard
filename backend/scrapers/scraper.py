import requests
from bs4 import BeautifulSoup
import pandas as pd

class scraper:

    def __init__(self, url):
        self.url = url
        self.headers = {'User-Agent': 'Mozilla/5.0 (compatible; MyScraper/1.0)'}

    def fetch_page(self):
        response = requests.get(self.url, headers=self.headers)
        response.raise_for_status()
        return response.text

    def get_soup(self): 
        html = self.fetch_page()
        return BeautifulSoup(html, "html.parser")
    
    def parse(self):
        """Override method for subclass parsing"""
        raise NotImplementedError("Subclass must implement parse()")



    
