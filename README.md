# Web-Scrapping
📄 README.md for Scraping Repository
🕸️ Election Web Scrapers
Scrapy + Selenium Pipelines for Large-Scale Public Data Extraction










This repository contains two production-ready pipelines for extracting data from semi-structured government election portals:

Scrapy Pipeline – for ASP.NET-style multi-level dropdown websites

Selenium Pipeline – for JavaScript-heavy portals where Scrapy cannot load dynamic content

Both pipelines output clean CSVs, structured folders, and include resilience features like error handling, retries, and explicit waits.

🚀 Features
✔ Scrapy Pipeline

Handles dependent dropdowns (Post → District → Block → Panchayat)

Uses FormRequest.from_response to simulate ASP.NET postbacks

Extracts HTML tables using pandas.read_html

Saves data with a traceable folder structure

Lightweight, fast, scalable

✔ Selenium Pipeline

Automates dynamic voter portals

Detects dropdown population & loading overlays

Extracts JS-rendered tables

Produces combined CSV output

Useful when HTML is not visible to Scrapy

📂 Folder Structure
election-web-scrapers/
│
├── scrapy_election_scraper/
│   ├── spider.py
│   ├── README.md
│   ├── scrapy.cfg
│   └── raw_data/
│
├── selenium_dynamic_scraper/
│   ├── scrape_dynamic.py
│   ├── README.md
│   └── selenium_output/
│
├── requirements.txt
├── LICENSE
└── README.md   # (main)

🧾 Setup
Install dependencies
pip install -r requirements.txt

Install ChromeDriver (for Selenium)
sudo apt install chromium-chromedriver

▶️ Usage
Run Scrapy spider
cd scrapy_election_scraper
scrapy crawl winnings

Run Selenium scraper
cd selenium_dynamic_scraper
python scrape_dynamic.py

📊 Outputs
Scrapy
raw_data/<post>/<district>/<block>/<panchayat>.csv

Selenium
selenium_output/combined.csv

🔧 Skills Demonstrated

Data engineering

Web scraping (static + dynamic)

Form simulation (ASP.NET)

Selenium automation

HTML parsing

Pipeline design

Error handling & retries

📄 License

MIT License – see LICENSE.

🙋 Contact

LinkedIn: https://linkedin.com/in/trupti-vm/
