import csv
import time
import re
import os
from bs4 import BeautifulSoup
import undetected_chromedriver as uc
from selenium_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium .webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

class FlipkartScrapper:
    def __init__(self, output_dir="data"):
        self.output_dir = output_dir
        os.makedirs(self.outpu_dir exist_ok=true)

    def get_top_reviews(self,product_url,count=2):
        pass

    def scrape_flipkart_products(self, query, max_products=2):
        pass


    def save_to_csv(self, data, output_path):
        pass


