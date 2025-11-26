# Web Scraper [Local Bodies]

Scrapy and Selenium pipelines for large-scale public data extraction.

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Scrapy](https://img.shields.io/badge/Scrapy-Production-green)
![Selenium](https://img.shields.io/badge/Selenium-Automation-orange)
![License](https://img.shields.io/badge/License-MIT-success)
![Status](https://img.shields.io/badge/Maintained-Yes-brightgreen)

This repository contains two production-ready pipelines for extracting data from semi-structured and dynamic portals:

1. **Scrapy Pipeline** – for ASP.NET-style dropdown navigation
2. **Selenium Pipeline** – for JavaScript-heavy, dynamic pages

All modules output clean CSVs and use reproducible folder structures.

---

## Features

### Scrapy Pipeline

* Handles dependent dropdowns (Post → District → Block → Panchayat)
* Uses `FormRequest.from_response` for ASP.NET postbacks
* Extracts HTML tables with `pandas.read_html`
* Outputs data in a structured folder hierarchy
* Fast and scalable

### Selenium Pipeline

* Handles JavaScript-rendered portals
* Waits for dynamic elements and loading overlays
* Extracts tables directly from rendered HTML
* Produces combined CSV output

---

## Repository Structure

```
election-web-scrapers/
|
├── scrapy_election_scraper/
│   ├── spider.py
│   ├── README.md
│   ├── scrapy.cfg
│   └── raw_data/
|
├── selenium_dynamic_scraper/
│   ├── scrape_dynamic.py
│   ├── README.md
│   └── selenium_output/
|
├── requirements.txt
├── LICENSE
└── README.md
```

---

## Installation

Clone the repository:

```
git clone https://github.com/<your-username>/election-web-scrapers.git
cd election-web-scrapers
```

Install dependencies:

```
pip install -r requirements.txt
```

For Selenium, install ChromeDriver:

```
# Ubuntu
sudo apt install chromium-chromedriver

# Mac (with Homebrew)
brew install chromedriver
```

---

## Usage

### Run Scrapy spider

```
cd scrapy_election_scraper
scrapy crawl winnings
```

The scraped CSVs will appear under:

```
scrapy_election_scraper/raw_data/
```

---

### Run Selenium scraper

```
cd selenium_dynamic_scraper
python scrape_dynamic.py
```

Output file:

```
selenium_dynamic_scraper/selenium_output/combined.csv
```

---

## Output Examples

### Scrapy

```
raw_data/
├── Post1
│   ├── District1
│   │   ├── Block1
│   │   │   ├── PanchayatA.csv
│   │   │   └── PanchayatB.csv
```

### Selenium

```
selenium_output/
└── combined.csv
```

---

## License

This project is licensed under the MIT License.
See the file `LICENSE`.

---

## Contact

LinkedIn: [https://linkedin.com/in/trupti-vm/](https://linkedin.com/in/trupti-vm/)

---
