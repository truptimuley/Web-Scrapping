import scrapy
from scrapy import FormRequest
from selectolax.parser import HTMLParser
from pathlib import Path
import pandas as pd

class WinningsSpider(scrapy.Spider):
    name = "winnings"
    start_urls = ["https://sec2021.bihar.gov.in/claim-objection/Final_WinningList.aspx"]

    def parse(self, response):
        html = HTMLParser(response.text)
        posts = html.css("select#ctl00_ContentPlaceHolder1_ddl_Post > option")[1:]

        for opt in posts:
            yield FormRequest.from_response(
                response,
                formdata={"ctl00$ContentPlaceHolder1$ddl_Post": opt.attributes.get("value")},
                callback=self.parse_district,
                meta={"post": opt.text()}
            )

    def parse_district(self, response):
        html = HTMLParser(response.text)
        dists = html.css("select#ctl00_ContentPlaceHolder1_ddlDistrict > option")[1:]

        for opt in dists:
            yield FormRequest.from_response(
                response,
                formdata={"ctl00$ContentPlaceHolder1$ddlDistrict": opt.attributes.get("value")},
                callback=self.parse_block,
                meta={**response.meta, "district": opt.text()}
            )

    def parse_block(self, response):
        html = HTMLParser(response.text)
        blocks = html.css("select#ctl00_ContentPlaceHolder1_ddlBlock > option")[1:]

        for opt in blocks:
            yield FormRequest.from_response(
                response,
                formdata={"ctl00$ContentPlaceHolder1$ddlBlock": opt.attributes.get("value")},
                callback=self.parse_panchayat,
                meta={**response.meta, "block": opt.text()}
            )

    def parse_panchayat(self, response):
        html = HTMLParser(response.text)
        pans = html.css("select#ctl00_ContentPlaceHolder1_ddlPanchayat > option")[1:]

        for opt in pans:
            yield FormRequest.from_response(
                response,
                formdata={"ctl00$ContentPlaceHolder1$ddlPanchayat": opt.attributes.get("value")},
                callback=self.save_table,
                meta={**response.meta, "panchayat": opt.text()}
            )

    def save_table(self, response):
        post = response.meta["post"]
        dist = response.meta["district"]
        block = response.meta["block"]
        panch = response.meta["panchayat"]

        out_dir = Path("scrapy_election_scraper/raw_data") / post / dist / block
        out_dir.mkdir(parents=True, exist_ok=True)

        file_path = out_dir / f"{panch}.csv"

        dfs = pd.read_html(response.text)
        if dfs:
            dfs[0].to_csv(file_path, index=False)
            self.log(f"Saved {file_path}")

