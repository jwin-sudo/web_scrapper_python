from pathlib import Path
from turtle import title
import scrapy

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    
    custom_settings = {
        "USER_AGENT": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    
    def __init__(self, url=None, *args, **kwargs):
        super(QuotesSpider, self).__init__(*args, **kwargs)
        print(f"Received URL: {url}")  # Debugging: Print the received URL
        self.start_urls = [url] if url else []

    def start_requests(self):
        for url in self.start_urls:
            print(f"Starting request for URL: {url}")  # Debugging: Confirm request is being made
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        print("Parse method called")  # Debugging: Confirm parse is called
        print(f"Scraping URL: {response.url}")  # Debugging: Print the response URL
        title = response.xpath('//title/text()').get()  # Using XPath to get the title text
        print(f"Page Title: {title}")  # Print the title for debugging
        
        # Extract the main content of the article
        content = response.xpath('//section[contains(@name, "articleBody")]//p//text()').getall()
        article_text = " ".join(content)  # Combine all paragraphs into a single string
        print(f"Article Content: {article_text}")
