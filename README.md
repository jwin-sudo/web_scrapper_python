# Web Scraper Project

This project is a web scraper built using **Scrapy** and **Selenium**. It is designed to scrape articles from websites, extracting key information such as the title, content, updated date, and byline.

## Features

- Scrapes article titles, content, updated dates, and bylines from web pages.
- Handles JavaScript-rendered content using Selenium.
- Saves the scraped data to local files for further analysis.
- Customizable to scrape different websites by modifying the spider.

## Requirements

- Python 3.7+
- Scrapy
- Selenium
- ChromeDriver (managed automatically by `webdriver_manager`)

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd web_scrapper_python
   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Navigate to the Scrapy project directory:
   ```bash
   cd web_scraper
   ```

2. Run the spider with the desired URL:
   ```bash
   scrapy crawl quotes -a url=<article-url>
   ```
   Replace `<article-url>` with the URL of the article you want to scrape.

3. The spider will extract the following information:
   - **Title**: The title of the article.
   - **Content**: The main content of the article.
   - **Updated Date**: The last modified date of the article.
   - **Byline**: The author or attribution of the article.

4. The extracted data will be saved to a local file in the format `article-<page>.txt`.

## Example

To scrape the article at `https://edition.cnn.com/travel/article/scenic-airport-landings-2020/index.html`, run:
```bash
scrapy crawl quotes -a url=https://edition.cnn.com/travel/article/scenic-airport-landings-2020/index.html
```

The output will include the article's title, content, updated date, and byline, and save it to a file named `article-index.txt`.

## Notes

- Ensure that the website you are scraping allows web scraping by checking its `robots.txt` file.
- If the website uses JavaScript to load content, Selenium is used to render the page and extract the required data.

## License

This project is licensed under the MIT License. Feel free to use, modify, and distribute this project as per the license terms.