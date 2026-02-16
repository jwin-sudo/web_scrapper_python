from pathlib import Path
from turtle import title
from urllib import response
import scrapy
import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    
    custom_settings = {
        "USER_AGENT": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    
    def __init__(self, url=None, *args, **kwargs):
        super(QuotesSpider, self).__init__(*args, **kwargs)
        self.start_urls = [url] if url else []

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        title = response.xpath('//title/text()').get()  # Using XPath to get the title text
        print(f"Page Title: {title}")  # Print the title for debugging
        
        # Extract the main content of the article
        content = response.xpath('//section[contains(@name, "articleBody")]//p//text()').getall()
        article_text = " ".join(content)  # Combine all paragraphs into a single string
        print(f"Article Content: {article_text}")
        
        # Parse out information such as the article title, updated date, and byline to return separately to the user.
        updated_date = response.xpath('//meta[@property="article:modified_time"]/@content').get()
        print(f"Updated Date: {updated_date}")  # Print the updated date for debugging
        
        # Extract the byline using Selenium
        try:
            driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
            driver.get(response.url)

            script_data = driver.execute_script("return window.CNN.metadata;")
            byline = script_data.get("content", {}).get("byline", None)
            print(f"Byline: {byline}")
        except Exception as e:
            print(f"Error extracting byline: {e}")
        finally:
            driver.quit()